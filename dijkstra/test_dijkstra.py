from collections import defaultdict
from dijkstra import Dijkstra

edges = [
    ("O", "A", 2),
    ("O", "C", 4),
    ("O", "B", 5),
    ("A", "D", 7),
    ("A", "B", 2),
    ("B", "D", 4),
    ("B", "E", 3),
    ("C", "B", 1),
    ("C", "E", 4),
    ("D", "T", 5),
    ("E", "T", 7)
]


def make_dict_graph(edges) -> dict:
    """ This function transforms a list of edges into a graph dictionary."""
    graph = defaultdict(list)

    for origin, destiny, distance in edges:
        graph[origin].append((destiny, distance))
        graph[distance].append((origin, distance))
        
    return graph


def dijkstra_algorithm_test(edges):
    print("\n### Dijkstra alogrith test")
    try:
        d = Dijkstra(make_dict_graph(edges), "O", "T")
        distance_total, prev = d.dijkstra_algorithm()
        print(f" Total distance: {distance_total}")
        for p in prev:
            if prev[p] != None:
                print(f" {prev[p]} ")

    except:
        print("Error...")



def generate_shortest_path_test(edges):
    print("\n### Generate shortest path test")
    try:
        d = Dijkstra(make_dict_graph(edges), "O", "T")
        distance_total, path = d.generate_shortest_path()
        print(f" {path} \n")
    except:
        print("Error")



dijkstra_algorithm_test(edges)
generate_shortest_path_test(edges)