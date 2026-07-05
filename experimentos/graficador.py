import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Colores de la paleta Okabe-Ito (segura para daltonismo); la curva teórica
# comparte el color de su serie empírica y se distingue por la línea discontinua
COLOR_BASE = "#0072B2"  # azul
COLOR_FW = "#D55E00"    # bermellón


def calcular_curva_teorica(n_vals, tiempos, grado):
    """
    Ajusta una curva teórica c * n^grado a los datos empíricos por mínimos
    cuadrados usando TODOS los puntos: la constante que minimiza el error
    cuadrático es c = sum(t_i * n_i^g) / sum(n_i^(2g)).
    Retorna un rango suave de n y la curva evaluada sobre él.
    """
    n = n_vals.to_numpy(dtype=float)
    t = tiempos.to_numpy(dtype=float)
    potencias = n ** grado
    c = (t * potencias).sum() / (potencias ** 2).sum()
    n_suave = np.linspace(n.min(), n.max(), 200)
    return n_suave, c * n_suave ** grado

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
        
        # 1. Graficamos los datos empíricos con barras de error
        #    (la barra es la desviación estándar de las 32 repeticiones)
        plt.errorbar(n_vals, df_base['Tiempo_Promedio_s'], yerr=df_base['Desviacion_Estandar'],
                     marker='o', capsize=3, label='Empírico: Algoritmo Base', color=COLOR_BASE)
        plt.errorbar(n_vals, df_fw['Tiempo_Promedio_s'], yerr=df_fw['Desviacion_Estandar'],
                     marker='s', capsize=3, label='Empírico: Floyd-Warshall', color=COLOR_FW)

        # 2. Comportamientos teóricos ajustados por mínimos cuadrados
        # Floyd-Warshall es siempre O(V^3)
        n_suave, teorico_fw = calcular_curva_teorica(n_vals, df_fw['Tiempo_Promedio_s'], grado=3)
        plt.plot(n_suave, teorico_fw, linestyle='--', color=COLOR_FW, alpha=0.55, label='Teórico Ajustado: FW $O(n^3)$')

        # Bellman-Ford (Base) es n * O(V * E)
        # Para Cadena, E es aprox n, entonces n * n * n = O(n^3)
        # Para Denso, Disperso y Negativo, la probabilidad escala con n^2, entonces n * n * n^2 = O(n^4)
        grado_base = 3 if exp == "Cadena" else 4
        n_suave, teorico_base = calcular_curva_teorica(n_vals, df_base['Tiempo_Promedio_s'], grado=grado_base)
        plt.plot(n_suave, teorico_base, linestyle='--', color=COLOR_BASE, alpha=0.55, label=f'Teórico Ajustado: Base $O(n^{grado_base})$')
        
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