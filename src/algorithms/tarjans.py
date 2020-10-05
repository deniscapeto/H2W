from typing import DefaultDict


class Tarjan:

    graph = DefaultDict(list)
    critical_connections = []
    visitedTimes = {}
    lowTimes = {}
    time = 0
    visited = []

    def get_critical_connections(self, connections):
        self.build_graph(connections)

        self.dfs(1, -1)

        return self.critical_connections

    def dfs(self, current_node, parent_node):

        print(f'DFS ---> {current_node}')

        self.visited.append(current_node)
        self.visitedTimes[current_node] = self.time
        self.lowTimes[current_node] = self.time

        self.time += 1

        for neighbor in self.graph[current_node]:
            if neighbor == parent_node:
                continue
                
            if neighbor not in self.visited:
                self.dfs(neighbor, current_node)

                self.lowTimes[current_node] = min(
                    self.lowTimes[current_node],
                    self.lowTimes[neighbor]
                )

                # THAT MEANS THE ONLY WAY TO REACH THIS NEIGHBOR IS THROUGH CURRENT NODE
                if self.visitedTimes[current_node] < self.lowTimes[neighbor]:
                    print(f'current_node: {current_node}, neighbor: {neighbor}')
                    print(f'visitedTimes: {self.visitedTimes}')
                    print(f'    lowTimes: {self.lowTimes}')


                    #self.critical_connections.append((current_node, neighbor))

                    # IF NEIGHBOR HAS ANY CONNECTION OTHER THAN THE CURRENT NODE
                    # IT MEANs that is we cut noeighbor node it will not disconect 
                    # other node, and so creating another graph
                    if len(self.graph[neighbor]) > 1:
                        # NOT GRAPH EDGE (LIMITE)
                        self.critical_connections.append(neighbor)

                    self.critical_connections.append(current_node)

            else: # back edge

                print(f'Updating lowtime: {current_node}: {self.lowTimes[current_node]} -> {self.visitedTimes[neighbor]}')
                self.lowTimes[current_node] = min(
                    self.lowTimes[current_node], self.visitedTimes[neighbor]
                )

    def build_graph(self, connections):

        for connection in connections:
            self.graph[connection[0]].append(connection[1])
            self.graph[connection[1]].append(connection[0])



# connections = [[0,1],[1,2],[2,0],[1,3]]

# connections = [[0,1],[1,2],[0,2],[1,3]]

connections = [[1,2],[1,3],[2,3],[3,4],[4,5],[4,6],[5,7],[6,7],[7,8],[8,9],[8,10]]



t = Tarjan()

a = t.get_critical_connections(connections)

print(a)


