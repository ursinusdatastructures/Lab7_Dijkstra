import numpy as np
import matplotlib.pyplot as plt

class MinPQ(object):
    def __init__(self):
        # Each arraylist entry is stored as a tuple (priority, (label, obj))
        # The smallest priority is at index 0
        self._arr = [] 

    def __len__(self):
        return len(self._arr)

    def _children(self, i):
        """
        Return the indices of the children of a particular
        node index

        Parameters
        ----------
        i: int
            Node index
        
        Returns
        -------
        List of [], [int] or [int, int]
            Children indices
        """
        children = []
        if 2*i+1 < len(self._arr):
            children.append(2*i+1)
        if 2*i+2 < len(self._arr):
            children.append(2*i+2)
        return children
    
    def _parent(self, i):
        """
        Compute the index of a parent of a node

        Parameters
        ----------
        i: int
            Node index
        
        Returns
        -------
        Index of parent of node
        """
        return (i-1)//2

    def draw(self):
        N = len(self._arr)
        height = int(np.ceil(np.log2(N)))
        width = 2**height
        xs = np.zeros(N)
        ys = np.zeros(N)
        level = -1
        xi = 0
        # First draw nodes, and remember positions
        # in the process
        x0 = width/2
        for i in range(N):
            if np.log2(i+1) == int(np.log2(i+1)):
                level += 1
                xi = 0
                x0 -= 2**(height-level-1)
            stride = 2**(height-level)
            x = x0 + xi*stride
            y = -5*level
            plt.scatter([x], [y], 100, c='k')
            s = "{}".format(self._arr[i][0])
            if self._arr[i][1]:
                s = s + " ({})".format(self._arr[i][1])
            plt.text(x+0.5, y, s)
            xs[i] = x
            ys[i] = y
            xi += 1
        # Next draw edges
        for i in range(N):
            for j in self._children(i):
                plt.plot([xs[i], xs[j]], [ys[i], ys[j]])
        plt.axis("off")
        plt.axis("equal")
    
    def _swap(self, i, j):
        """
        Swap the information stored in each node
        """
        self._arr[i], self._arr[j] = self._arr[j], self._arr[i]

    def _upheap(self, i):
        """
        Move an object up the heap until it is correctly placed

        Parameters
        ----------
        i: int
            Index of current item
        """
        parent = self._parent(i)
        if i > 0 and self._arr[i][0] < self._arr[parent][0]:
            self._swap(i, parent)
            self._upheap(parent)
    
    def _downheap(self, i):
        """
        Move an object up down the heap until it is correctly placed

        Parameters
        ----------
        i: int
            Index of current item
        """
        children = self._children(i)
        if len(children) > 0:
            child = children[0]
            if len(children) > 1:
                c2 = children[1]
                if self._arr[c2][0] < self._arr[child][0]:
                    child = c2
            if self._arr[child][0] < self._arr[i][0]:
                self._swap(i, child)
                self._downheap(child)

    def get_priority(self, label):
        """
        Get the current priority of a particular object

        Parameters
        ----------
        label: string
            Label of object
        
        Returns
        -------
        float: The priority
        """
        pass
        ## TODO: Fill this in

    def update_priority(self, label, priority):
        """
        Update the priority of an entry on the heap

        Parameters
        ----------
        label: hashable
            Label of object
        priority: float
            New priority of object
        """
        pass
        ## TODO: Fill this in

    def push(self, entry):
        """
        Add an entry to the heap

        Parameters
        ----------
        entry: (float, (hashable, obj))
            Tuple of (priority, (label, object))
        """
        self._arr.append(entry)
        self._upheap(len(self._arr)-1)
    
    def pop(self):
        """
        Remove and return the object with the lowest priority
        from the heap
        
        Returns
        -------
        obj: Lowest priority object
        """
        assert(len(self) > 0)
        ret = self._arr[0]
        self._arr[0] = self._arr[-1]
        self._arr.pop()
        self._downheap(0)
        return ret[1][1]
