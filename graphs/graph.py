import heapq
from collections import deque

from trees.union_find import UnionFind


class Graph:
    """
    Undirected weighted graph using adjacency list representation.
    """

    def __init__(self):
        self._adj = {}
        self._num_edges = 0

    def add_node(self, name):
        """Add a node if not already present. O(1) average."""
        if name not in self._adj:
            self._adj[name] = []

    def add_edge(self, u, v, weight=1):
        """
            Add an undirected edge between u and v with given weight.
            Adds the nodes if they don't exist yet.
            O(1) average.
        """
        self.add_node(u)
        self.add_node(v)
        self._num_edges += 1
        self._adj[u].append((v, weight))
        self._adj[v].append((u, weight))
    
    def neighbors(self, node):
        """Return list of (neighbor, weight) for a node. O(1) average."""
        if node not in self._adj:
            return []
        return self._adj[node]
    
    def nodes(self):
        """Return all nodes. O(V)."""
        return list(self._adj.keys())
    
    def edges(self):
        """Return all edges as list of (u, v, weight). O(V + E)."""
        result = []
        for u in self._adj:
            for v, w in self._adj[u]:
                if u < v:
                    result.append((u, v, w))
        return result
    
    def num_nodes(self):
        """O(1)."""
        return len(self._adj)
    
    def num_edges(self):
        """O(1)."""
        return self._num_edges

    def __len__(self):
        """Number of nodes. Allows len(graph) and use as `n` in benchmarks. O(1)."""
        return len(self._adj)

    def shortest_distances(self, start):
        """
        Compute shortest distance from `start` to every other node.
        Returns dict {node: distance}. Unreachable nodes have float('inf').
        Complexity: O((V + E) log V).
        """
        if start not in self._adj:
            return {}

        distances = {node: float('inf') for node in self._adj}
        distances[start] = 0

        pq = [(0, start)]

        while pq:
            current_dist, current = heapq.heappop(pq)

            if current_dist > distances[current]:
                continue

            for neighbor, weight in self.neighbors(current):
                new_dist = current_dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))

        return distances

    def bfs(self, start):
        """
            Breadth-First Search starting from `start`.
            Returns the list of visited nodes in order of visit.
            O(V + E).
        """
        if start not in self._adj:
            return []

        visited = set()
        queue = deque([start])
        visited.add(start)
        traversal_order = []
        while queue:
            current_node = queue.popleft()
            traversal_order.append(current_node)

            for neighbor, _ in self.neighbors(current_node):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return traversal_order

    def dfs(self, start):
        """
            Depth-First Search starting from `start`.
            Returns the list of visited nodes in order of visit.
            O(V + E).
        """
        if start not in self._adj:
            return []

        visited = set()
        result = []
        self._dfs_visit(start, visited, result)
        return result

    def _dfs_visit(self, node, visited, result):
        """Recursive helper for DFS."""
        visited.add(node)
        result.append(node)
        for neighbor, _ in self.neighbors(node):
            if neighbor not in visited:
                self._dfs_visit(neighbor, visited, result)

    def minimum_spanning_tree(self):
        """
            Return the Minimum Spanning Tree using Kruskal's algorithm.
            Returns list of (u, v, weight) edges, total V-1 edges if graph is connected.
            Complexity: O(E log E).
        """
        sorted_edges = sorted(self.edges(), key=lambda e: e[2])

        nodes = self.nodes()
        name_to_index = {name: i for i, name in enumerate(nodes)}
        uf = UnionFind(len(nodes))

        mst = []
        for u, v, weight in sorted_edges:
            u_idx = name_to_index[u]
            v_idx = name_to_index[v]
            if not uf.connected(u_idx, v_idx):
                uf.union(u_idx, v_idx)
                mst.append((u, v, weight))

        return mst
