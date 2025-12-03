import random


class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacent = {}

    def add_edge_to(self, vertex: 'Vertex', weight: int = 0):
        self.adjacent[vertex] = weight

    def increment_edge(self, vertex: 'Vertex'):
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1

    @property
    def adjacent_nodes(self) -> list:
        return list(self.adjacent.keys())

    @property
    def adjacent_weights(self) -> list:
        return list(self.adjacent.values())

    def next_word(self) -> 'Vertex':
        return random.choices(self.adjacent_nodes, self.adjacent_weights)[0]


class Graph:
    def __init__(self):
        self.vertices: dict[str, Vertex] = {}

    def __bool__(self):
        return bool(self.vertices)

    def get_vertex_values(self) -> list[str]:
        return list(self.vertices.keys())

    def add_vertex(self, value: str):
        self.vertices[value] = Vertex(value)

    def get_vertex(self, value: str) -> Vertex:
        if value not in self.vertices:
            self.add_vertex(value)
        return self.vertices[value]

    def get_next_word(self, current_vertex: Vertex) -> Vertex:
        return self.vertices[current_vertex.value].next_word()

    def flush(self):
        self.vertices.clear()
