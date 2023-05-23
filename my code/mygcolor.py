def printConfiguration(colorArray):
	print('Assigned colors:')
	for i in range(len(colorArray)):
		print('Vertex:', i, 'Color: ', colorArray[i])
		
def isSafe(graph, colorArray, vertex, color):
	for i in range(len(graph)):
		if graph[vertex][i] and colorArray[i]==color:
			return False
	return True
	
def graphF(graph, m, vertex, colorArray):
	if vertex == len(graph):
		return True
	
	for color in range(1, m+1):
		if isSafe(graph, colorArray, vertex, color):
			colorArray[vertex] = color
			if graphF(graph, m, vertex+1, colorArray):
				return True
			colorArray[vertex] = 0
	return False
	
	
graph = []
n = int(input('Enter number of vertices: '))

print('Enter adjacency matrix (space-seperated values):')

for _ in range(n):
	row = list(map(int, input().split()))
	graph.append(row)

m = int(input('Enter the number of colors: '))

colorArray = [0]*n

if graphF(graph, m, 0, colorArray):
	print('Coloring is possible!')
	printConfiguration(colorArray)

else:
	print('Coloring is not possible')
