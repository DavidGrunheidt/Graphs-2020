from not_directed_graph import NotDirectedGraph

class DirectedGraph(NotDirectedGraph):
	def __init__(self):
		self.vertices = dict()
		self.graph = dict()
		self.numberOfEdges = 0

	def addEdge(self, vertex1_id: str, vertex2_id: str, weight: float) -> None:
		if self.hasVertexId(vertex1_id) and self.hasVertexId(vertex2_id):
			self.graph[vertex1_id].addEdge(vertex2_id, weight)
			self.numberOfEdges += 1
		else:
			self.__rise_exception_invalid_ids(vertex1_id, vertex2_id)

	def removeEdge(self, vertex1_id: str, vertex2_id: str) -> None:
		if self.hasVertexId(vertex1_id) and self.hasVertexId(vertex2_id):
			self.graph[vertex1_id].removeEdge(vertex2_id)
			self.numberOfEdges -= 1
		else:
			self.__rise_exception_invalid_ids(vertex1_id, vertex2_id)


