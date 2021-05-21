from dijkstra.dijkstra import Dijkstra
from graph.graph import Graph


if __name__ == "__main__":
    origin = input("Type the origin point: ")
    destiny = input("Type the destiny point: ")

    graph = Graph()
    g = graph.make_dict_graph("grafo.txt")
    dijkstra = Dijkstra(g, origin, destiny)

    
    d, path = dijkstra.generate_shortest_path()

    print(f"\n{origin} -> {destiny}")
    print(f"distance {d}, {path}")