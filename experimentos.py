import time
import math
import csv

from algoritmo_base import alg_base
from alg_floyd_warshall import floyd_warshall
from grafo_denso import grafo_denso
from grafo_disp import grafo_disperso
from grafo_neg import grafo_pesos_negativos
from grafo_cadena import grafo_cadena


REPETICIONES = 32

def medir(algoritmo, n, aristas):
    tiempos = []
    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        algoritmo(n, aristas)
        fin = time.perf_counter()
        tiempos.append(fin - inicio)

    promedio = sum(tiempos) / REPETICIONES
    varianza = sum((t - promedio) ** 2 for t in tiempos) / REPETICIONES
    std = math.sqrt(varianza)
    return promedio, std


def correr_experimento(nombre, generador, tamanios):
    filas = []

    for n in tamanios:
        aristas = generador(n)

        prom_b, std_b = medir(alg_base, n, aristas)
        prom_fw, std_fw = medir(floyd_warshall, n, aristas)

        print(f"  n={n} algoritmo base: {prom_b:.4f}s, algoritmo Floyd-Warshall: {prom_fw:.4f}s")

        filas.append({
            "experimento": nombre,
            "n": n,
            "aristas": len(aristas),
            "base_prom": prom_b,
            "base_std": std_b,
            "fw_prom": prom_fw,
            "fw_std": std_fw,
        })

    return filas


# tamaños de n para cada experimento, se puede cambiar para mas o menos rep
ns_denso    = [10, 20, 30, 40, 50, 60, 70, 80]
ns_disperso = [20, 50, 100, 150, 200, 250, 300]
ns_negativo = [10, 20, 30, 40, 50, 60, 70]
ns_cadena   = [50, 100, 200, 300, 400, 500]

# definimos los experimentos a correr, cada uno con su generador y tamaños de n
experimentos = [
    ("Grafo Denso",           grafo_denso,           ns_denso),
    ("Grafo Disperso",        grafo_disperso,        ns_disperso),
    ("Pesos Negativos",       grafo_pesos_negativos, ns_negativo),
    ("Grafo Cadena", grafo_cadena,          ns_cadena),
]

# corremos todos y juntamos todo en una lista
todos = []
for nombre, generador, tamanios in experimentos:
    filas = correr_experimento(nombre, generador, tamanios)
    todos.extend(filas)

# guardamos todo en un solo csv
with open("resultados.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=todos[0].keys())
    writer.writeheader()
    writer.writerows(todos)
