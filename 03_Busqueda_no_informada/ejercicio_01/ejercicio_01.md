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

Para mi análisis, decidí utilizar como punto de partila la ciudad de **Zerind** hacia **Vasliu**. He aquí los resultados que obtuve con cada uno de los algoritmos que utilicé:

## Evidencias 
| Breadth-first search | Depth-first search |
| :---: | :---: |
| ![ Breadth-first search](Imagenes/Breadth-first%20search.png) | ![Depth-first search](Imagenes/Depth-first%20search.png) |
| Uniform-cost search| Iterative_deepening search |
| ![Uniform-cost search](Imagenes/Uniform-cost%20search.png) | ![Iterative_deepening search](Imagenes/Iterative_deepening%20search.png) |
| Depth-limited search (6)|  |
| ![Depth-limited search (limit 6)](Imagenes/Depth-limited%20search%206.png) | |

## Tabla comparativa del performance de los algoritmos bajo el mismo problema (Zerind hacia Vasliu)
| Algoritmo | Status | Path | Depth | Cost | Expanded | Generated |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| Breadth-first search | success | Zerind → Arad → Sibiu → Fagaras → Bucharest → Urziceni → Vaslui | 6 roads | 752 km | 14 nodes | 37 nodes |
| Uniform-cost search | success | Zerind → Arad → Sibiu → Rimnicu Vilcea → Pitesti → Bucharest → Urziceni → Vaslui | 7 roads | 720 km | 16 nodes | 41 nodes |
| Depth-first search | success | Zerind → Arad → Sibiu → Fagaras → Bucharest → Urziceni → Vaslui | 6 roads | 752 km | 14 nodes | 35 nodes |
| Depth-limited search (limit 2) | cutoff | NA | NA | NA | 3 nodes | 8 nodes |
| Depth-limited search (limit 4) | cutoff | NA | NA | NA | 13 nodes | 35 nodes |
| Iterative deepening search | success | Zerind → Arad → Sibiu → Fagaras → Bucharest → Urziceni → Vaslui | 6 roads | 752 km | 52 nodes | 141 nodes |

***

## Breve reporte

De manera general, podemos decir que BFS encontró el camino con menos carreteras, pero no singnica que fue el único algorimtmo que lo logró. Muy probablemente por el punto de inicio y final que elegí, pero el performance de BFS es equiparable al desempeño que tuvo el Depth first search y el Iterative deepening search. En términos de costo por KM, el UCS fue efectivamente el más eficiente aunque fue tambiém el que utilizó más nodos en su grafo.

No aplicó para mi caso en particular, sin embargo, es importante mencionar que el DFS pudiera devolver un camino más largo aunque el grafo sea el mismo. Esto es por la naturaleza del mismo algoritmo que lo que hace es explorar la totalidad de una rama antes de pasar a la siguiente para encontrar la más optima. Precisamente por esta "exploración" es suceptible a ciclarse y jamás encontrar una respuesta, y aunque esto es un caso catastrófico, estaríamos creando un camino infinito dentro de un mismo grafo.
Utilizando el algoritmo de DLS, tuve que utilizar un limit de 6 para que por fin pudidera pasar de un cutoff a una solución real a mi problema, que fue justamente la profundidad que utilizó BFS.

***

Como parte de mis evidencias, [adjunto aquí screenshots de las veces que corrí los algoritmos](Evidencias)