from src.grafos.grafo import Grafo
from src.algoritmos.algoritmo_base import algoritmo_base
from src.algoritmos.alg_floyd_warshall import floyd_warshall

def test_grafo_normal():
    print("--- TEST 1: Grafo con pesos negativos (Sin ciclos) ---")
    g = Grafo(4)
    
    # Topología:
    # 0 -> 1 (peso 3) | 0 -> 2 (peso 8) | 1 -> 3 (peso 1)
    # 2 -> 1 (peso -2) 
    # 3 -> 2 (peso 2)
    g.agregar_arista(0, 1, 3)
    g.agregar_arista(0, 2, 8)
    g.agregar_arista(1, 3, 1)
    g.agregar_arista(2, 1, -2)
    g.agregar_arista(3, 2, 2)
    
    resultado_base = algoritmo_base(g)
    resultado_fw = floyd_warshall(g)
    
    assert resultado_base == resultado_fw, " Error: los algoritmos dan matrices distintas"
    print(" Exito: los algoritmos calcularon exactamente las mismas distancias\n")


def test_matriz_conocida():
    print("--- TEST 2: Grafo de 5 nodos con matriz de distancias calculada a mano ---")
    g = Grafo(5)

    # Topología:
    # 0 -> 1 (peso 2) | 1 -> 2 (peso 3) | 2 -> 0 (peso 4)
    # 0 -> 3 (peso 7) | 3 -> 4 (peso 1) | 2 -> 4 (peso 5)
    # El nodo 4 no tiene aristas de salida y el 3 solo llega al 4,
    # así que varios pares quedan sin camino (distancia infinita).
    g.agregar_arista(0, 1, 2)
    g.agregar_arista(1, 2, 3)
    g.agregar_arista(2, 0, 4)
    g.agregar_arista(0, 3, 7)
    g.agregar_arista(3, 4, 1)
    g.agregar_arista(2, 4, 5)

    # Matriz de distancias mínimas verificada a mano
    # (ej: d(0,4) = 0->3->4 = 7+1 = 8, mejor que 0->1->2->4 = 2+3+5 = 10)
    INF = float('inf')
    esperada = [
        [0,   2,   5,   7,   8],
        [7,   0,   3,   14,  8],
        [4,   6,   0,   11,  5],
        [INF, INF, INF, 0,   1],
        [INF, INF, INF, INF, 0],
    ]

    resultado_base = algoritmo_base(g)
    resultado_fw = floyd_warshall(g)

    assert resultado_base == esperada, " Error: el Algoritmo Base no coincide con la matriz calculada a mano"
    assert resultado_fw == esperada, " Error: Floyd-Warshall no coincide con la matriz calculada a mano"
    print(" Exito: ambos algoritmos reproducen la matriz calculada a mano (incluye pares inalcanzables)\n")


def test_camino_indirecto():
    print("--- TEST 3: El camino con más aristas gana a la arista directa ---")
    g = Grafo(3)

    # La arista directa 0 -> 1 pesa 10, pero el camino 0 -> 2 -> 1 pesa solo 3
    g.agregar_arista(0, 1, 10)
    g.agregar_arista(0, 2, 1)
    g.agregar_arista(2, 1, 2)

    resultado_base = algoritmo_base(g)
    resultado_fw = floyd_warshall(g)

    assert resultado_base == resultado_fw, " Error: los algoritmos dan matrices distintas"
    assert resultado_base[0][1] == 3, f" Error: d(0,1) debería ser 3 (vía el nodo 2), se obtuvo {resultado_base[0][1]}"
    print(" Exito: ambos algoritmos prefieren el camino indirecto más barato\n")


def test_ciclo_negativo():
    print("--- TEST 4: Grafo CON ciclo negativo ---")
    g_ciclo = Grafo(3)
    
    # Creamos un ciclo evidente: 0 -> 1 -> 2 -> 0 cuya suma es -1
    g_ciclo.agregar_arista(0, 1, 1)
    g_ciclo.agregar_arista(1, 2, -1)
    g_ciclo.agregar_arista(2, 0, -1)
    
    # Verificamos que el Algoritmo Base levante el error
    base_detecto = False
    try:
        algoritmo_base(g_ciclo)
    except ValueError as e:
        print(f" Algoritmo Base detectó el problema: {e}")
        base_detecto = True

    # Verificamos que Floyd-Warshall levante el error
    fw_detecto = False
    try:
        floyd_warshall(g_ciclo)
    except ValueError as e:
        print(f" Floyd-Warshall detectó el problema: {e}")
        fw_detecto = True
        
    assert base_detecto and fw_detecto, " Error: algún algoritmo falló en detectar el ciclo negativo"


if __name__ == "__main__":
    print("Iniciando validación de algoritmos...\n")
    test_grafo_normal()
    test_matriz_conocida()
    test_camino_indirecto()
    test_ciclo_negativo()
    print("\nTodas las pruebas pasaron correctamente!")