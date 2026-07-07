import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.grafos.grafo import Grafo
from src.algoritmos.alg_floyd_warshall import floyd_warshall

import time
import csv

# Sección 2.3: ejecutar Floyd-Warshall sobre los datasets reales de
# networkrepository.com (bio-SC-TS, power-685-bus y chebyshev2), reportar el
# tiempo de ejecución y exportar las distancias mínimas a un .csv con filas
# {nodo1, nodo2, distancia_minima}.


def cargar_edges(ruta):
    """
    Carga un archivo .edges (lista de aristas "u v peso", nodos desde 0).
    bio-SC-TS es un grafo no dirigido con pesos positivos, así que agregamos
    cada arista en ambas direcciones.
    """
    aristas = []
    max_id = 0
    with open(ruta) as f:
        for linea in f:
            partes = linea.split()
            if not partes:
                continue
            u, v, w = int(partes[0]), int(partes[1]), float(partes[2])
            aristas.append((u, v, w))
            max_id = max(max_id, u, v)

    g = Grafo(max_id + 1)
    for u, v, w in aristas:
        g.agregar_arista(u, v, w)
        g.agregar_arista(v, u, w)
    return g


def cargar_mtx(ruta):
    """
    Carga un archivo MatrixMarket (.mtx), con nodos desde 1.
    Estas matrices no representan distancias con sus valores numéricos
    (power-685-bus es una matriz de admitancia y chebyshev2 una matriz de
    diferenciación espectral; ambas tienen valores negativos que crearían
    ciclos negativos), así que usamos solo la estructura del grafo con peso 1
    por arista, igual que como lo presenta networkrepository.

    El header dice si la matriz es 'symmetric' (guarda cada arista una vez y
    el grafo es no dirigido, caso power-685-bus) o 'general' (guarda cada
    entrada dirigida por separado, caso chebyshev2). Retorna (grafo, dirigido).
    """
    g = None
    with open(ruta) as f:
        # El header %%MatrixMarket trae: objeto formato tipo simetría
        dirigido = f.readline().split()[-1].lower() == 'general'
        for linea in f:
            if linea.startswith('%'):
                continue
            partes = linea.split()
            if g is None:
                # La primera línea sin comentario trae las dimensiones: filas columnas entradas
                g = Grafo(int(partes[0]))
                continue
            u, v = int(partes[0]) - 1, int(partes[1]) - 1
            # Ignoramos la diagonal (self-loops no aportan a las distancias)
            if u == v:
                continue
            g.agregar_arista(u, v, 1)
            if not dirigido:
                g.agregar_arista(v, u, 1)
    return g, dirigido


def procesar_dataset(nombre, grafo, dirigido=False):
    """Corre Floyd-Warshall midiendo el tiempo y exporta las distancias a CSV."""
    n = grafo.n
    print(f"\n--- Dataset {nombre}: {n} nodos, {len(grafo.obtener_aristas())} aristas dirigidas ---")

    inicio = time.perf_counter()
    dist = floyd_warshall(grafo)
    tiempo = time.perf_counter() - inicio
    print(f"  Floyd-Warshall terminó en {tiempo:.2f} segundos")

    os.makedirs("resultados", exist_ok=True)
    ruta_salida = f"resultados/distancias_{nombre}.csv"
    INF = float('inf')
    no_alcanzables = 0

    with open(ruta_salida, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["nodo1", "nodo2", "distancia_minima"])
        # En un grafo no dirigido las distancias son simétricas, así que basta
        # exportar cada par una sola vez (i < j); en uno dirigido d(i,j) puede
        # diferir de d(j,i) y exportamos todos los pares ordenados
        for i in range(n):
            for j in range(n) if dirigido else range(i + 1, n):
                if i == j:
                    continue
                if dist[i][j] == INF:
                    # Pares en componentes distintas: distancia infinita
                    writer.writerow([i, j, "inf"])
                    no_alcanzables += 1
                else:
                    writer.writerow([i, j, dist[i][j]])

    print(f"  Distancias exportadas a {ruta_salida}")
    if no_alcanzables:
        print(f"  Aviso: {no_alcanzables} pares sin camino (grafo no conexo), quedaron como 'inf'")
    return tiempo


if __name__ == "__main__":
    tiempos = {}

    g_bio = cargar_edges("datasets/bio-SC-TS.edges")
    tiempos["bio-SC-TS"] = procesar_dataset("bio-SC-TS", g_bio)

    g_power, dirigido = cargar_mtx("datasets/power-685-bus.mtx")
    tiempos["power-685-bus"] = procesar_dataset("power-685-bus", g_power, dirigido)

    g_cheb, dirigido = cargar_mtx("datasets/chebyshev2.mtx")
    tiempos["chebyshev2"] = procesar_dataset("chebyshev2", g_cheb, dirigido)

    print("\n=== Resumen de tiempos (para el informe) ===")
    for nombre, t in tiempos.items():
        print(f"  {nombre}: {t:.2f} s")
