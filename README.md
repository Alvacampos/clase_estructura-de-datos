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