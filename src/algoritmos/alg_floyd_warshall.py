# src/algoritmos/floyd_warshall.py

def floyd_warshall(grafo):
    """
    Función principal que recibe el objeto Grafo y ejecuta Floyd-Warshall
    para calcular la matriz de distancias mínimas.
    """
    # Extraemos la información del objeto
    n = grafo.n
    aristas = grafo.obtener_aristas()
    
    # Llamamos a tu lógica pura
    return alg_floyd_warshall(n, aristas)


def alg_floyd_warshall(n, aristas):
    """
    Lógica pura de Programación Dinámica para Floyd-Warshall en O(|V|^3).
    
    n: número de nodos
    aristas: lista de tuplas (u, v, peso) representando el grafo dirigido
    Retorna una matriz con la distancia mínima.
    """
    INF = float('inf') # Distancia infinita
    dist = [[INF] * n for _ in range(n)]

    # Distancia de cada nodo a sí mismo es 0
    for i in range(n):
        dist[i][i] = 0

    # Inicializamos las distancias directas usando la lista de aristas
    for u, v, w in aristas:
        # Si hay aristas paralelas, nos quedamos con la de menor peso
        if w < dist[u][v]:
            dist[u][v] = w

    # Probamos cada nodo k como intermediario
    for k in range(n):
        for i in range(n):
            for j in range(n): 
                # Solo sumamos si no estamos en el infinito
                if dist[i][k] != INF and dist[k][j] != INF:
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

    # Si dist[i][i] < 0 hay ciclo negativo
    for i in range(n):
        if dist[i][i] < 0:
            # Levantamos un error en lugar de imprimir para proteger los experimentos masivos
            raise ValueError(f"El grafo contiene un ciclo de peso negativo detectado en el nodo {i}")

    return dist