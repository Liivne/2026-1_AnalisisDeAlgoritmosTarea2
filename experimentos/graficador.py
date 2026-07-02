import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

def calcular_curva_teorica(n_vals, tiempos, grado):
    """
    Ajusta una curva teórica O(n^grado) al último punto de los datos empíricos.
    Calcula la constante 'c' tal que c * (n_max^grado) = tiempo_max
    """
    n_max = n_vals.iloc[-1]
    tiempo_max = tiempos.iloc[-1]
    c = tiempo_max / (n_max ** grado)
    return c * (n_vals ** grado)

def generar_graficos():
    # Aseguramos que la carpeta exista
    os.makedirs("resultados/graficos", exist_ok=True)
    
    # Cargamos los datos del CSV generado por runner.py
    ruta_csv = "resultados/metricas_experimentos.csv"
    if not os.path.exists(ruta_csv):
        print(f"Error: No se encontró el archivo {ruta_csv}")
        return
        
    df = pd.read_csv(ruta_csv)
    experimentos = df['Experimento'].unique()
    
    for exp in experimentos:
        plt.figure(figsize=(10, 6))
        
        # Filtramos los datos del experimento actual
        df_exp = df[df['Experimento'] == exp]
        df_base = df_exp[df_exp['Algoritmo'] == 'Base (Bellman-Ford)']
        df_fw = df_exp[df_exp['Algoritmo'] == 'Floyd-Warshall']
        
        n_vals = df_base['N']
        
        # 1. Graficamos los datos empíricos
        plt.plot(n_vals, df_base['Tiempo_Promedio_s'], marker='o', label='Empírico: Algoritmo Base', color='blue')
        plt.plot(n_vals, df_fw['Tiempo_Promedio_s'], marker='s', label='Empírico: Floyd-Warshall', color='red')
        
        # 2. Comportamientos teóricos ajustados
        # Floyd-Warshall es siempre O(V^3)
        teorico_fw = calcular_curva_teorica(n_vals, df_fw['Tiempo_Promedio_s'], grado=3)
        plt.plot(n_vals, teorico_fw, linestyle='--', color='darkred', alpha=0.5, label='Teórico Ajustado: FW $O(n^3)$')
        
        # Bellman-Ford (Base) es n * O(V * E)
        # Para Cadena, E es aprox n, entonces n * n * n = O(n^3)
        # Para Denso, Disperso y Negativo, la probabilidad escala con n^2, entonces n * n * n^2 = O(n^4)
        grado_base = 3 if exp == "Cadena" else 4
        teorico_base = calcular_curva_teorica(n_vals, df_base['Tiempo_Promedio_s'], grado=grado_base)
        plt.plot(n_vals, teorico_base, linestyle='--', color='darkblue', alpha=0.5, label=f'Teórico Ajustado: Base $O(n^{grado_base})$')
        
        # 3. Configuraciones visuales en escala lineal
        plt.title(f'Tiempos de Ejecución: Experimento Grafo {exp}')
        plt.xlabel('Número de Nodos (N)')
        plt.ylabel('Tiempo Promedio (Segundos)')
        plt.grid(True, linestyle=':', alpha=0.7)
        plt.legend()
        
        # Guardamos el gráfico
        ruta_salida = f"resultados/graficos/grafico_{exp.lower()}.png"
        plt.savefig(ruta_salida, dpi=300)
        plt.close()
        print(f" Gráfico guardado: {ruta_salida}")

if __name__ == "__main__":
    generar_graficos()