import numpy as np
import matplotlib.pyplot as plt

class MinPQ(object):
    def __init__(self):
        self._arr = []
        self._obj2idx = {} # Key: obj (hashable), Value: Index into _arr where we can find obj

    def __contains__(self, obj):
        """
        Check to see whether a particular object is in the heap

        Parameters
        ----------
        obj: hashable object
            The object to check

        Returns
        -------
        True if object is in the heap, False otherwise
        """
        return obj in self._obj2idx
    
    def __getitem__(self, obj):
        """
        Return the priority of an object in the heap

        Parameters
        ----------
        obj: hashable object
            The object to check
        
        Returns
        -------
        Priority of this object
        """
        assert(obj in self)
        return self._arr[self._obj2idx[obj]][0]
    
    def __len__(self):
        """
        Length of the heap
        """
        return len(self._arr)

    def _children(self, i):
        """
        Parameters
        ----------
        i: int
            Index of a node

        Returns
        -------
        list of indices of children of that node
        """
        children = []
        if 2*i + 1 < len(self._arr):
            children.append(2*i + 1)
        if 2*i + 2 < len(self._arr):
            children.append(2*i + 2)
        return children
    
    def _parent(self, i):
        """
        Parameters
        ----------
        i: int
            Index of a node
        
        Returns
        -------
        Index of the parent node
        """
        return (i-1)//2
    
    def _swap(self, i, j):
        """
        Swap two elements in the heap, being sure to update
        _obj2idx appropriately

        Parameters:
        ----------
        i: int
            Index of first node
        j: int
            Index of second node
        """
        obji = self._arr[i][1]
        objj = self._arr[j][1]
        self._obj2idx[obji] = j
        self._obj2idx[objj] = i
        self._arr[i], self._arr[j] = self._arr[j], self._arr[i]
        
    
    def _heapup(self, i):
        """
        Keep bubbling the node at i up until it 
        satisfies the heap condition

        Parameters
        ----------
        i: int
            Node to check
        """
        if i > 0:
            parent = self._parent(i)
            if self._arr[i][0] < self._arr[parent][0]:
                self._swap(i, parent)
                self._heapup(parent)
                
    def _heapdown(self, i):
        """
        Keep moving a node at i down until it satisfies the
        heap condition, swapping it with the smaller of its two
        children if not

        Parameters
        ----------
        i: int
            Node to check
        """
        children = self._children(i)
        if len(children) > 0:
            ## Make child be the smaller of the two children
            child = children[0]
            if len(children) > 1:
                if self._arr[children[1]][0] < self._arr[children[0]][0]:
                    child = children[1]
            if self._arr[child][0] < self._arr[i][0]:
                self._swap(i, child)
                self._heapdown(child)
        
    def push(self, entry):
        """
        Add an element to the heap

        Parameters
        ----------
        entry: (priority, obj)
            Priority and object to add (following python's heappush convention)
        """
        ## Step 1: Put this entry at the end of the _arr
        self._arr.append(entry)
        self._obj2idx[entry[1]] = len(self._arr)-1

        ## Step 2: Bubble up entry until the heap condition is satisfied
        self._heapup(len(self._arr)-1)
    
    def pop(self):
        """
        Remove and return the element with the smallest priority from the heap

        Returns
        -------
        (priority, obj)
            Priority and object with the smallest priority (following python's heappop convention)
        """
        assert(len(self._arr) > 0)
        ret = self._arr[0]
        ## Move the last element to the root
        self._swap(0, -1)
        ## Take off the last element
        del self._obj2idx[ret[1]]
        self._arr.pop()
        ## Fix up the internal structure
        self._heapdown(0)
        return ret

    def update(self, entry):
        """
        Update the priority of a particular object

        Parameters
        ----------
        entry: (priority, obj)
            Object to update, as well as its new priority
        """
        (new_priority, obj) = entry
        assert(obj in self)
        idx = self._obj2idx[obj]
        old_priority = self._arr[idx][0]
        self._arr[idx] = (new_priority, obj)
        if new_priority < old_priority:
            self._heapup(idx)
        elif new_priority > old_priority:
            self._heapdown(idx)
    
    def draw(self, fac=1.5):
        """
        Draw the heap
        
        Parameters
        ----------
        fac: float
            Factor of amount of space to put between nodes when drawing
        """
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
                x0 -= fac*2**(height-level-1)
            stride = fac*2**(height-level)
            x = x0 + xi*stride
            y = -5*level
            plt.scatter([x], [y], 100, c='k')
            s = "{}".format(self._arr[i][0])
            if self._arr[i][1]:
                s = s + " ({})".format(self._arr[i][1])
            plt.text(x, y-0.7, s, horizontalalignment='center')
            xs[i] = x
            ys[i] = y
            xi += 1
        # Next draw edges
        for i in range(N):
            for j in self._children(i):
                plt.plot([xs[i], xs[j]], [ys[i], ys[j]])
        plt.axis("off")
        plt.axis("equal")


if __name__ == '__main__':
    pq = MinPQ()
    pq.push((10, "Theo"))
    pq.push((20, "Chris"))
    pq.push((5, "Celia"))
    pq.push((1, "Layla"))
    pq.push((2, "Artemis"))
    pq.push((3, "Apollo"))
    pq.update((0, "Theo"))
    pq.update((25, "Artemis"))
    pq.update((40, "Apollo"))
    pq.update((-1, "Celia"))
    while len(pq) > 0:
        print(pq.pop())