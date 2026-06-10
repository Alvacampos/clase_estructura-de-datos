# Examen

Examen Parcial de Algoritmos y Estructuras de Datos

Universidad Blas Pascal

Alumno: Gonzalo Ramiro Alvarez Campos

## Aclaracion
Cada parte de los ejercicio va quedar en un PR por separado para que sea mas facil evaluar.

# Plataforma de análisis de incidentes y rutas

## Descripción general

El sistema gestiona eventos/urgencias acorde a prioridad, categoría, origen y destino. La idea es poder crear un sistema que sea capaz de hacer un triage de los eventos y de gestionar el orden en el cual se procesan.

## Estructura del proyecto

```
Examen/
├── main.py                       # archivo principal (orquestador)
├── models/
│   └── event.py                  # modelo de los eventos: define la estructura
│                                 # y características que tiene un evento
├── storage/
│   ├── event_store.py            # almacenamiento de los eventos
│   └── index.py                  # gestión de la búsqueda de eventos
├── analisys/
│   └── text_analyzer.py          # análisis de textos de los distintos eventos
├── queues/
│   ├── priority_queue.py         # cola de prioridad (wrapper sobre heapq)
│   └── incident_queue.py         # cola FIFO de incidentes (wrapper sobre deque)
└── router/
    └── router.py                 # gestión de rutas (a desarrollar como grafo
                                  # en la parte 2)
```

## Decisiones de diseño

### ¿Por qué estas 5 clases?

Estas clases son los pilares de la app: permiten el manejo dinámico de variables basadas en modelos mutables, heredables y manipulables, pero con fundamentos bien definidos.

### Responsabilidades de cada clase

- **Event**: define la estructura y métodos de los eventos.
- **EventStore**: define la estructura y capacidades de almacenamiento.
- **Index**: define los métodos de búsqueda para eventos.
- **TextAnalyzer**: define los métodos para procesar textos.
- **Router**: gestiona las rutas y define el grafo.

### Relaciones entre clases

La clase `Event` es probablemente la más usada, ya que define los eventos: la variable base de todo el programa.

### ¿Por qué modularicé en carpetas?

Esta decisión es la más debatible: por lo general no hay una forma 100% correcta de estructurar un proyecto, depende mucho de los gustos y necesidades al momento de crearlo. Aquí modularicé para tener una separación de responsabilidades, lo que hace más fácil auditar el código y trabajar en él. La estructura tiene cierto parecido con el patrón MVC que se usa en el backend para el manejo de datos, donde tenemos una *source of truth* en los modelos, que son usados por los otros módulos y se muestran en `main` (en este caso).

### Ejercicio 2

#### Estructuras elegidas

- Para la `PriorityQueue` se utilizó **heap** (vía `heapq`) dado que es extremadamente fácil organizar prioridades con un sistema numérico donde el de mayor prioridad es el número más bajo (min-heap). Es un ordenamiento casi natural con poco código.
- El heap permite un ordenamiento natural a través de un árbol binario autobalanceado, donde al sacar el elemento raíz (el próximo en el orden de prioridad), reacomodar la colección es relativamente sencillo y eficiente.
- Para la `IncidentQueue` se utilizó **`deque`** ya que una lista simple es muy ineficiente: `list.pop(0)` es O(n) porque tiene que correr todos los elementos un lugar a la izquierda. `deque` permite sacar elementos desde la izquierda con `popleft()` en O(1), lo cual es extremadamente eficiente. Esto hace que la cola de incidentes pueda ser procesada rápidamente aun con grandes volúmenes de datos. Se le pueden dar distintos usos como pre-triage o cola de notificaciones: es una cola FIFO que sirve para acompañar a la `PriorityQueue`.

#### Complejidades

Las complejidades fueron explicadas en cada operación con docstrings, pero en resumen:

| Estructura              | Operación                              | Complejidad |
| ----------------------- | -------------------------------------- | ----------- |
| `PriorityQueue` (heap)  | `peek`                                 | O(1)        |
| `PriorityQueue` (heap)  | `add` / `pop`                          | O(log n)    |
| `PriorityQueue` (heap)  | `is_empty` / `size`                    | O(1)        |
| `IncidentQueue` (deque) | `add_incident` / `get_next_incident`   | O(1)        |
| `IncidentQueue` (deque) | `is_empty` / `size`                    | O(1)        |

Se priorizó eficiencia haciendo un análisis de la *Big-O notation*: O(1) para las lecturas rápidas (raíz del min-heap, ambos extremos del deque) y O(log n) para inserción/extracción en el heap.

### Ejercicio 3

**Algoritmos elegidos:** Bubble Sort (O(n²)) y Merge Sort (O(n log n)). Se eligió uno simple y uno eficiente para que la diferencia de comportamiento se note al crecer el tamaño de los datos.

**Búsquedas comparadas:** búsqueda secuencial (O(n)), búsqueda binaria propia (O(log n)) y `bisect` del módulo estándar.

**Baseline:** `sorted()` de Python (Timsort, implementado en C).

#### Resultados (medidos con `timeit` y `tracemalloc`)

##### Tiempo de ejecución (segundos)

|     n | binary_search | sequential_search | bisect_search | bubble_sort | merge_sort | sorted (Timsort) |
| ----: | ------------: | ----------------: | ------------: | ----------: | ---------: | ---------------: |
|   100 |      0.000017 |          0.000004 |      0.000014 |    0.000397 |   0.000138 |         0.000005 |
|   500 |      0.000068 |          0.000063 |      0.000053 |    0.047075 |   0.000901 |         0.000023 |
| 1.000 |      0.000120 |          0.000158 |      0.000115 |    0.358785 |   0.004042 |         0.000055 |

##### Memoria pico (MB)

