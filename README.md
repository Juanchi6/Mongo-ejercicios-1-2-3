# Práctico de MongoDB: ejercicios 1, 2 y 3

**Estudiante:** Juan Ignacio Burghi  
**Asignatura:** Big Data · Universidad Católica del Uruguay

## Introducción

Este documento se utilizará para registrar la resolución de los ejercicios de MongoDB sobre los datos de IMDb, correspondientes a las páginas 102, 103 y 105 de la presentación «Clase 4 - 5 - NoSQL 2026».

El trabajo comprende la configuración del entorno, la importación de `title.basics`, `title.ratings` y `name.basics`, la justificación del modelo documental, las consultas, las agregaciones y las modificaciones solicitadas. RocketDB corresponde a una entrega anterior; los ejercicios 4 y 5 quedan fuera del alcance de esta entrega.

**Estado:** en elaboración. MongoDB está funcionando en Docker y conectado desde Compass. Se importaron 12.881.680 documentos en `titulos` y 1.723.150 en `ratings`, con cuatro evidencias incorporadas. Restan las personas, la justificación del modelo y la resolución de los ejercicios.

## 1. Entorno e importación de los datos

### 1.1. MongoDB en Docker

Se creó un contenedor de MongoDB Community Server utilizando la imagen `mongodb/mongodb-community-server:8.0-ubi8`. Desde PowerShell se ejecutó:

```powershell
docker run -d --name mongodb-imdb-burghi -p 127.0.0.1:27017:27017 -v mongodb-imdb-burghi-data:/data/db mongodb/mongodb-community-server:8.0-ubi8
```

Docker descargó la imagen y devolvió el identificador del contenedor, cuyo prefijo es `e3ffd0fdfcdb`. El puerto 27017 del contenedor se publicó en `127.0.0.1:27017` para permitir la conexión desde el mismo equipo. El volumen `mongodb-imdb-burghi-data`, montado en `/data/db`, se utiliza para conservar los datos entre ejecuciones del contenedor.

En Docker Desktop se comprobó que el contenedor estaba en ejecución: la fila muestra el indicador verde, el mismo prefijo de identificador y el mapeo `27017:27017`. También se observa el estado **Engine running**.

![Contenedor de MongoDB en ejecución en Docker Desktop](evidencias/01_mongodb_docker.png)

*Figura 1. MongoDB en Docker Desktop: contenedor activo y puerto 27017 publicado. Captura del 20 de octubre de 2026.*

### 1.2. Conexión desde MongoDB Compass

Se agregó una conexión con la URI `mongodb://127.0.0.1:27017`, utilizando el nombre **IMDb local - Docker**. La conexión permite acceder desde Compass al servidor MongoDB que se está ejecutando en el contenedor local.

La captura muestra la conexión activa con indicador verde y las bases del sistema `admin`, `config` y `local`. En esta etapa todavía no se había creado la base del práctico ni importado los archivos de IMDb.

![Conexión local activa en MongoDB Compass](evidencias/02_conexion_compass.png)

*Figura 2. Compass conectado a IMDb local - Docker, con las bases del sistema disponibles.*

### 1.3. Preparación de los archivos de IMDb

Se descargaron los tres archivos completos de IMDb y se convirtieron de TSV comprimido a JSON con un documento por línea, para poder importarlos desde Compass. Se conservaron todos los registros y los identificadores originales; se normalizaron los campos numéricos, los arrays y los valores ausentes antes de la carga.

El procedimiento reproducible, los recuentos de origen y los hashes de las fuentes se detallan en [Fuentes y preparación de los datos](datos/README.md).

La preparación se comprobó por separado de la carga en MongoDB. A continuación se registra cada importación con su recuento y su evidencia.

### 1.4. Importación de los títulos

Se creó la base `imdb_burghi_2026` y la colección `titulos`. Desde **Add Data → Import JSON or CSV file** se seleccionó `titulos.json`, generado a partir del archivo completo `title.basics.tsv.gz`.

