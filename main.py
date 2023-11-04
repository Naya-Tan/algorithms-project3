import networkx as nx
import matplotlib.pyplot as plt

# 1
G1 = nx.Graph()

edges = [
    ('A', 'B'), ('A', 'E'), ('B', 'C'), ('B', 'F'), ('C', 'D'), ('C', 'G'),
    ('D', 'H'), ('E', 'F'), ('E', 'I'), ('F', 'G'), ('F', 'J'), ('G', 'H'),
    ('G', 'K'), ('H', 'L'), ('I', 'J'), ('I', 'M'), ('J', 'N'), ('K', 'L'),
    ('K', 'O'), ('L', 'P'), ('M', 'N'), ('N', 'O')
]

G1.add_edges_from(edges)

# part a 
def find_all_connected_components(graph):
    # This will return a list of sets, each set is a connected component
    return list(nx.connected_components(graph))

connected_components = find_all_connected_components(G1)
print('Part A\n')
print('Connected Components:', connected_components)

# part b 
def check_path(graph, start, end):
    # Check path using BFS
    bfs_path_exists = nx.has_path(graph, start, end, method='bfs')
    # Check path using DFS
    dfs_path_exists = nx.has_path(graph, start, end, method='dfs')
    
    return bfs_path_exists, dfs_path_exists

# Example check between 'A' and 'M'
bfs_path, dfs_path = check_path(G1, 'A', 'M')
print('Part B\n')
print(f"Path exists between 'A' and 'M': BFS: {bfs_path}, DFS: {dfs_path}")


#part c 
def compare_paths(graph, start, end):
    # Find path using BFS
    bfs_path = nx.shortest_path(graph, start, end, method='bfs')
    # Find path using DFS
    dfs_path = nx.shortest_path(graph, start, end, method='dfs')
    
    return bfs_path, dfs_path

# Example path comparison between 'A' and 'M'
bfs_path, dfs_path = compare_paths(G1, 'A', 'M')
print('Part \n')
print(f"BFS path between 'A' and 'M': {bfs_path}")
print(f"DFS path between 'A' and 'M': {dfs_path}")





#2
edges = [(1, 3), (3, 2), (4, 1), (2, 1), (4, 2), 
         (3, 5), (5, 6), (5, 8), (6, 8), (6, 7),
         (6, 10), (8, 10), (10, 9), (10, 11), (8, 9),
         (9, 5), (7, 10), (9, 11), (11, 12), (4, 12)]

print(len(edges))

G = nx.DiGraph()
G.add_edges_from(edges)

scc = list(nx.strongly_connected_components(G))

print("Strongly Connected Components:")
for i in scc:
    print(i)

meta_graph = nx.condensation(G)
pos = nx.spring_layout(meta_graph)
nx.draw(meta_graph, pos, with_labels = True, node_size = 1000, node_color = 'skyblue')
plt.title("Meta Graph of Strongly Connected Components")
plt.show()

topological = list(nx.topological_sort(meta_graph))

print("Topological Order:")
print(topological)
nx.draw_kamada_kawai(G, with_labels = True)
plt.show()




#3