class Grafo:
    def __init__(self, num_nodos):
        self.n = num_nodos
        # Inicializamos la matriz con infinito (representa que no hay conexión directa)
        self.matriz = [[float('inf')] * num_nodos for _ in range(num_nodos)]
        
        # La distancia de un nodo a sí mismo es 0
        for i in range(num_nodos):
            self.matriz[i][i] = 0.0
            
        # Mantenemos también una lista de aristas (útil para Bellman-Ford)
        self.aristas = [] 

    def agregar_arista(self, u, v, peso):
        """Agrega una arista dirigida del nodo u al nodo v con su peso."""
        self.matriz[u][v] = peso
        self.aristas.append((u, v, peso))

    def obtener_matriz(self):
        return self.matriz
        
    def obtener_aristas(self):
        return self.aristas
    
    #cambié la estructura anterior: trabajar solo con un tipo de grafo dirigido, luego lo que cambie es como se construirán las aristas -> esto verlo en el "generador de experimentos(experimentos/generador.py)"