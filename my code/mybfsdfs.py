def bfs(graph, start_node, visited=None, queue=None):
    if visited is None:
        visited = []
    if queue is None:
        queue = [start_node]
        
    if not queue:
        return True
    
    node = queue.pop(0)
    print('->', node, end=' ')
    if node not in visited:
        visited.append(node)
        neighbors = graph[node]
        for neighbor in neighbors:
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)
    
    return bfs(graph, start_node, visited, queue)

def dfs(graph, start_node, visited=None, stack=None):
    if visited is None:
        visited = []
    if stack is None:
        stack = [start_node]

    if not stack:
        return True
    
    node = stack.pop()
    print('->', node, end=' ')
    if node not in visited:
        visited.append(node)
        neighbors = graph[node]
        for neighbor in neighbors:
            if neighbor not in visited and neighbor not in stack:
                stack.append(neighbor)
    return dfs(graph, start_node, visited, stack)
   
num_nodes = int(input('Enter number of nodes:'))
graph = [[] for _ in range(num_nodes)]

for i in range(num_nodes):
    neighbors = input(f'Enter the neighbors of node {i}: ').split()
    for neighbor in neighbors:
        graph[i].append(int(neighbor))


start_node = int(input('Enter the starting node: '))

print()
bfs(graph, start_node)
print()
dfs(graph, start_node)



