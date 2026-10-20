# Práctico de MongoDB: ejercicios 1, 2 y 3

**Estudiante:** Juan Ignacio Burghi  
**Asignatura:** Big Data · Universidad Católica del Uruguay

## Introducción

Este documento se utilizará para registrar la resolución de los ejercicios de MongoDB sobre los datos de IMDb, correspondientes a las páginas 102, 103 y 105 de la presentación «Clase 4 - 5 - NoSQL 2026».

El trabajo comprende la configuración del entorno, la importación de `title.basics`, `title.ratings` y `name.basics`, la justificación del modelo documental, las consultas, las agregaciones y las modificaciones solicitadas. RocketDB corresponde a una entrega anterior; los ejercicios 4 y 5 quedan fuera del alcance de esta entrega.

**Estado:** en elaboración. Todavía no se han incorporado evidencias de ejecución. Las secciones se completarán con los pasos efectivamente realizados, sus resultados y las capturas correspondientes.

## 1. Entorno e importación de los datos

Pendiente de ejecución y documentación.

- [ ] MongoDB funcionando en Docker.
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
