# Práctico de MongoDB: ejercicios 1, 2 y 3

**Estudiante:** Juan Ignacio Burghi  
**Asignatura:** Big Data · Universidad Católica del Uruguay

## Introducción

Este documento se utilizará para registrar la resolución de los ejercicios de MongoDB sobre los datos de IMDb, correspondientes a las páginas 102, 103 y 105 de la presentación «Clase 4 - 5 - NoSQL 2026».

El trabajo comprende la configuración del entorno, la importación de `title.basics`, `title.ratings` y `name.basics`, la justificación del modelo documental, las consultas, las agregaciones y las modificaciones solicitadas. RocketDB corresponde a una entrega anterior; los ejercicios 4 y 5 quedan fuera del alcance de esta entrega.

**Estado:** en elaboración. MongoDB ya está funcionando en Docker y se incorporó la primera evidencia. La conexión desde Compass, la importación, el modelado y los ejercicios continúan pendientes.

## 1. Entorno e importación de los datos

### 1.1. MongoDB en Docker

Se creó un contenedor de MongoDB Community Server utilizando la imagen `mongodb/mongodb-community-server:8.0-ubi8`. Desde PowerShell se ejecutó:

```powershell
docker run -d --name mongodb-imdb-burghi -p 127.0.0.1:27017:27017 -v mongodb-imdb-burghi-data:/data/db mongodb/mongodb-community-server:8.0-ubi8
```

Docker descargó la imagen y devolvió el identificador del contenedor, cuyo prefijo es `e3ffd0fdfcdb`. El puerto 27017 del contenedor se publicó en `127.0.0.1:27017` para permitir la conexión desde el mismo equipo. El volumen `mongodb-imdb-burghi-data`, montado en `/data/db`, se utiliza para conservar los datos entre ejecuciones del contenedor.

En Docker Desktop se comprobó que el contenedor estaba en ejecución: la fila muestra el indicador verde, el mismo prefijo de identificador y el mapeo `27017:27017`. También se observa el estado **Engine running**.

![Contenedor de MongoDB en ejecución en Docker Desktop](evidencias/Captura%20de%20pantalla%202026-10-20%20201357.png)

*Figura 1. MongoDB en Docker Desktop: contenedor activo y puerto 27017 publicado. Captura del 20 de octubre de 2026.*

### Avance de la configuración

- [x] MongoDB funcionando en Docker.
- [ ] Conexión desde MongoDB Compass.
- [ ] Importación de los tres archivos de IMDb y comprobación de los recuentos.
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
