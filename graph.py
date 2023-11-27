from heap import MinPQ

UNTOUCHED = 0
FRONTIER = 1
VISITED = 2

class Vertex:
    def __init__(self, label):
        self.label = label
        self.neighbs = set([]) # Stores (weight, Vertex object) tuples
        self.state = UNTOUCHED
    
    def __repr__(self):
        return "{}".format(self.label)

class Graph:
    def __init__(self):
        # Key: Vertex to look up
        # Value is the object encapsulating
        # information about that vertex
        self.vertices = {}

    def add_vertex(self, u):
        self.vertices[u] = Vertex(u)
    
    def add_edge(self, u, v, w):
        """
        Add a weighted edge between two vertices

        Parameters
        ----------
        u: hashable
            Hashable identifier of first vertex (usually int or string)
        u: hashable
            Hashable identifier of second vertex (usually int or string)
        w: float
            Weight of edge
        """
        self.vertices[u].neighbs.add((w, self.vertices[v]))
        self.vertices[v].neighbs.add((w, self.vertices[u]))
    
    def explore(self, start):
        """
        Given V vertices and E edges in the graph
        
        Perform Dijkstra's algorithm to find the lengths of the shortest 
        paths from "start" to all other vertices

        Parameters
        ----------
        start: hashable
            Lable of vertex at which to start the search
        
        Returns
        -------
        dictionary: label->distance
            Distance of all vertices from the start
        """
        frontier = MinPQ()
        frontier.push([0, start, self.vertices[start]])
        distances = {} ## TODO: Fill this in
        # Each vertex passes through the frontier exactly once
        while len(frontier) > 0: # O(V) iterations
            pass
            ## TODO: Take off the node at the front and record its distance

            # Look at each neighbor of v.  Add its weight to the distance
            # to get d'
            # a) If it's not on the queue and it hasn't been visited, 
            # add the neighbor with priority d'
            # b) If it's already on the queue and d' is less than its priority, 
            # update the priority
            # Otherwise, if it's already been visited, do nothing
        
        return distances