import random


def grafo_pesos_negativos(n, semilla=42):
    """
    Grafo denso con pesos negativos y positivos.
    El 10% de las aristas tienen peso en [-50, -1], el resto en [1, 100].
    Se evitan ciclos negativos usando solo pesos negativos en aristas aisladas.
    """
    random.seed(semilla)
    aristas = []
    for u in range(n):
        for v in range(n):
            if u != v and random.random() < 0.7:
                if random.random() < 0.1:
                    w = random.randint(-50, -1)
                else:
                    w = random.randint(1, 100)
                aristas.append((u, v, w))
    return aristas