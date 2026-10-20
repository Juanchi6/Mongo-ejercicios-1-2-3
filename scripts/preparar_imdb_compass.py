"""Convierte fuentes IMDb completas a JSON por linea para importar en Compass.

No se conecta a MongoDB ni ejecuta consultas o modificaciones.
Uso: python preparar_imdb_compass.py --entrada carpeta_gz --salida carpeta_json
"""
import argparse
import concurrent.futures
import csv
import gzip
import hashlib
import json
import time
from datetime import datetime, timezone
from pathlib import Path


def integer(value):
    return None if value == '\\N' else int(value)


def string(value):
    return None if value == '\\N' else value


def array(value):
    return [] if value == '\\N' else value.split(',')


def title(r):
    return dict(_id=r[0], titleType=string(r[1]), primaryTitle=string(r[2]),
                originalTitle=string(r[3]), isAdult=integer(r[4]),
                startYear=integer(r[5]), endYear=integer(r[6]),
                runtimeMinutes=integer(r[7]), genres=array(r[8]))


def rating(r):
    return dict(_id=r[0], averageRating=None if r[1] == '\\N' else float(r[1]),
                numVotes=integer(r[2]))


def person(r):
    return dict(_id=r[0], primaryName=string(r[1]), birthYear=integer(r[2]),
                deathYear=integer(r[3]), primaryProfession=array(r[4]), knownForTitles=array(r[5]))


SPECS = {
    'titulos': ('title.basics', title, ['tconst', 'titleType', 'primaryTitle', 'originalTitle',
                                     'isAdult', 'startYear', 'endYear', 'runtimeMinutes', 'genres']),
    'ratings': ('title.ratings', rating, ['tconst', 'averageRating', 'numVotes']),
    'personas': ('name.basics', person, ['nconst', 'primaryName', 'birthYear', 'deathYear',
                                      'primaryProfession', 'knownForTitles']),
}


def convert(task):
    collection, input_dir, output_dir = task
    source, transform, columns = SPECS[collection]
    original = Path(input_dir) / f'{source}.tsv.gz'
    target = Path(output_dir) / f'{collection}.json'
    partial = target.with_suffix('.json.part')
    receipt = target.with_suffix('.preparacion.json')
    if target.exists() or receipt.exists():
        raise FileExistsError(f'{collection}: ya existe una salida; revisar antes de repetir')
    start = time.monotonic()
    with original.open('rb') as source_file:
        original_sha = hashlib.file_digest(source_file, 'sha256').hexdigest()
    count = 0
    digest = hashlib.sha256()
    first = last = None
    with gzip.open(original, 'rt', encoding='utf-8', newline='') as inp, partial.open('wb', buffering=4*1024*1024) as out:
        rows = csv.reader(inp, delimiter='\t', quoting=csv.QUOTE_NONE)
        header = next(rows)
        if header != columns:
            raise ValueError(f'{source}: encabezado inesperado {header}')
        for line_number, row in enumerate(rows, 2):
            if len(row) != len(columns):
                raise ValueError(f'{source}: cantidad de columnas incorrecta en linea {line_number}')
            try:
                doc = transform(row)
            except (ValueError, IndexError) as exc:
                raise ValueError(f'{source}: linea {line_number}: {exc}') from exc
            encoded = (json.dumps(doc, ensure_ascii=False, separators=(',', ':'), allow_nan=False)+'\n').encode('utf-8')
            out.write(encoded)
            digest.update(encoded)
            count += 1
            if first is None:
                first = doc
            last = doc
            if count % 2000000 == 0:
                print(f'{collection}: {count:,} documentos preparados ({time.monotonic()-start:.0f}s)', flush=True)
    # La lectura hasta EOF tambien verifica el CRC de cada archivo gzip.
    validation = Path(input_dir) / f'{source}.validacion.json'
    if validation.exists():
        expected = json.loads(validation.read_text(encoding='utf-8'))['rows']
        if expected != count:
            raise ValueError(f'{collection}: recuento inesperado {count}/{expected}')
    partial.replace(target)
    result = dict(collection=collection, source=original.name, source_sha256=original_sha,
                  output=target.name, output_sha256=digest.hexdigest(), documents=count,
                  bytes=target.stat().st_size, first_document=first, last_document=last,
                  prepared_at=datetime.now(timezone.utc).isoformat(),
                  seconds=round(time.monotonic()-start, 1),
                  status='preparado_para_importar_no_ejecutado_en_mongodb')
    receipt.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'{collection}: COMPLETO, {count:,} documentos, {target.stat().st_size:,} bytes', flush=True)
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--entrada', type=Path, required=True)
    parser.add_argument('--salida', type=Path, required=True)
    parser.add_argument('--coleccion', choices=[*SPECS, 'todas'], default='todas')
    args = parser.parse_args()
    args.salida.mkdir(parents=True, exist_ok=True)
    collections = list(SPECS) if args.coleccion == 'todas' else [args.coleccion]
    with concurrent.futures.ProcessPoolExecutor(max_workers=len(collections)) as pool:
        results = list(pool.map(convert, [(c, str(args.entrada.resolve()), str(args.salida.resolve())) for c in collections]))
    print(json.dumps([dict(collection=r['collection'], documents=r['documents'], bytes=r['bytes'])
                      for r in results], indent=2), flush=True)

