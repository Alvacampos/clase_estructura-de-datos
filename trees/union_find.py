"""
    Union-Find (Disjoint Set Union) implementation in Python.
    This data structure is used to keep track of a set of elements partitioned into disjoint subsets
    and supports union and find operations efficiently.
"""
class UnionFind:
    def __init__(self, n):
        """
            Initializes the Union-Find data structure with n elements, where each element is its own parent (representing a separate set).
            The rank array is used to keep track of the depth of the trees for union by rank optimization.
            The count variable keeps track of the number of disjoint sets.
        """
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n
        
    def add(self):
        """
            Add a new element as its own set. Returns its index. O(1).
        """
        idx = len(self.parent)
        self.parent.append(idx)
        self.rank.append(0)
        self.count += 1
        return idx

    def find(self, x):
        """
            The find method implements path compression to flatten the structure of the tree, making future find operations faster.
            BigO: O(α(n))
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """
            The union method merges two sets containing elements x and y.
            It uses union by rank to keep the tree balanced.
            BigO: O(α(n))
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            # Union by rank
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            self.count -= 1
    
    def connected(self, x, y):
        """ 
            The connected method checks if two elements x and y belong to the same set by comparing their roots.
            BigO: O(α(n))
        """            
        return self.find(x) == self.find(y)
    
    def num_sets(self):
        """ 
            The num_sets method returns the number of disjoint sets.
            BigO: O(1)
        """
        return self.count