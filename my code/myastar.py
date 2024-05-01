def astarsearch(start_node, stop_node):
	open_set = set(start_node)
	closed_set = set()
	g = {}
	parents = {}
	g[start_node] = 0 
	parents[start_node] = start_node
	
	while(open_set):
		n = None
		for q in open_set:
			if n == None or g[q]+heuristic[q]<g[n]+heuristic[n]:
				n = q
		
		if n == stop_node or Graph_nodes[n] == None:
			pass
		
		
		else:
			for (m, weight) in get_neighbours(n):
				if m not in open_set and m not in closed_set:
					open_set.add(m)
					parents[m] = n
					g[m] = g[n]+weight
				
				else:
					if g[m] > g[n]+weight:
						g[m] = g[n]+weight
						parents[m] = n
						if m in closed_set:
							closed_set.remove(m)
							open_set.add(m)
				
		if n == None:
			print('Path does not exist!')
			return None
		
		if n == stop_node:
			path = []
			while parents[n]!=n:
				path.append(n)
				n = parents[n]
			path.append(start_node)
			path.reverse()
			print('Path: {}'.format(path))
			return path
	
		open_set.remove(n)
		closed_set.add(n)
	print('Path does not exist!')
	return None
	

def get_neighbours(node):
	if node in Graph_nodes:
		return Graph_nodes[node]
	else:
		return None


Graph_nodes = {}

n = int(input("Enter no of edges: "))
for i in range(n):
    edge = input("Enter edge (format: source destination weight): ").split(' ')
    source = edge[0]
    dest = edge[1]
    weight = int(edge[2])
    if(source not in Graph_nodes):
        Graph_nodes[source] = [[dest, weight]]
    else:
        Graph_nodes[source].append([dest, weight])    
    if(dest not in Graph_nodes):
        Graph_nodes[dest] = [[source, weight]]
    else:
        Graph_nodes[dest].append([source, weight])
        
	
heuristic = {}
print("Enter heuristic values: ")
for key in Graph_nodes:
    print("Node: " + key)
    h = int(input("H: "))
    heuristic[key] = h
    
while(true):
    s = input("Enter source: ")
    d = input("Enter destination: ")
    astarsearch(s, d)
