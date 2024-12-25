# The Algorithm 
# 1.Build Max-Heap:  O(n)
#   Rearrange the input array to form a max-heap.

# 2.Sort: O(n log n)
#   Repeat until the heap size is 1: 
    #   Swap: Swap the root element (maximum value) with the last element of the heap.
    #   Reduce Heap Size: Reduce the effective size of the heap by 1 (without physically removing elements).
    #   Heapify: Restore the max-heap property at the root of the reduced heap.  O(log n) <- max_heapify may need to traverse the entire height of the heap to find the correct position for the node.
# 3.Result:
#   The array is now sorted in ascending order.

#-----------------------------codes------------------

def max_heapify(arr, n, i):
    """
    Maintains the max-heap property at a given index.
    """
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

def build_max_heap(arr):
    """
    Builds a max-heap from the given array.
    """
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

def heap_sort(arr):
    """
    Sorts the given array using the Heapsort algorithm.
    """
    n = len(arr)

    build_max_heap(arr)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, i, 0)

# Example usage
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)


###########################

# 1. Sort edges: Sort the edges in increasing order of weight (O(E log E)).

# 2. Initialize: Create parent and rank arrays for each vertex (O(V)).

# 3.Iterate through edges: For each edge (u, v, w): O(E) * O(log*V) ≈ O(E)
    # Find the sets of vertices u and v.
    # If they belong to different sets:
        # Add the edge to the MST.
        # Merge the sets of u and v using union by rank.
# Return: The resulting MST.

# Codes -------------

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1

    def KruskalMST(self):

        result = []
        i = 0
        e = 0

        self.graph = sorted(self.graph, key=lambda item: item[2]) 

        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        minimumCost = 0
        print("Edges in the constructed MST")
        for u, v, weight in result:
            minimumCost += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree", minimumCost)


if __name__ == '__main__':
    g = Graph(4)
    g.addEdge(0, 1, 10)
    g.addEdge(0, 2, 6)
    g.addEdge(0, 3, 5)
    g.addEdge(1, 3, 15)
    g.addEdge(2, 3, 4)

    g.KruskalMST()