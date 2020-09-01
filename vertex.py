class Vertex:
	def __init__(self, vertex_id: str, vertex_name: str):
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

	# O(1) -> https://wiki.python.org/moin/TimeComplexity/#dict (k in d), "in" operation is O(1)
	def hasEdgeTo(self, vertex_id: str) -> bool:
		return vertex_id in self.neighbors

	# O(1) -> hasEdgeTo = O(1), self.edges[vertex_id] = O(1) (https://wiki.python.org/moin/TimeComplexity/#dict (get item))
	def getEdgeWeight(self, vertex_id: str) -> float:
		if self.hasEdgeTo(vertex_id):
			return self.edges[vertex_id][0]
		else: 
			return float("inf")