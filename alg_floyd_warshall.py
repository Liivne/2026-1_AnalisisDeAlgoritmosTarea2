def floyd_warshall(n, aristas):
    """
    n: número de nodos
    aristas: lista de tuplas (u, v, peso) representando el grafo dirigido
    Retorna una matriz con la distancia min.
    """
    INF = float('inf') #distancia infinita
    dist = [[INF] * n for _ in range(n)]

    # distancia de cada nodo a si mismo si es 0
    for i in range(n):
        dist[i][i] = 0

    for u, v, w in aristas:
        # Si hay aristas paralelas, nos quedamos con la de menor peso
        if w < dist[u][v]:
            dist[u][v] = w

    #probamos cada nodo k como intermediario
    for k in range(n):
        for i in range(n):
            for j in range(n): 
                if dist[i][k] != INF and dist[k][j] != INF:
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

    #si dist[i][i] < 0 hay ciclo negativo
    for i in range(n):
        if dist[i][i] < 0:
            print("El grafo contiene un ciclo de peso negativo")

    return dist