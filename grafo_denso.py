import random

def grafo_denso(n, semilla=42):
    """
    Grafo casi completo: cada par (u,v) tiene arista con probabilidad 0.9.
    Pesos enteros positivos en [1, 100].
    """
    random.seed(semilla)
    aristas = []
    for u in range(n):
        for v in range(n):
            if u != v and random.random() < 0.9:
                w = random.randint(1, 100)
                aristas.append((u, v, w))
    return aristas