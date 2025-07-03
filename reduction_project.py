import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(graph, title):
    pos = nx.spring_layout(graph)
    plt.figure(figsize=(8, 6))
    nx.draw(graph, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=16, font_color="black", font_weight="bold", edge_color="gray")
    plt.title(title)
    plt.show()

def reduce_graph(graph, k):
    if k > len(graph.edges()):
        print(f"Cannot perform {k} reductions, as the graph has only {len(graph.edges())} edges.")
        return graph
    
    reduced_graph = graph.copy()
    edges_to_contract = list(reduced_graph.edges())[:k]
    
    for u, v in edges_to_contract:
        reduced_graph = nx.contracted_nodes(reduced_graph, u, v, self_loops=False)
        
    return reduced_graph

def main():
    # Crée un graphe initial
    G = nx.Graph()
    edges = [("A", "B"), ("B", "C"), ("C", "D"), ("D", "E"), ("A", "E")]
    G.add_edges_from(edges)
    
    # Dessine le graphe initial
    draw_graph(G, "Graphe initial")
    
    # Demande à l'utilisateur le nombre de réductions à appliquer
    k = int(input("Entrez le nombre de réductions à appliquer: "))
    
    # Applique les réductions
    G_reduced = reduce_graph(G, k)
    
    # Dessine le graphe réduit
    draw_graph(G_reduced, f"Graphe après {k} réduction(s)")
    
if __name__ == "__main__":
    main()
