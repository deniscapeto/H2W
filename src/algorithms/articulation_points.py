



from typing import DefaultDict

## tarjans algorithm

def breadth_first_search(item_to_find, graph):
    pass


class Graph:

    def __init__(self, number_of_vertex):
        self.number_of_vertex = number_of_vertex
        self.graph = DefaultDict(list)


    def addEdge(self, u, v):
        # since is an undirected graph we add both sides
        self.graph[u].append(v)
        self.graph[v].append(u)


def articulation_points(graph):
    pass

    
g = Graph(10)
g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(4,5)

g.addEdge(4,6)
g.addEdge(5,7)
g.addEdge(6,7)
g.addEdge(7,8)
g.addEdge(8,9)
g.addEdge(8,10)



articulation_points = articulation_points(g)