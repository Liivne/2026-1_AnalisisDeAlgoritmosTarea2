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


def test_ciclo_negativo():
    print("--- TEST 2: Grafo CON ciclo negativo ---")
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
    test_ciclo_negativo()
    print("\nTodas las pruebas pasaron correctamente!")