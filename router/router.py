"""    
    This module contains the Router class, which is responsible for routing
    queries to the appropriate index.
"""

from trees.union_find import UnionFind


class Router:
    """
        The Router class manages the routing of queries to the appropriate index based on the connections between nodes (origins and destinations).
    """
    def __init__(self):
        self._node_index = {}
        self._uf = UnionFind(0)

    def add_route(self, origin, destination):
        """
            The add_route method adds a route between the origin and destination nodes.
            It updates the Union-Find structure to reflect the new connection.
            O(α(n))
        """
        if origin not in self._node_index:
            self._node_index[origin] = self._uf.add()
        if destination not in self._node_index:
            self._node_index[destination] = self._uf.add()

        self._uf.union(self._node_index[origin], self._node_index[destination])
        
    def are_connected(self, origin, destination):
        """
            The are_connected method checks if the origin and destination nodes are connected.
            O(α(n))
        """
        if origin not in self._node_index or destination not in self._node_index:
            return False
        return self._uf.connected(self._node_index[origin], self._node_index[destination])
    
    def zone_count(self):
        """
            The zone_count method returns the number of disjoint zones.
            O(1)
        """
        return self._uf.num_sets()