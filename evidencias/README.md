# Evidencias de ejecución

Esta carpeta reúne las capturas de los resultados clave del práctico.

## Capturas incorporadas

| Figura | Archivo | Resultado documentado |
|---|---|---|
| 1 | [MongoDB en Docker](01_mongodb_docker.png) | Contenedor en ejecución, identificador `e3ffd0fdfcdb`, puerto `27017:27017` y motor de Docker activo. |
| 2 | [Conexión desde Compass](02_conexion_compass.png) | Conexión IMDb local - Docker activa y bases del sistema admin, config y local visibles. |
| 3 | [Importación de títulos](03_importacion_titulos.png) | Importación completada en imdb_burghi_2026.titulos: 12.881.680 documentos. |
| 4 | [Importación de valoraciones](04_importacion_ratings.png) | Importación completada en imdb_burghi_2026.ratings: 1.723.150 documentos. |
| 5 | [Importación de personas](05_importacion_personas.png) | Importación completada en imdb_burghi_2026.personas: 15.750.813 documentos. |
| 6 | [Búsqueda de Fight Club](06_consulta_fight_club.png) | Documentos de las películas Fight Club de 1999 y 2023 visibles; contador total N/A. |
| 7 | [Fight Club de 1999](07_consulta_fight_club_1999.png) | Filtro completo y un único resultado: tt0137523, Fight Club, 1999. |
| 8 | [Películas de 1999](08_consulta_peliculas_1999.png) | Filtro completo y listado de películas de 1999: 5.154 resultados. |
| 9 | [Películas posteriores a 1999](09_consulta_peliculas_posteriores_1999.png) | Filtro startYear mayor que 1999: 388.352 resultados. |
| 10 | [Películas con endYear](10_consulta_peliculas_endyear_sin_resultados.png) | Consulta literal sobre movie con endYear numérico: cero coincidencias y mensaje No results. |
| 11 | [Títulos con endYear](11_consulta_titulos_con_endyear.png) | Consulta complementaria sobre todos los tipos: 163.284 resultados, con ejemplos de tvSeries. |

Las capturas se renombran con un número y una descripción breve al incorporarlas al documento.

## Criterio de registro

- Capturar el entorno funcionando, las importaciones completas, las consultas y agregaciones con sus resultados, y las modificaciones verificadas.
- Evitar capturas de descargas, menús o pasos intermedios que no demuestren un resultado.
- Mantener legibles el nombre de la base y colección, el filtro o pipeline utilizado y su resultado. Una consulta sin resultados también es una evidencia válida si se muestra el filtro y se explica.
- Usar nombres numerados y descriptivos, por ejemplo `01_mongodb_docker.png`. El nombre concreto se indicará al llegar a cada captura.
- Incorporar cada imagen al documento principal con un pie de figura y una explicación del resultado observado.

El documento principal está en [`README.md`](../README.md).
