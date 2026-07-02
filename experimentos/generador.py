import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.grafos.grafo import Grafo
import random

def generar_grafo_denso(num_nodos):
    """Genera un grafo donde casi todos los nodos están conectados."""
    g = Grafo(num_nodos)
    for i in range(num_nodos):
        for j in range(num_nodos):
            if i != j:
                # Agregamos aristas con un 90% de probabilidad para asegurar densidad
                if random.random() > 0.1: 
                    g.agregar_arista(i, j, random.uniform(1, 100))
    return g

def generar_grafo_cadena(num_nodos):
    """Genera un grafo lineal: 0 -> 1 -> 2 -> ... -> n"""
    g = Grafo(num_nodos)
    for i in range(num_nodos - 1):
        g.agregar_arista(i, i+1, random.uniform(1, 10))
    return g

def generar_grafo_disperso(num_nodos):
    """Genera un grafo con muy pocas conexiones (ej. 5% de probabilidad por arista)."""
    g = Grafo(num_nodos)
    for i in range(num_nodos):
        for j in range(num_nodos):
            if i != j:
                # Solo un 5% de probabilidad de que exista una arista
                if random.random() < 0.05: 
                    g.agregar_arista(i, j, random.uniform(1, 100))
    return g

def generar_grafo_negativo(num_nodos):
    """Genera un grafo que incluye pesos negativos aleatorios."""
    g = Grafo(num_nodos)
    for i in range(num_nodos):
        for j in range(num_nodos):
            if i != j:
                # 20% de probabilidad de conexión
                if random.random() < 0.20: 
                    # Generamos pesos entre -20 y 100 (algunos serán negativos)
                    peso = random.uniform(-20, 100)
                    g.agregar_arista(i, j, peso)
    return g