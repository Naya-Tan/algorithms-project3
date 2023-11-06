import networkx as nx
import matplotlib.pyplot as plt

# 1
print("Problem 1")

G1 = nx.Graph()
main_edges = [
    ('A', 'B'), ('A', 'E'), ('B', 'C'), ('B', 'F'), ('C', 'D'), ('C', 'G'), 
    ('D', 'H'), ('E', 'F'), ('E', 'I'), ('F', 'G'), ('F', 'J'), ('G', 'H'), 
    ('I', 'J'), ('I', 'M'), ('J', 'N'), ('M', 'N')
]

unconnected_edges = [
    ('K', 'L'), ('L', 'O'), ('O', 'P')
]

# add all edges to the graph
G1.add_edges_from(main_edges)
G1.add_edges_from(unconnected_edges)

# part a 
def find_all_connected_components(graph):
    return list(nx.connected_components(graph))

connected_components = find_all_connected_components(G1)
print('\nPart A')
print('Connected Components:', connected_components)

# part b 
def check_path(graph, start, end):
    bfs_path_exists = nx.has_path(graph, start, end)
    # check path using DFS manually
    dfs_path_exists = False
    for path in nx.dfs_edges(graph, start):
        if end in path:
            dfs_path_exists = True
            break
    
    return bfs_path_exists, dfs_path_exists

# example check between 'A' and 'M'
bfs_path, dfs_path = check_path(G1, 'A', 'M')
print('\nPart B')
print(f"Path exists between 'A' and 'M': BFS: {bfs_path}, DFS: {dfs_path}")


#part c 
def compare_paths(graph, start, end):
    # find path using BFS
    bfs_path = nx.shortest_path(graph, start, end)
    # find path using DFS
    dfs_paths = list(nx.all_simple_paths(graph, start, end))
    # grab the first path 
    dfs_path = dfs_paths[0] if dfs_paths else None
    
    return bfs_path, dfs_path

# compare the paths 
bfs_path, dfs_path = compare_paths(G1, 'A', 'M')
print('\nPart C')
print(f"BFS path between 'A' and 'M': {bfs_path}")
print(f"DFS path (one of the possible paths) between 'A' and 'M': {dfs_path}")
print('\n')





#2
print("Problem 2 \n")
edges = [(1, 3), (3, 2), (4, 1), (2, 1), (4, 2), 
         (3, 5), (5, 6), (5, 8), (6, 8), (6, 7),
         (6, 10), (8, 10), (10, 9), (10, 11), (8, 9),
         (9, 5), (7, 10), (9, 11), (11, 12), (4, 12)]

G = nx.DiGraph()
G.add_edges_from(edges)

#Part A
#Find strongly connected components of the digraph
scc = list(nx.strongly_connected_components(G))

print("Part A \nStrongly Connected Components:")
for i in scc:
    print(i)

#Part B
#Draw the meta graph
meta_graph = nx.condensation(G)
pos = nx.spring_layout(meta_graph)
nx.draw(meta_graph, pos, with_labels = True, node_size = 1000, node_color = 'skyblue')
plt.title("Meta Graph of Strongly Connected Components")
plt.show()

#Part C
#Linearize it in topological order
#topological = list(nx.topological_sort(meta_graph))

print("Topological Order:")
#print(topological)
print(list(reversed(list(nx.topological_sort(meta_graph)))))
nx.draw_kamada_kawai(G, with_labels = True)
plt.show()


#3
print("\nProblem 3")

