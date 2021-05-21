import collections
from graph import Graph

def read_edges_file_test():
    print("\n### Read edges file test")
    try:
        g = Graph()
        edges = g.read_edges_file("./grafo.txt")

        for edge in edges:
            print(f" {edge} ")   
    except:
        print("Error...")


def make_dict_graph_test():
    print("\n### Make dict graph test")
    try:
        g = Graph()
        graph_dict = g.make_dict_graph("./grafo.txt")

        if type(graph_dict) == collections.defaultdict:
            for key in graph_dict:
                print(f" {key}: {graph_dict[key]} ")
        else:
            raise TypeError("Not return a dict...")
    except :
        print("Error...")


read_edges_file_test()
make_dict_graph_test()