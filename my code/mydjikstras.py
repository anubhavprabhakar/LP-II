#dijkstras

import sys

def dijkstras(graph, start):
    distances = {node: sys.maxsize for node in graph}
    distances[start] = 0
    visited = set()
    
    while len(visited)<len(graph):
        min_node = None
        for node in graph:
            if node not in visited and (min_node is None or distances[node]<distances[min_node]):
                min_node = node
        
        if min_node is None:
            break
        
        visited.add(min_node)
        current_distance = distances[min_node]
        
        for neighbor, weight in graph[min_node].items():
            distance = current_distance + weight
            if distance<distances[neighbor]:
                distances[neighbor] = distance
    
    return distances
    

graph = {}
num_nodes = int(input('Enter number of nodes: '))

for i in range(num_nodes):
    node = input('Enter name of node {}:'.format(i+1))
    graph[node] = {}
    
    num_neighbors = int(input('Enter number of neighbors of node {}:'.format(node)))
    for j in range(num_neighbors):
        neighbor, weight = input('Enter the name of neighbor and its weight (space-seperated): ').split()
        graph[node][neighbor] = int(weight)

start_node = input('Enter the starting node: ')

distances = dijkstras(graph, start_node)

print('Shortest distances from node {}:'.format(start_node))
for node, distance in distances.items():
    print('Node: {}, Distance: {}'.format(node, distance))
     


