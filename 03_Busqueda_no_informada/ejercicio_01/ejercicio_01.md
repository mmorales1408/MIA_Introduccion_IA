## Objetivo

Elegir una ruta distinta de Arad → Bucharest, correr BFS, UCS, DFS, DLS e IDS,
y analizar diferencias de camino, costo, profundidad y nodos expandidos.

***

## Entrega

1. La pareja origen–destino elegida y un diagrama del subgrafo usado.
2. Una tabla comparativa con Path, Depth, Cost, Expanded (y Status en DLS).
3. Un breve reporte (media página) que responda:
   - ¿BFS encontró el camino con **menos carreteras**? ¿UCS el de **menos km**?
   - ¿Por qué DFS puede devolver un camino más largo aunque el grafo sea el
     mismo?
   - ¿Con qué `--limit` DLS pasó de `cutoff` a solución, y cómo se relaciona
     eso con la profundidad del camino de BFS/IDS?
4. Evidencias de haber ejecutado los cinco algoritmos.

***

Para mi análisis, decidí utilizar como punto de partila la ciudad de Zerind hacia Vasliu. He aquí los resultados que obtuve con cada uno de los algoritmos que utilicé:

### Evidencias 
| Breadth-first search | Depth-first search |
| :---: | :---: |
| ![ Breadth-first search](Imagenes/Breadth-first%20search.png) | ![Depth-first search](Imagenes/Depth-first%20search.png) |
| Uniform-cost search| Iterative_deepening search |
| ![Uniform-cost search](Imagenes/Uniform-cost%20search.png) | ![Iterative_deepening search](Imagenes/Iterative_deepening%20search.png) |
| Depth-limited search (6)|  |
| ![Depth-limited search (limit 6)](Imagenes/Depth-limited%20search%206.png) | |