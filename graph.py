from vertex import Vertex

class NotDirectedGraph:
	def __init__(self):
		self.vertices = dict()
		self.graph = dict()
		self.numberOfEdges = 0

	def addVertex(self, vertex_id: str, vertex_name: str) -> None:
		if not self.hasVertexId(vertex_id):
			self.vertices[vertex_id] = vertex_name
			self.graph[vertex_id] = Vertex(vertex_id, vertex_name)

	def addEdge(self, vertex1_id: str, vertex2_id: str, weight: float) -> None:	
		if self.hasVertexId(vertex1_id) and self.hasVertexId(vertex2_id):
			self.graph[vertex1_id].addEdge(vertex2_id, weight)
			self.graph[vertex2_id].addEdge(vertex1_id, weight)
			self.numberOfEdges += 1
		else:
			self.__rise_exception_invalid_ids(vertex1_id, vertex2_id)

	def getNumberOfVertices(self) -> int: 
		return len(self.vertices)

	def getNumberOfEdges(self) -> int: 
		return self.numberOfEdges

	def getVertexDegree(self, vertex_id: str) -> int:
		if self.hasVertexId(vertex_id):
			return self.graph[vertex_id].degree

		self.__rise_exception_invalid_ids(vertex_id)

	def getVertexLabel(self, vertex_id: str) -> int:
		if self.hasVertexId(vertex_id):
			return self.graph[vertex_id].degree

		self.__rise_exception_invalid_ids(vertex_id)

	def getVertexNeighbours(self, vertex_id: str) -> set:
		if self.hasVertexId(vertex_id):
			return self.graph[vertex_id].vertex_name

		self.__rise_exception_invalid_ids(vertex_id)

	def hasVertexId(self, vertex_id: str) -> bool:
		return vertex_id in self.vertices

	def hasEdge(self, vertex1_id: str, vertex2_id: str) -> bool:
		if self.hasVertexId(vertex1_id) and self.hasVertexId(vertex2_id):
			return self.graph[vertex1_id].hasEdgeTo(vertex2_id)

		self.__rise_exception_invalid_ids(vertex1_id, vertex2_id)

	def weight(self, vertex1_id: str, vertex2_id: str) -> float:
		if self.hasVertexId(vertex1_id) and self.hasVertexId(vertex2_id):
			return self.graph[vertex1_id].getEdgeWeight(vertex2_id)

		self.__rise_exception_invalid_ids(vertex1_id, vertex2_id)

	def __rise_exception_invalid_ids(self, *vertices_ids: 'list[str]') -> None:
		not_included_ids = set()
		for vertex_id in vertices_ids:
			if not self.hasVertexId(vertex_id):
				not_included_ids.add(vertex_id)

		raise Exception("ids \""+str(not_included_ids)+"\" aren't in your vertices")