|     n | binary_search | sequential_search | bisect_search | bubble_sort | merge_sort | sorted (Timsort) |
| ----: | ------------: | ----------------: | ------------: | ----------: | ---------: | ---------------: |
|   100 |      0.001032 |          0.000585 |      0.001160 |    0.000681 |   0.002032 |         0.001433 |
|   500 |      0.012336 |          0.000633 |      0.012336 |    0.000633 |   0.008536 |         0.008384 |
| 1.000 |      0.024320 |          0.000633 |      0.024320 |    0.000633 |   0.016456 |         0.016384 |

#### Análisis

Bubble Sort se dispara: su complejidad es cuadrática **O(n²)**, así que cuanto más grande es el arreglo, peor es la performance. Recorre la lista una y otra vez moviendo elementos constantemente, lo cual es extremadamente costoso. Pasar de 100 a 1.000 elementos lo hace ~900x más lento.

Merge Sort se degrada mucho menos rápido porque es **O(n log n)**: divide el arreglo en mitades sucesivamente y luego las une ordenadas. Es la opción razonable para arreglos grandes.

La desventaja de Merge Sort es la **memoria adicional** que requiere para hacer esas particiones (se ve en la tabla: ~16 MB pico contra los ~0 MB de Bubble Sort, que es *in-place*). Es el clásico **trade-off tiempo vs memoria**: Merge sacrifica memoria para ganar tiempo.

`sorted()` (Timsort de Python) le gana a ambos por amplio margen porque está implementado en C y combina Merge Sort con Insertion Sort, optimizado para datos del mundo real.

En cuanto a búsquedas: Sequential es la más simple (no requiere ordenar), pero crece linealmente. Binary y Bisect son mucho más rápidas en listas grandes, pero tienen un costo "oculto": **necesitan la lista ordenada**, y en estos benchmarks el `sorted()` previo se incluye en la medición — por eso aparecen con memoria alta. Esto plantea un trade-off práctico: si vamos a buscar **una sola vez**, conviene secuencial. Si vamos a buscar **muchas veces**, conviene ordenar una vez y usar binaria.

### Ejercicio 4

#### Análisis

Se optó por un `dict` (diccionario de Python) como índice. Implementar un hashmap a mano sería reinventar la rueda: Python ya lo trae implementado en C, con muy buena performance para búsquedas por clave (O(1) promedio).

Se utilizó `id` para indexar el diccionario ya que es un valor único, lo cual es vital para trabajar con diccionarios. En un trabajo real seguramente se utilizaría un UUID y no un id numerado linealmente como hacemos aquí, pero para fines didácticos sirve.

#### Sobre colisiones

Una **colisión** ocurre cuando dos claves *distintas* producen el mismo hash (o caen en el mismo bucket de la tabla después del módulo). No es lo mismo que insertar dos veces la misma clave: eso simplemente sobrescribe el valor.

Las dos estrategias clásicas para resolverlas son:

- **Encadenamiento (separate chaining)**: cada bucket guarda una lista de pares `(clave, valor)` que comparten ese slot. Al buscar, se recorre la lista del bucket comparando claves.
- **Direccionamiento abierto (open addressing)**: si el bucket está ocupado, se busca el siguiente disponible siguiendo alguna regla (linear probing, quadratic probing, etc.).

Python usa una variante de direccionamiento abierto en su implementación de `dict`, y redimensiona automáticamente la tabla cuando se llena para mantener la performance. Como usuario no me tengo que preocupar por la función hash ni por las colisiones: el lenguaje las resuelve transparentemente, y por eso elegí no implementar una tabla hash propia.

## Uso de herramientas de IA

Para este trabajo utilicé **Claude Code (Anthropic)** como herramienta de acompañamiento conceptual, en línea con lo permitido por la consigna del examen.

### En qué me ayudó la IA

- **Explicaciones conceptuales**: cómo funciona internamente un heap, por qué `deque` es más eficiente que `list` para una cola FIFO, qué es Big-O y cómo se mide, cómo funcionan los decoradores en Python (con paralelos a JavaScript), qué hace `functools.wraps`.
- **Detección de bugs y errores**: en cada iteración le mostré el código que escribía y me devolvía feedback indicando qué fallaba y por qué (por ejemplo: usar `@property.setter` en métodos comunes, comparar objetos sin `__lt__`, mezclar tipos en búsquedas binarias, falta de `random.shuffle` antes de medir un sort, etc.).
- **Sugerencias de organización**: opciones para estructurar carpetas y módulos, cuándo conviene un wrapper sobre `heapq`/`deque`, alternativas para acumular datos de benchmarks (closure vs variable de módulo).
- **Correcciones de redacción**: tildes, typos y reorganización de tablas en este README.

### Qué hice yo

- **Las decisiones de diseño**: estructura de carpetas, qué clase vive en cada módulo, qué responsabilidad tiene cada una, cómo se relacionan entre sí.
- **El código tipeado**: las clases del sistema (`Event`, `EventStore`, `Index`, `TextAnalyzer`, `Router`), los wrappers (`PriorityQueue`, `IncidentQueue`), los algoritmos del punto 3 (búsquedas y ordenamientos), el script de benchmark.
- **La justificación escrita**: lo que está en este README sobre por qué cada decisión (heap, deque, Bubble vs Merge, trade-offs) fue redactado por mí — la IA pulió forma y corrigió typos, pero los argumentos son míos.
- **El criterio para iterar**: cada feedback de la IA fue una sugerencia. Yo decidía qué aplicar, qué descartar y cómo aplicarlo.

### Aclaración explícita

**Esta declaración fue escrita por mí.** El contenido de este README, incluyendo esta misma sección, refleja mi propio criterio sobre el uso que hice de la herramienta. La IA cumplió un rol de **tutoría iterativa**, no de resolución automática del examen.
