class Vertex:
	def __init__(self, vertex_id: int, vertex_name: str):
		self.vertex_id = vertex_id
		self.vertex_name = vertex_name
		self.neighbors = set()
		self.edges = dict()
		self.degree = 0

	def addEdge(self, vertex_id: str, weight: float) -> None:
		if (vertex_id not in self.neighbors):
			self.neighbors.add(vertex_id)
			self.edges[vertex_id] = [weight] 
		else:
			self.edges[vertex_id].append(weight)

		if (vertex_id == self.vertex_id):
			self.degree += 2
		else:
			self.degree += 1

	def hasEdgeTo(self, vertex_id: int) -> bool:
		return vertex_id in self.neighbors

	def getEdgeWeight(self, vertex_id: str) -> float:
		if self.hasEdgeTo(vertex_id):
			return self.edges[vertex_id]
		else: 
			return float("inf")