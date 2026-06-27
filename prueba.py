from alg_floyd_warshall import floyd_warshall
from algoritmo_base import alg_base

#probar algotirmo base y de floyd warshall
n = 4
aristas = [(0, 1, 5), (0, 3, 10), (1, 2, 3), (2, 3, 1)]

distancia_base = alg_base(n, aristas)
distancia_floyd = floyd_warshall(n, aristas)

print("Distancias por el algoritmo base:")
for row in distancia_base:
    print(row)

print("\nDistancias por el algoritmo de Floyd-Warshall:")
for row in distancia_floyd:
    print(row)

