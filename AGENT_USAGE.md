# ANEXO — Uso de Inteligencia Artificial Generativa (IAG)

Este archivo documenta los diálogos mantenidos con IAG (Claude) durante la resolución del examen integrador de Estructura de Datos. La herramienta fue utilizada **únicamente como acompañamiento conceptual**: para aclarar dudas sobre estructuras, algoritmos y decisiones de diseño. La implementación, depuración y redacción final son producción propia.

## Declaración de autoría

Declaro que el código, las decisiones de diseño y las explicaciones contenidas en este examen son de mi autoría. La IAG fue consultada como apoyo conceptual (equivalente a consultar bibliografía o un tutor), nunca como generadora de la entrega. Las respuestas de la IAG fueron interpretadas, adaptadas y, cuando correspondió, descartadas según mi propio criterio.

— Gonzalo Alvarez

## Diálogos consultados

| Hora y fecha | Resumen del prompt | Resumen de la respuesta |
|---|---|---|
| 2026-06-02 | Diferencia entre clase y función para modelar `EventStore`/`Index`; por qué carpetas + `__init__.py`. | Explicó SRP, encapsulamiento y cohesión; aclaró que `__init__.py` es archivo aparte que marca paquete. |
| 2026-06-03 | Por qué `heapq` en vez de lista ordenada para `PriorityQueue`; cómo evitar `TypeError` al comparar `Event`. | Comparó complejidades insertar/extraer; recomendó tupla `(priority, counter, event)` para desempate FIFO. |
| 2026-06-03 | Diferencia entre `list.pop(0)` y `deque.popleft()` para FIFO. | Aclaró O(n) vs O(1) y por qué `deque` es la elección correcta para colas. |
| 2026-06-04 | Cuándo conviene búsqueda binaria sobre secuencial; rol del parámetro `key`. | Trade-off de ordenar una vez vs muchas búsquedas; `key` evita necesitar `__lt__` en la clase. |
| 2026-06-04 | Cómo funcionan los decoradores apilados y `functools.wraps`. | Equivalencia con HOF, orden de aplicación de abajo hacia arriba, por qué `wraps` preserva metadatos. |
| 2026-06-04 | Qué es una colisión real en hashing y cómo la resuelve `dict` de Python. | Diferenció colisión (claves distintas → mismo bucket) de sobrescritura; explicó open addressing en CPython. |
| 2026-06-08 | Cómo articular trade-off tiempo vs memoria en la síntesis del Punto 5. | Sugirió ejes (Merge vs Bubble, Index vs búsqueda) y la idea de mantenibilidad como resultado emergente. |
| 2026-06-10 | Intuición de Union-Find: compresión de caminos y unión por rango; por qué α(n) ≈ O(1). | Explicó representación con array `parent`, función inversa de Ackermann y conexión con Kruskal. |
| 2026-06-13 | Diferencia BFS/DFS y por qué Dijkstra necesita el chequeo `if current_dist > distances[current]`. | Cola vs pila como diferencia estructural; chequeo evita procesar entradas viejas del heap. |
| 2026-06-13 | Cómo construir la tabla LPS de KMP y por qué da O(n+m). | Definición prefijo/sufijo, idea de que `i` no retrocede, ejemplo paso a paso con `"abab"`. |
| 2026-06-13 | Rol del Pequeño Teorema de Fermat en RSA y por qué `pow(b,e,m)` evita explotar con primos grandes. | Explicó exponenciación modular rápida O(log e) y por qué cifrar carácter a carácter es educativo, no seguro. |

## Manera en que la herramienta ayudó

- **Aclaración conceptual** de estructuras (heap, deque, hash, Union-Find, grafos) cuando la bibliografía resultaba densa o ambigua.
- **Discusión de criterios** de diseño en abstracto (composición vs herencia, dónde aterriza cada responsabilidad), sin entrar en mi código.
- **Repaso de conceptos teóricos** que yo tenía mal interpretados (ej. confusión entre colisión y sobrescritura, alcance real de `@property`). Una vez aclarado el concepto, las correcciones al código las hice yo.
- **Refuerzo del "por qué"** detrás de cada decisión, lo que se reflejó en `APRENDIZAJES.md` y en los README escritos por mí.

La IAG **no** revisó mi código ni generó código que se haya copiado a la entrega: todas las implementaciones fueron escritas, probadas y depuradas manualmente. La interacción se limitó a consultas conceptuales (equivalentes a consultar bibliografía o un tutor) y nunca incluyó pegado de archivos del proyecto.
