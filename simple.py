from graph import Graph

if __name__ == '__main__':
    G = Graph()
    for i in range(6):
        G.add_vertex(chr(ord("a")+i))
    G.add_edge("a", "b", 1)
    G.add_edge("b", "c", 2)
    G.add_edge("a", "c", 4)
    G.add_edge("a", "f", 2)
    G.add_edge("e", "f", 4)
    G.add_edge("c", "e", 5)
    G.add_edge("d", "e", 2)
    G.add_edge("c", "d", 10)

    print(G.explore("a"))