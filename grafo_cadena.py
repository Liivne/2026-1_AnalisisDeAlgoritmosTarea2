import random


def grafo_cadena(n, semilla=42):
    """
    Grafo en forma de cadena con algunos atajos aleatorios.
    Cada nodo i tiene una arista a i+1, y algunos nodos tienen aristas adicionales a nodos aleatorios.
    Pesos enteros positivos en [1, 10].
    """
    random.seed(semilla)
    aristas = []
    # Cadena principal
    for u in range(n - 1):
        w = random.randint(1, 10)
        aristas.append((u, u + 1, w))
    # Atajos aleatorios
    for _ in range(n // 2):
        u = random.randint(0, n - 1)
        v = random.randint(0, n - 1)
        if u != v:
            w = random.randint(1, 10)
            aristas.append((u, v, w))
    return aristas