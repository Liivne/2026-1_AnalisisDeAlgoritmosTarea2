def alg_base(n, aristas):
    """
    n: número de nodos
    aristas: lista de tuplas (u, v, peso) representando el grafo dirigido
    Retorna una matriz con las distancias minimas.
    """
    INF = float('inf') #distancia infinita
    dist = [[INF] * n for _ in range(n)]

    for s in range(n):
        dist[s][s] = 0

        # repetir n-1 para relajar todas las artistas
        for i in range(n - 1):
            for u, v, w in aristas:
                # Relajar la arista (u, v) con peso w
                if dist[s][u] != INF and dist[s][u] + w < dist[s][v]:
                    dist[s][v] = dist[s][u] + w

        # si todavia se puede relajar alguna arista, entonces hay un ciclo negativo
        for u, v, w in aristas:
            if dist[s][u] != INF and dist[s][u] + w < dist[s][v]:
                print("Hay un ciclo negativo en el grafo")

    return dist
