class Dijkstra:
    def __init__(self, graph, origin, destiny) -> None:
        self.graph = graph
        self.origin = origin
        self.destiny = destiny


    def dijkstra_algorithm(self) -> dict and dict:
        """this function will apply the dijkstra algorithm to the graph to return the shortest path"""
        nodes = []
        
        for node in self.graph:
            nodes.append(node)
            nodes += [n[0] for n in self.graph[node]]
        
        queue = set(nodes)
        nodes = list(queue)
        distances = dict()
        previous = dict()

        for node in nodes:
            distances[node] = float("inf")
            previous[node] = None
        
        distances[self.origin] = 0

        while len(queue) > 0:
            next_node = min(queue, key=distances.get)
            queue.remove(next_node)

            if next_node == self.destiny:
                return distances[self.destiny], previous

            for vertex, distance in self.graph.get(next_node, ()):
                alt = int(distances[next_node]) + int(distance)
                if alt < distances[vertex]:
                    distances[vertex] = alt
                    previous[vertex] = next_node
        
        return distances, previous
    

    def generate_shortest_path(self) -> str and list:
        """this function will generate the path taken by the algorithm"""
        distance, prev = self.dijkstra_algorithm()
        node = self.destiny
        parents = []

        while node != None:
            parents.append(node)
            node = prev[node]

        return distance, parents[::-1]