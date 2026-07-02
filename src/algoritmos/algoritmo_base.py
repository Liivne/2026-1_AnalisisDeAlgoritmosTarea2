# src/algoritmos/base.py

def algoritmo_base(grafo):
    """
    Función principal que recibe el objeto Grafo y ejecuta Bellman-Ford 
    para calcular la distancia mínima entre todo par de nodos.
    """
    # Extraemos la información necesaria del objeto Grafo
    n = grafo.n
    aristas = grafo.obtener_aristas()
    
    # Llamamos a la lógica algorítmica pura
    return alg_base(n, aristas)


def alg_base(n, aristas):
    """
    Lógica pura del algoritmo de Bellman-Ford ejecutado n veces.
    
    n: número de nodos
    aristas: lista de tuplas (u, v, peso) representando el grafo dirigido
    Retorna una matriz NxN con las distancias mínimas.
    """
    INF = float('inf') # Distancia infinita
    dist = [[INF] * n for _ in range(n)]

    # Ejecutamos Bellman-Ford tomando cada nodo 's' como origen
    for s in range(n):
        dist[s][s] = 0

        # Repetir n-1 veces para relajar todas las aristas
        for _ in range(n - 1):
            for u, v, w in aristas:
                # Relajar la arista (u, v) con peso w
                if dist[s][u] != INF and dist[s][u] + w < dist[s][v]:
                    dist[s][v] = dist[s][u] + w

        # Verificación de ciclos negativos:
        # Si todavía se puede relajar alguna arista, el problema no tiene solución óptima finita
        for u, v, w in aristas:
            if dist[s][u] != INF and dist[s][u] + w < dist[s][v]:
                raise ValueError(f"Se detectó un ciclo negativo accesible desde el nodo {s}")

    return dist