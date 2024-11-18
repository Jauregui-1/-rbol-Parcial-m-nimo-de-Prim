#RODRIGUEZ JAUREGUI JARED

import heapq  # Importa la librería heapq para trabajar con min-heaps (montículos mínimos)
import matplotlib.pyplot as plt  # Importa matplotlib para graficar los resultados
import networkx as nx  # Importa networkx para crear y manipular grafos

# Función que implementa el algoritmo de Prim para encontrar el árbol de expansión mínima (MST)
def prim(grafo, inicio):
    visitados = set()  # Conjunto para almacenar los nodos que ya han sido visitados
    # Inicia la cola de prioridad (min-heap), comenzando con el nodo de inicio con costo 0
    heap_minimo = [(0, inicio, None)]  # (costo, nodo, nodo_padre)
    costo_total = 0  # Variable para almacenar el costo total del MST
    arbol_expansion_minima = []  # Lista para almacenar las aristas del MST

    # Mientras haya elementos en el heap (es decir, nodos por procesar)
    while heap_minimo:
        # Extrae el nodo con el menor costo desde el heap
        costo, nodo, padre = heapq.heappop(heap_minimo)
        
        # Mostrar el estado de la cola de prioridad y el nodo actual
        print("\nCola de prioridad:", heap_minimo)
        print("Nodo seleccionado:", nodo, "con costo", costo)
        
        # Si el nodo no ha sido visitado previamente
        if nodo not in visitados:
            # Marca el nodo como visitado
            visitados.add(nodo)
            # Suma el costo del nodo al costo total
            costo_total += costo
            # Si el nodo tiene un nodo padre (no es el nodo inicial), agrega la arista al MST
            if padre is not None:
                arbol_expansion_minima.append((padre, nodo, costo))  # Agrega la arista (padre, nodo) con su peso
            
            # Mostrar el estado actual de los nodos visitados
            print("Nodos visitados:", visitados)
            
            # Itera sobre todos los vecinos del nodo actual
            for costo_siguiente, vecino in grafo[nodo]:
                # Si el vecino no ha sido visitado, lo agrega al heap para explorarlo
                if vecino not in visitados:
                    heapq.heappush(heap_minimo, (costo_siguiente, vecino, nodo))  # Agrega al heap
                    print("Se agrega la arista (", nodo, ",", vecino, ") con costo", costo_siguiente, "a la cola de prioridad")
        else:
            # Si el nodo ya ha sido visitado, se omite y no se agrega al heap
            print("El nodo", nodo, "ya ha sido visitado. Se omite.")
    
    # Devuelve el MST como una lista de aristas y el costo total del árbol
    return arbol_expansion_minima, costo_total

# Ejemplo de uso del algoritmo con un grafo con más nodos y aristas
grafo = {
    'A': [(1, 'B'), (4, 'C'), (7, 'E')],  # Nodo A tiene conexiones a B, C y E con costos 1, 4, 7
    'B': [(1, 'A'), (2, 'C'), (5, 'D')],  # Nodo B tiene conexiones a A, C y D con costos 1, 2, 5
    'C': [(4, 'A'), (2, 'B'), (3, 'D'), (6, 'E')],  # Nodo C tiene conexiones a A, B, D y E
    'D': [(5, 'B'), (3, 'C'), (8, 'E')],  # Nodo D tiene conexiones a B, C y E
    'E': [(7, 'A'), (6, 'C'), (8, 'D')]  # Nodo E tiene conexiones a A, C y D
}

# Llamada a la función prim con el grafo y el nodo de inicio 'A'
arbol_expansion_minima, costo_total = prim(grafo, 'A')

# Imprimir el árbol de expansión mínima y el costo total
print("\nÁrbol de Expansión Mínima:", arbol_expansion_minima)
print("Costo total:", costo_total)

# Crear un grafo para la visualización del grafo original usando NetworkX
grafo_original = nx.Graph()
# Añadir todas las aristas del grafo original al objeto grafo_original
for nodo in grafo:
    for vecino_costo in grafo[nodo]:
        grafo_original.add_edge(nodo, vecino_costo[1], weight=vecino_costo[0])  # (nodo, vecino, peso)

# Crear un grafo para la visualización del árbol de expansión mínima (MST)
grafo_mst = nx.Graph()
# Añadir todas las aristas del MST al grafo_mst
for u, v, peso in arbol_expansion_minima:
    grafo_mst.add_edge(u, v, weight=peso)  # (nodo_u, nodo_v, peso)

# Crear una ventana con subgráficos para mostrar ambos grafos
figura, ejes = plt.subplots(1, 2, figsize=(15, 8))  # Dos subgráficos (uno para el grafo original y otro para el MST)

# Visualizar el grafo original en el primer subgráfico
posicion_original = nx.spring_layout(grafo_original)  # Genera la disposición de los nodos de forma automática
nx.draw(grafo_original, posicion_original, with_labels=True, node_size=500, node_color='lightblue', font_size=10, font_weight='bold', ax=ejes[0])  # Dibuja el grafo original
etiquetas_original = nx.get_edge_attributes(grafo_original, 'weight')  # Obtiene los pesos de las aristas
nx.draw_networkx_edge_labels(grafo_original, posicion_original, edge_labels=etiquetas_original, ax=ejes[0])  # Dibuja las etiquetas de los pesos
ejes[0].set_title("Grafo Original")  # Título para el subgráfico del grafo original

# Visualizar el árbol de expansión mínima (MST) en el segundo subgráfico
posicion_mst = nx.spring_layout(grafo_mst)  # Genera la disposición de los nodos para el MST
nx.draw(grafo_mst, posicion_mst, with_labels=True, node_size=500, node_color='lightgreen', font_size=10, font_weight='bold', ax=ejes[1])  # Dibuja el MST
etiquetas_mst = nx.get_edge_attributes(grafo_mst, 'weight')  # Obtiene los pesos de las aristas en el MST
nx.draw_networkx_edge_labels(grafo_mst, posicion_mst, edge_labels=etiquetas_mst, ax=ejes[1])  # Dibuja las etiquetas de los pesos
ejes[1].set_title("Árbol de Expansión Mínima (MST)")  # Título para el subgráfico del MST

# Ajustar el diseño y mostrar la ventana con ambos grafos
plt.tight_layout()  # Ajusta el diseño para evitar solapamiento de elementos
plt.show()  # Muestra la ventana con ambos gráficos