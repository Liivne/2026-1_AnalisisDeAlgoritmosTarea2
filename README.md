# 2026-1_AnalisisDeAlgoritmosTarea2

== Tarea 2 - Análisis de Algoritmos ==

Archivos incluidos:
  alg_base.py       ----- Algoritmo Base (Bellman-Ford n veces)
  floyd_warshall.py ----- Algoritmo de Floyd-Warshall
  grafo.py          ----- Estructura unica para trabajar con los grafos 
  experimentos.py   ----- Medición de tiempos y generacion de gráficos
  runner.py         ----- Experimentos de 32 repeticiones (metricas_experimentos.cvs)
  generador.py      ----- Para generar los 4 tipos de grafos
  graficador.py     ----- Encargado de los graficos (resultados/graficos)
  ! informe.pdf     ----- Informe final
  git.ignore        -----
  README.md         ----- Fases y division del trabajo entre el grupo

Requisitos:
    python, 

============================================================
Plan de Acción Paso a Paso:
1. Fase 1: Análisis Teórico y Diseño (Sección 1). Antes de tocar el código, resolver en papel las preguntas 1.1 y 1.2. Argumentar por qué a lo más $n$ llamadas a Bellman-Ford resuelven el problema. Luego, utilizar la propiedad de subestructura óptima para diseñar el algoritmo de Floyd-Warshall y demuestren que su tiempo es $O(|V|^{3})$. -> Luego pasarlo al informe. 
`Ignacio: en proceso⏲️`


2. Fase 2: Estructuras Base (Sección 2.1). Programar la representación del grafo (matriz de adyacencia y/o lista de adyacencia) desde cero, ya que no se pueden emplear librerías con subrutinas preprogramadas para grafos.  
`Mariel: listo✔️ -> cambios(Javier)✔️` 


3. Fase 3: Implementación de Algoritmos (Sección 2.1). Implementar el Algoritmo Base y el algoritmo de Floyd-Warshall. Crear instancias pequeñas hechas a mano para comprobar que ambos algoritmos arrojan exactamente los mismos resultados correctos.  
`Mariel: listo✔️`


4. Fase 4: Diseño y Ejecución de Experimentos (Sección 2.2). Programar un script que genere los cuatro tipos distintos de instancias requeridas, variando la estructura de los grafos o los pesos de las aristas. Configurar el script para que cada medición sea el promedio de al menos 32 ejecuciones y calcule la desviación estándar.  
`Javier: listo✔️`


5. Fase 5: Procesamiento de Datasets Reales (Sección 2.3). Descargar los datasets de Network Repository según la opción que elijan. Ejecuten Floyd-Warshall sobre ellos y exporten los resultados en un archivo .csv.  
`: en proceso⏲️`


6. Fase 6: Análisis y Redacción (Sección 3). Generar los gráficos en escala lineal comparando ambos algoritmos y sus comportamientos teóricos ajustados. Responder las preguntas de discusión en el informe sobre las diferencias entre teoría y práctica, y las posibles optimizaciones.
`: en proceso⏲️`


7. Fase 7: Empaquetado. Redactar el informe final asegurándose de documentar el código en él. Crear el archivo Readme detallando cómo ejecutar los códigos y las especificaciones de la máquina utilizada. 
`: en proceso⏲️`