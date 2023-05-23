import sys


def prim(graph):
    # Select the starting node as the first node in the graph
    start_node = list(graph.keys())[0]

    # Initialize the minimum spanning tree and visited nodes
    mst = []
    visited = set()

    while len(visited) < len(graph):
        # Find the minimum weight edge from visited to unvisited nodes
        min_edge = None
        min_weight = sys.maxsize

        for node in visited:
            for neighbor, weight in graph[node]:
                if neighbor not in visited and weight < min_weight:
                    min_edge = (node, neighbor)
                    min_weight = weight

        if min_edge is None:
            break

        # Add the minimum weight edge to the minimum spanning tree
        mst.append(min_edge)
        visited.add(min_edge[1])

    return mst


# Get user input for the graph
graph = {}
num_nodes = int(input("Enter the number of nodes in the graph: "))

for _ in range(num_nodes):
    node = input("Enter the name of the node: ")
    neighbors = []

    num_neighbors = int(input("Enter the number of neighbors for node {}: ".format(node)))
    for _ in range(num_neighbors):
        neighbor, weight = input("Enter the name of the neighbor and its weight (separated by space): ").split()
        neighbors.append((neighbor, int(weight)))

    graph[node] = neighbors

# Run Prim's algorithm
minimum_spanning_tree = prim(graph)

# Print the minimum spanning tree
print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    print("{} -- {} with weight {}".format(edge[0], edge[1], graph[edge[0]][edge[1]]))

