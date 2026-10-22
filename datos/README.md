# Fuentes y preparación de los datos de IMDb

Se descargaron el 20 de octubre de 2026 los tres archivos completos indicados por la consigna desde [IMDb Non-Commercial Datasets](https://data.imdb.com/non-commercial-datasets/). Los datos de IMDb se actualizan diariamente, por lo que los recuentos dependen de la fecha de descarga.

## Archivos utilizados

| Fuente | Archivo preparado para Compass | Colección prevista | Registros en la fuente |
|---|---|---|---:|
| [title.basics.tsv.gz](https://datasets.imdbws.com/title.basics.tsv.gz) | `titulos.json` | `titulos` | 12.881.680 |
| [title.ratings.tsv.gz](https://datasets.imdbws.com/title.ratings.tsv.gz) | `ratings.json` | `ratings` | 1.723.150 |
| [name.basics.tsv.gz](https://datasets.imdbws.com/name.basics.tsv.gz) | `personas.json` | `personas` | 15.750.813 |

Los recuentos de la tabla anterior corresponden a los archivos fuente. La carga en MongoDB se comprueba por separado con evidencias de ejecución.

## Estado de la importación

| Colección | Documentos importados verificados | Evidencia |
|---|---:|---|
| `titulos` | 12.881.680 | [Figura 3: importación completada](../evidencias/03_importacion_titulos.png) |
| `ratings` | 1.723.150 | [Figura 4: importación completada](../evidencias/04_importacion_ratings.png) |
| `personas` | Pendiente | Pendiente |

Los archivos de datos se conservan localmente. En el repositorio se registra el procedimiento para reproducir su preparación.

## Conversión para Compass

El script [`scripts/preparar_imdb_compass.py`](../scripts/preparar_imdb_compass.py) lee los archivos TSV comprimidos y genera JSON con un documento por línea. Procesa todos los registros, sin seleccionar una muestra. Este formato permite importar los datos desde Compass.

Durante la conversión se aplican las siguientes reglas:

- `tconst` pasa a ser `_id` en `titulos` y `ratings`; `nconst` pasa a ser `_id` en `personas`. Se conserva el identificador original como clave del documento.
- Los años, la duración, `numVotes` e `isAdult` se convierten a enteros cuando tienen valor. `averageRating` se convierte a número decimal.
- `genres`, `primaryProfession` y `knownForTitles` se convierten en arrays de cadenas.
- El marcador `\N` se representa como `null` en campos escalares y como array vacío en los multivaluados.
- Se conservan todos los tipos de título. Esto permite consultar también los años de finalización de las series.

El script solo prepara archivos: no se conecta a MongoDB ni realiza consultas o modificaciones en la base. Utiliza la biblioteca estándar de Python y puede ejecutarse así, indicando las carpetas correspondientes:

```text
python scripts/preparar_imdb_compass.py --entrada carpeta_con_los_gz --salida datos_imdb
```

Cada conversión produce también un archivo `.preparacion.json` con el número de documentos, el tamaño y los hashes SHA256 de la fuente y del resultado. La lectura completa comprueba la integridad gzip; se comprueban los encabezados, la cantidad de columnas y la conversión de los campos numéricos.

## Identificación de las fuentes utilizadas

| Fuente | SHA256 del archivo comprimido |
|---|---|
| `title.basics.tsv.gz` | `9c5628538083daf4bae92fb8945d36d7d736f6e1a83d570ce0b2498f94b56fa1` |
| `title.ratings.tsv.gz` | `68b1df796e1b316d923de8aa16271fee5436c98bc1f453f114c2c842166aed05` |
| `name.basics.tsv.gz` | `6457218f7a98410ea5cd95ff2c1f460f89b9f91403affacbac249a775f56a596` |
