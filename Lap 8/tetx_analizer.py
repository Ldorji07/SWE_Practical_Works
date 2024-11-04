class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        # Add a vertex to the graph if it does not already exist.
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        # Add an edge between vertex1 and vertex2 (undirected).
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)  # For undirected graph
    
    def print_graph(self):
        # Print the graph in an adjacency list format.
        for vertex in self.graph:
            print(f"{vertex}: {' '.join(map(str, self.graph[vertex]))}")

# Test the Graph class
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.print_graph()

class Graph:
    # ... (previous methods remain the same)

    def dfs(self, start_vertex):
        # Perform Depth First Search (DFS) starting from start_vertex.
        visited = set()
        self._dfs_recursive(start_vertex, visited)
    
    def _dfs_recursive(self, vertex, visited):
        # Helper function for DFS that recursively visits vertices.
        visited.add(vertex)
        print(vertex, end=' ')
        
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)

# Test DFS
print("\nDFS starting from vertex 0:")
g.dfs(0)

from collections import deque

class Graph:
    # ... (previous methods remain the same)

    def bfs(self, start_vertex):
        # Perform Breadth First Search (BFS) starting from start_vertex.
        visited = set()
        queue = deque([start_vertex])
        visited.add(start_vertex)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=' ')

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

# Test BFS
print("\nBFS starting from vertex 0:")
g.bfs(0)

class Graph:
    # ... (previous methods remain the same)

    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        # Find all paths from start_vertex to end_vertex.
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in self.graph:
            return []
        paths = []
        for neighbor in self.graph[start_vertex]:
            if neighbor not in path:
                new_paths = self.find_all_paths(neighbor, end_vertex, path)
                for new_path in new_paths:
                    paths.append(new_path)
        return paths

# Test finding all paths
print("\nAll paths from vertex 0 to vertex 3:")
all_paths = g.find_all_paths(0, 3)
for path in all_paths:
    print(' -> '.join(map(str, path)))

class Graph:
    # ... (previous methods remain the same)

    def is_connected(self):
        # Check if the graph is connected.
        if not self.graph:
            return True
        start_vertex = next(iter(self.graph))
        visited = set()
        self._dfs_recursive(start_vertex, visited)
        return len(visited) == len(self.graph)

# Test if the graph is connected
print("\nIs the graph connected?", g.is_connected())

# Add a disconnected vertex and test again
g.add_vertex(4)
print("After adding a disconnected vertex:")
print("Is the graph connected?", g.is_connected())
