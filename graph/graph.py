from collections import defaultdict


class Graph:
    def read_edges_file(self, edges_file) -> list:
        """This function extracts data from a file and stores it in a list of tuples"""
        with open(edges_file) as file:
            itens = [line.rstrip() for line in file]
    
        edges = []
        for item in itens:
            edges.append(tuple(item.split(",")))
        
        return edges

    def make_dict_graph(self, edges_file) -> dict:
        """ This function transforms a list of edges into a graph dictionary."""
        edge_list = self.read_edges_file(edges_file)
        graph = defaultdict(list)

        for origin, destiny, distance in edge_list:
            graph[origin].append((destiny, distance))
            graph[distance].append((origin, distance))
        
        return graph
    


    