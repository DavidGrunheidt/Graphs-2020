from vertex import Vertex

class NotDirectedGraph:
	def __init__(self):
		self.vertices = dict()
		self.graph = dict()
		self.numberOfEdges = 0

	def addVertex(self, vertex_id: int, vertex_name: str) -> None:
		if not self.hasVertexId(vertex_id):
			self.vertices[vertex_id] = vertex_name
			self.graph[vertex_id] = Vertex(vertex_id, vertex_name)

	def addEdge(self, vertex1_id: int, vertex2_id: int, weight: float) -> None:	
		if self.hasVertexId(vertex1_id) and self.hasVertexId(vertex2_id):
			self.graph[vertex1_id].addEdge(vertex2_id, weight)
			self.graph[vertex2_id].addEdge(vertex1_id, weight)
			self.numberOfEdges += 1
		else:
			if not self.hasVertexId(vertex1_id):
				print("id " + vertex1_id + " is not in your vertices: " + ','.join(self.vertices) + "\n")
			if not self.hasVertexId(vertex2_id):
				print("id " + vertex2_id + " is not in your vertices: " + ','.join(self.vertices) + "\n")

	def getNumberOfVertices(self) -> int: 
		return len(self.vertices)

	def getNumberOfEdges(self) -> int: 
		return self.numberOfEdges

	def getVertexDegree(self, vertex_id: int) -> int:
		if self.hasVertexId(vertex_id):
			return self.graph[vertex_id].degree
		else:
			print("id " + vertex_id + " is not in your vertices " + ','.join(self.vertices))
			return -1

	def getVertexNeighbours(self, vertex_id: int) -> set:
		if self.hasVertexId(vertex_id):
			return self.graph[vertex_id].neighbors
		else: 
			print("id " + vertex_id + " is not in your vertices: " + ','.join(self.vertices))

	def hasVertexId(self, vertex_id: int) -> bool:
		return vertex_id in self.vertices

	def hasEdge(self, vertex1_id: int, vertex2_id: int) -> bool:
		if self.hasVertexId(vertex1_id) and self.hasVertexId(vertex2_id):
			return self.graph[vertex1_id].hasEdgeTo(vertex2_id)
		else:
			return False

	def weight(self, vertex1_id: int, vertex2_id: int) -> float:
		if self.hasVertexId(vertex1_id) and self.hasVertexId(vertex2_id):
			return self.graph[vertex1_id].getEdgeWeight(vertex2_id)
		else:
			return float("inf")