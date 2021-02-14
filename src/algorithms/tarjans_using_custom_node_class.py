from dataclasses import dataclass
from typing import DefaultDict, Union, List

@dataclass
class Node:

    number_id: int
    discovery_index: int
    lowest_index_to_reach: int
    neighbors: List['Node']
    visited: bool = False

    def __str__(self) -> str:
        return f'Node {self.number_id}, di: {self.discovery_index}, lo: {self.lowest_index_to_reach}, visited: {self.visited}, neighbor: {len( self.neighbors )} \n'

    def __repr__(self) -> str:
        return self.__str__()

class Tarjan:

    def __init__(self) -> None:
        
        self.discovery_index = 0
        self.graph = DefaultDict(self.newNode)

    def newNode(self):
        node = Node(
            number_id=0,
            discovery_index=self.discovery_index,
            lowest_index_to_reach=self.discovery_index,
            neighbors=[]
        )
        self.discovery_index += 1
        return node        

    critical_connections = set()

    def get_critical_connections(self, connections):
   
        self.build_graph(connections)

        first_item = next(iter(self.graph.values()))

        self.dfs(first_item, None)

        print(self.graph)

        return self.critical_connections

    def dfs(self,current_node: Node, parent_node: Union[None, Node]):
        
        current_node.visited = True

        for neighbor in current_node.neighbors:

            if parent_node and neighbor.number_id == parent_node.number_id:
                continue

            if not neighbor.visited:
                self.dfs(
                    current_node=neighbor,
                    parent_node=current_node
                )

                current_node.lowest_index_to_reach = min(
                    current_node.lowest_index_to_reach,
                    neighbor.lowest_index_to_reach
                )

                if current_node.discovery_index < neighbor.lowest_index_to_reach:

                    # Add as critical path if not edge (ponta do grafico)
                    if len(neighbor.neighbors) > 1:
                        self.critical_connections.add(neighbor.number_id)
                    
                    self.critical_connections.add(current_node.number_id)

            else:
                # back path 
                # so o set that the lowest index to reach this 
                # node can be made by coming from this neighbor
                current_node.lowest_index_to_reach = neighbor.discovery_index
                # min(
                #     neighbor.discovery_index,
                #     current_node.lowest_index_to_reach
                # )

    def build_graph(self, connections):

        for connection in connections:

            node1 = self.graph[connection[0]]
            node1.number_id = connection[0]

            node2 = self.graph[connection[1]]
            node2.number_id = connection[1]

            self.graph[connection[0]].neighbors.append(node2)
            self.graph[connection[1]].neighbors.append(node1)

connections = [[0,1],[1,2],[2,0],[1,3]]

# connections = [[0,1],[1,2],[0,2],[1,3]]

# connections = [[1,2],[1,3],[2,3],[3,4],[4,5],[4,6],[5,7],[6,7],[7,8],[8,9],[8,10]]

t = Tarjan()

a = t.get_critical_connections(connections)

print(a)