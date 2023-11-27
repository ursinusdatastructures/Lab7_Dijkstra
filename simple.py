from graph import Graph

if __name__ == '__main__':
    G = Graph()
    for i in range(6):
        G.add_vertex(i)
    G.add_edge(0, 1, 1)
    G.add_edge(1, 2, 2)
    G.add_edge(0, 2, 4)
    G.add_edge(0, 5, 2)
    G.add_edge(4, 5, 4)
    G.add_edge(2, 4, 5)
    G.add_edge(3, 4, 2)
    G.add_edge(2, 3, 10)

    