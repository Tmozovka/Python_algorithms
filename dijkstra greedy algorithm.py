# Python program for Dijkstra's single 
# source shortest path algorithm. The program is 
# for adjacency matrix representation of the graph 

# Library for INT_MAX 
import sys 

class Graph(): 

	def __init__(self, vertices): 
		self.V = vertices 
		self.graph = [[0 for column in range(vertices)] 
					for row in range(vertices)] 

	def printSolution(self, dist): 
		print ("Vertex tDistance from Source")
		for node in range(self.V): 
			print (node,"t",dist[node] )

	def find_min_value(self,arr,not_indexes):
		min = sys.maxsize
		min_index = -1
		for i in range(len(arr)):
			if arr[i] < min and i not in not_indexes:
				min = arr[i]
				min_index = i
		return min, min_index

	# Funtion that implements Dijkstra's single source 
	# shortest path algorithm for a graph represented 
	# using adjacency matrix representation
	def dijkstra(self, src): 
		res = [sys.maxsize for i in range(self.V)]
		res[src] = 0
		checked_indexes = list()
		while len(checked_indexes) != self.V + 1:
			value, src = self.find_min_value(res,checked_indexes)
			#print(value, src)
			line = self.graph[src]
			checked_indexes.append(src)
			for i in range(self.V):	
				if line[i] != 0 and line[i] + value < res[i] and i not in checked_indexes:
					res[i] = self.graph[src][i] + value 
		
		return res

# Driver program 
g = Graph(9) 
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
		[4, 0, 8, 0, 0, 0, 0, 11, 0], 
		[0, 8, 0, 7, 0, 4, 0, 0, 2], 
		[0, 0, 7, 0, 9, 14, 0, 0, 0], 
		[0, 0, 0, 9, 0, 10, 0, 0, 0], 
		[0, 0, 4, 14, 10, 0, 2, 0, 0], 
		[0, 0, 0, 0, 0, 2, 0, 1, 6], 
		[8, 11, 0, 0, 0, 0, 1, 0, 7], 
		[0, 0, 2, 0, 0, 0, 6, 7, 0] ]

print(g.dijkstra(0))

 