Compass confirmó **Import completed: 12.881.680 documents imported**. El total coincide con los 12.881.680 registros de la fuente. La captura muestra también la base y colección utilizadas y documentos de ejemplo: `startYear` y `runtimeMinutes` aparecen como números, `endYear` como `null` cuando falta el dato y `genres` como array. El identificador original de IMDb se conserva en `_id`.

![Importación completa de los títulos de IMDb](evidencias/03_importacion_titulos.png)

*Figura 3. Colección titulos con 12.881.680 documentos y confirmación de importación completada en MongoDB Compass.*

### 1.5. Importación de las valoraciones

Dentro de `imdb_burghi_2026` se creó la colección normal `ratings`, con la opción Time Series desactivada. Desde **Add Data → Import JSON or CSV file** se importó `ratings.json`, preparado a partir del archivo completo `title.ratings.tsv.gz`.

Compass confirmó **Import completed: 1.723.150 documents imported**, y el mismo total aparece en la navegación de documentos. El recuento coincide con el de la fuente. Los documentos muestran el identificador del título en `_id` y los campos numéricos `averageRating` y `numVotes`. Por ejemplo, para `tt0000001` se observa una valoración de `5.7` y `2237` votos.

![Importación completa de las valoraciones de IMDb](evidencias/04_importacion_ratings.png)

*Figura 4. Colección ratings con 1.723.150 documentos y confirmación de importación completada en MongoDB Compass, el 22 de octubre de 2026.*

### Avance de la configuración

- [x] MongoDB funcionando en Docker.
- [x] Conexión desde MongoDB Compass.
- [x] Importación de `title.basics` en `titulos`: 12.881.680 documentos.
- [x] Importación de `title.ratings` en `ratings`: 1.723.150 documentos.
- [ ] Importación de `name.basics` en `personas` y comprobación del recuento.
- [ ] Modelo de documentos, tipos de datos y justificación.

## 2. Ejercicio 1: consultas

Pendiente de ejecución y documentación.

- [ ] Buscar la película Fight Club.
- [ ] Buscar Fight Club de 1999.
- [ ] Mostrar las películas de 1999.
- [ ] Mostrar las películas posteriores a 1999.
- [ ] Consultar los títulos con un valor de `endYear`.
- [ ] Comparar `endYear` con `startYear`.

La interpretación de las dos últimas consultas se explicará al documentarlas: la consigna utiliza el término «películas», mientras que IMDb define `endYear` para series de televisión.

## 3. Ejercicio 2: agregaciones

Pendiente de ejecución y documentación.

- [ ] Ordenar por `startYear` los títulos cuyo `endYear` sea mayor que `startYear`.
- [ ] Contar las películas de 1999.
- [ ] Contar las películas de género Western.
- [ ] Generar un array con los títulos de los westerns.
- [ ] Agrupar los títulos de los westerns por género, explicitando el criterio utilizado.

## 4. Ejercicio 3: modificaciones

Pendiente de ejecución y documentación.

- [ ] Localizar Fight Club de 1999.
- [ ] Agregar la etiqueta de género «Comedia oscura».
- [ ] Incorporar director, director de fotografía, producción y elenco, citando las fuentes de los créditos.
- [ ] Insertar Shrek 5 con los valores indicados en la consigna y explicar el tratamiento de los datos ausentes.
- [ ] Consultar los documentos resultantes para verificar las modificaciones.

## Evidencias

Las capturas se guardarán en [`evidencias/`](evidencias/README.md). Se incorporarán al documento junto al paso que demuestran, con numeración y una explicación breve. Las consultas y sus resultados deberán ser legibles; los resultados vacíos también se documentarán cuando correspondan.

## Fuentes

- Presentación de clase: «Clase 4 - 5 - NoSQL 2026», páginas 102, 103 y 105.
- Consigna de entrega: «Ejercicio MongoDB (1 al 3)» y aviso del docente del 14 de octubre de 2026.
- [IMDb Non-Commercial Datasets](https://data.imdb.com/non-commercial-datasets/).
