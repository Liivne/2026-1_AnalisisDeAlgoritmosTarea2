import os
import time
import statistics
import pandas as pd
from src.algoritmos.algoritmo_base import algoritmo_base
from src.algoritmos.alg_floyd_warshall import floyd_warshall
from experimentos.generador import (
    generar_grafo_denso, 
    generar_grafo_disperso, 
    generar_grafo_cadena, 
    generar_grafo_negativo
)

# Configuración de los experimentos
REPETICIONES = 32
# Valores de n (cantidad de nodos). Mantenemos valores moderados porque Bellman-Ford iterado puede llegar a ser O(V^4) en grafos densos.
TAMAÑOS_N = [10, 20, 30, 40, 50] 

def medir_tiempos(algoritmo, grafo):
    """Ejecuta el algoritmo múltiples veces y retorna promedio y desviación."""
    tiempos = []
    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        # Si el grafo tuviera un ciclo negativo el algoritmo lanza ValueError y
        # abortamos la medición: silenciarlo dejaría tiempos que no corresponden
        # a una ejecución completa (Bellman-Ford aborta temprano y Floyd-Warshall
        # no), y esos datos no son comparables.
        algoritmo(grafo)
        fin = time.perf_counter()
        tiempos.append(fin - inicio)
        
    promedio = statistics.mean(tiempos)
    desv_est = statistics.stdev(tiempos) if len(tiempos) > 1 else 0.0
    return promedio, desv_est

def ejecutar_experimentos():
    resultados = []
    
    experimentos = {
        "Denso": generar_grafo_denso,
        "Disperso": generar_grafo_disperso,
        "Cadena": generar_grafo_cadena,
        "Negativo": generar_grafo_negativo
    }
    
    for nombre_exp, generador in experimentos.items():
        print(f"\n--- Iniciando Experimento: Grafo {nombre_exp} ---")
        
        for n in TAMAÑOS_N:
            print(f"  Midiendo para n={n}...")
            # Generamos el grafo en memoria una sola vez por cada tamaño
            grafo = generador(n)
            
            # Medimos Bellman-Ford (Algoritmo Base)
            prom_base, dev_base = medir_tiempos(algoritmo_base, grafo)
            
            # Medimos Floyd-Warshall
            prom_fw, dev_fw = medir_tiempos(floyd_warshall, grafo)
            
            # Guardamos la fila de resultados
            resultados.append({
                "Experimento": nombre_exp,
                "N": n,
                "Algoritmo": "Base (Bellman-Ford)",
                "Tiempo_Promedio_s": prom_base,
                "Desviacion_Estandar": dev_base
            })
            resultados.append({
                "Experimento": nombre_exp,
                "N": n,
                "Algoritmo": "Floyd-Warshall",
                "Tiempo_Promedio_s": prom_fw,
                "Desviacion_Estandar": dev_fw
            })

    # Usamos pandas para exportar todo a un CSV limpio
    df_resultados = pd.DataFrame(resultados)
    os.makedirs("resultados", exist_ok=True)
    ruta_salida = "resultados/metricas_experimentos.csv"
    df_resultados.to_csv(ruta_salida, index=False)
    print(f"\n Experimentos finalizados! Datos guardados en {ruta_salida}")

if __name__ == "__main__":
    ejecutar_experimentos()