import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.grafos.grafo import Grafo
import random

def generar_grafo_denso(num_nodos, semilla=42):
    """Genera un grafo donde casi todos los nodos están conectados."""
    # Semilla fija para que los experimentos sean reproducibles
    random.seed(semilla)
    g = Grafo(num_nodos)
    for i in range(num_nodos):
        for j in range(num_nodos):
            if i != j:
                # Agregamos aristas con un 90% de probabilidad para asegurar densidad
                if random.random() > 0.1: 
                    g.agregar_arista(i, j, random.uniform(1, 100))
    return g

def generar_grafo_cadena(num_nodos, semilla=42):
    """Genera un grafo lineal: 0 -> 1 -> 2 -> ... -> n"""
    random.seed(semilla)
    g = Grafo(num_nodos)
    for i in range(num_nodos - 1):
        g.agregar_arista(i, i+1, random.uniform(1, 10))
    return g

def generar_grafo_disperso(num_nodos, semilla=42):
    """Genera un grafo con muy pocas conexiones (ej. 5% de probabilidad por arista)."""
    random.seed(semilla)
    g = Grafo(num_nodos)
    for i in range(num_nodos):
        for j in range(num_nodos):
            if i != j:
                # Solo un 5% de probabilidad de que exista una arista
                if random.random() < 0.05: 
                    g.agregar_arista(i, j, random.uniform(1, 100))
    return g

def generar_grafo_negativo(num_nodos, semilla=42):
    """
    Genera un grafo con pesos negativos pero SIN ciclos negativos.

    Usamos la técnica de reponderación con potenciales (la misma idea del
    algoritmo de Johnson): a cada nodo le asignamos un potencial h(v) y cada
    arista (i, j) recibe peso = base + h(i) - h(j), con base > 0.
    En cualquier ciclo los potenciales se cancelan (h(i) - h(j) suma 0 al
    recorrer el ciclo completo), así que el peso de todo ciclo es la suma de
    sus pesos base, que es estrictamente positiva. Las aristas individuales
    sí pueden quedar negativas cuando h(j) supera a h(i) + base.
    """
    random.seed(semilla)
    g = Grafo(num_nodos)
    potenciales = [random.uniform(0, 60) for _ in range(num_nodos)]
    for i in range(num_nodos):
        for j in range(num_nodos):
            if i != j:
                # 20% de probabilidad de conexión
                if random.random() < 0.20:
                    peso = random.uniform(1, 20) + potenciales[i] - potenciales[j]
                    g.agregar_arista(i, j, peso)
    return g