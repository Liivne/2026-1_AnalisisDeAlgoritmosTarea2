# Tarea 2 — Análisis de Algoritmos

Comparación experimental del **Algoritmo Base** (Bellman-Ford ejecutado desde cada nodo) y **Floyd-Warshall** para el problema All-Pairs Shortest Path en grafos dirigidos, más su ejecución sobre datasets reales de [networkrepository.com](https://networkrepository.com).

## Estructura del proyecto

```
src/
  grafos/grafo.py                  Estructura de grafo dirigido (matriz de adyacencia + lista de aristas), hecha desde cero
  algoritmos/algoritmo_base.py     Algoritmo Base: Bellman-Ford desde cada uno de los n nodos
  algoritmos/alg_floyd_warshall.py Floyd-Warshall vía programación dinámica, O(|V|^3)
experimentos/
  generador.py                     Generadores de los 4 tipos de instancias (denso, disperso, cadena, pesos negativos), con semilla fija
  runner.py                        Medición de tiempos: 32 repeticiones por medición, promedio + desviación estándar
  graficador.py                    Gráficos en escala lineal con barras de error y curvas teóricas ajustadas por mínimos cuadrados
  exportar_csv.py                  Sección 2.3: Floyd-Warshall sobre los datasets reales y exportación a CSV
datasets/                          bio-SC-TS.edges, power-685-bus.mtx y chebyshev2.mtx (networkrepository.com)
resultados/                        CSVs de métricas y distancias + gráficos .png generados
prueba.py                          Verificación de correctitud con instancias pequeñas hechas a mano
docs/informe.pdf                   Informe final
```

## Requisitos

- Python 3.10 o superior (probado con Python 3.13)
- Dependencias de `requirements.txt` (pandas, matplotlib, numpy — solo para medición y gráficos; los algoritmos y el grafo no usan ninguna librería externa)

Instalación (desde la raíz del proyecto):

```bash
python3 -m venv .venv
source .venv/bin/activate        # en Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Cómo ejecutar

Todos los comandos se corren **desde la raíz del proyecto**, con el entorno virtual activado.

**1. Verificación de correctitud** (instancias pequeñas hechas a mano, ambos algoritmos deben coincidir):

```bash
python prueba.py
```

**2. Experimentos de la sección 2.2** (4 tipos de instancias × 5 tamaños × 32 repeticiones; tarda algunos minutos):

```bash
python -m experimentos.runner
```

Genera `resultados/metricas_experimentos.csv` con promedio y desviación estándar de cada medición.

**3. Gráficos** (requiere haber corrido el runner antes):

```bash
python experimentos/graficador.py
```

Genera un `.png` por experimento en `resultados/graficos/`, comparando ambos algoritmos en escala lineal con sus curvas teóricas ajustadas superpuestas.

**4. Datasets reales de la sección 2.3** (bio-SC-TS, power-685-bus y chebyshev2; tarda varios minutos por el tamaño de chebyshev2):

```bash
python experimentos/exportar_csv.py
```

Corre Floyd-Warshall sobre los tres datasets, reporta el tiempo de ejecución y exporta `resultados/distancias_<dataset>.csv` con filas `{nodo1, nodo2, distancia_minima}` (un par por fila; `inf` para pares sin camino). bio-SC-TS y power-685-bus son no dirigidos, así que su CSV trae cada par una sola vez; chebyshev2 es dirigido (matriz MatrixMarket `general`) y su CSV trae todos los pares ordenados.

## Especificaciones de la máquina utilizada

Los tiempos reportados en el informe se midieron en:

- **CPU**: Intel Core i5-12450HX (12ª gen), 4 núcleos / 8 hilos disponibles
- **RAM**: 9,7 GiB disponibles para el entorno de ejecución
- **Sistema operativo**: Ubuntu 24.04 LTS sobre WSL2 (Windows, kernel 6.6.87.2-microsoft-standard-WSL2)
- **Python**: 3.13.13

Tiempos de referencia de la sección 2.3 en esta máquina: bio-SC-TS (636 nodos) en ~7 s, power-685-bus (685 nodos) en ~14 s y chebyshev2 (2053 nodos) en ~519 s (~8,7 min).

============================================================
Plan de Acción Paso a Paso:
1. Fase 1: Análisis Teórico y Diseño (Sección 1). Antes de tocar el código, resolver en papel las preguntas 1.1 y 1.2. Argumentar por qué a lo más $n$ llamadas a Bellman-Ford resuelven el problema. Luego, utilizar la propiedad de subestructura óptima para diseñar el algoritmo de Floyd-Warshall y demuestren que su tiempo es $O(|V|^{3})$. -> Luego pasarlo al informe. 
`Ignacio: en proceso⏲️`


2. Fase 2: Estructuras Base (Sección 2.1). Programar la representación del grafo (matriz de adyacencia y/o lista de adyacencia) desde cero, ya que no se pueden emplear librerías con subrutinas preprogramadas para grafos.  
`Mariel: listo✔️ -> cambios(Javier)✔️` 


3. Fase 3: Implementación de Algoritmos (Sección 2.1). Implementar el Algoritmo Base y el algoritmo de Floyd-Warshall. Crear instancias pequeñas hechas a mano para comprobar que ambos algoritmos arrojan exactamente los mismos resultados correctos.  
`Mariel: listo✔️ -> instancias extra(Martín)✔️`


4. Fase 4: Diseño y Ejecución de Experimentos (Sección 2.2). Programar un script que genere los cuatro tipos distintos de instancias requeridas, variando la estructura de los grafos o los pesos de las aristas. Configurar el script para que cada medición sea el promedio de al menos 32 ejecuciones y calcule la desviación estándar.  
`Javier: listo✔️ -> correcciones(Martín)✔️`


5. Fase 5: Procesamiento de Datasets Reales (Sección 2.3). Descargar los datasets de Network Repository según la opción que elijan. Ejecuten Floyd-Warshall sobre ellos y exporten los resultados en un archivo .csv.  
`Martín: listo✔️`


6. Fase 6: Análisis y Redacción (Sección 3). Generar los gráficos en escala lineal comparando ambos algoritmos y sus comportamientos teóricos ajustados. Responder las preguntas de discusión en el informe sobre las diferencias entre teoría y práctica, y las posibles optimizaciones.
`gráficos listos✔️ -> discusión: en proceso⏲️`


7. Fase 7: Empaquetado. Redactar el informe final asegurándose de documentar el código en él. Crear el archivo Readme detallando cómo ejecutar los códigos y las especificaciones de la máquina utilizada. 
`README listo✔️ -> informe: en proceso⏲️`
