import networkx as nx
import matplotlib.pyplot as plt

# Création du graphe original
G = nx.Graph()
edges = [(1, 2), (1, 4), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (6, 3)]
G.add_edges_from(edges)

# Positionnement des sommets pour une visualisation claire
pos = nx.spring_layout(G)

# Affichage du graphe original
plt.figure(figsize=(14, 7))

plt.subplot(121)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=15, edge_color='gray')
plt.title("Graphe Original")

# Création de la 3-bipartition correcte
# Dans la 3-bipartition correcte, il ne doit pas y avoir d'arêtes entre les sommets du même ensemble
V1 = [1, 4]
V2 = [2, 5]
V3 = [3, 6]

# Création d'un nouveau graphe pour la 3-bipartition
H = nx.Graph()

# Ajout des sommets et des arêtes en respectant la 3-bipartition
for u, v in edges:
    if (u in V1 and v not in V1) or (u in V2 and v not in V2) or (u in V3 and v not in V3):
        H.add_edge(u, v)

# Coloration des sommets en fonction de leur partition
color_map = []
for node in H:
    if node in V1:
        color_map.append('red')
    elif node in V2:
        color_map.append('blue')
    elif node in V3:
        color_map.append('green')

# Affichage du graphe avec la 3-bipartition correcte
plt.subplot(122)
nx.draw(H, pos, with_labels=True, node_color=color_map, node_size=500, font_size=15, edge_color='gray')
plt.title("Graphe avec 3-Bipartition Correcte")

# Affichage des graphes
plt.show()
