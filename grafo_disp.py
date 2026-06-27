import random

def grafo_disperso(n, semilla=42):
    """
    Grafo disperso: cada nodo tiene aprox sqrt(n) vecinos.
    Pesos en [1, 100].
    """
    random.seed(semilla)
    aristas = []
    grado = max(1, int(n ** 0.5))

    for u in range(n):
        # candidatos: todos los nodos menos u mismo
        candidatos = [v for v in range(n) if v != u]
        vecinos = random.sample(candidatos, min(grado, len(candidatos)))
        for v in vecinos:
            w = random.randint(1, 100)
            aristas.append((u, v, w))

    return aristas