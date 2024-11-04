from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)  
    def shortest_path(self, start_vertex, end_vertex):
        """Find the shortest path between two vertices using BFS."""
        visited = set()
        queue = deque([(start_vertex, [start_vertex])])

        while queue:
            vertex, path = queue.popleft()
            if vertex == end_vertex:
                return path
            
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        return None  

    def has_cycle_util(self, vertex, visited, parent):
        """Utility function to detect a cycle in the graph."""
        visited.add(vertex)
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                if self.has_cycle_util(neighbor, visited, vertex):
                    return True
            elif parent != neighbor:
                return True
        return False

    def has_cycle(self):
        """Detect cycles in the graph."""
        visited = set()
        for vertex in self.graph:
            if vertex not in visited:
                if self.has_cycle_util(vertex, visited, None):
                    return True
        return False

    def dijkstra(self, start_vertex):
        """Implement Dijkstra's algorithm to find the shortest paths in a weighted graph."""
        from heapq import heappop, heappush
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start_vertex] = 0
        priority_queue = [(0, start_vertex)]

        while priority_queue:
            current_distance, current_vertex = heappop(priority_queue)

            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heappush(priority_queue, (distance, neighbor))

        return distances

    def is_bipartite(self):
        """Determine if the graph is bipartite."""
        color = {}
        for vertex in self.graph:
            if vertex not in color:
                queue = deque([vertex])
                color[vertex] = 0  

                while queue:
                    current = queue.popleft()
                    for neighbor in self.graph[current]:
                        if neighbor not in color:
                            color[neighbor] = 1 - color[current]
                            queue.append(neighbor)
                        elif color[neighbor] == color[current]:
                            return False
        return True

# Example usage of the implemented methods
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)

print("Shortest path from vertex 0 to vertex 3:", g.shortest_path(0, 3))


g.add_edge(3, 1)  
print("Does the graph have a cycle?", g.has_cycle())

weighted_graph = Graph()
weighted_graph.add_edge(0, 1)
weighted_graph.add_edge(0, 2)
weighted_graph.add_edge(1, 2)
weighted_graph.add_edge(2, 3)
weighted_graph.graph[0] = [(1, 1), (2, 4)]
weighted_graph.graph[1] = [(0, 1), (2, 2)]
weighted_graph.graph[2] = [(0, 4), (1, 2), (3, 1)]
weighted_graph.graph[3] = [(2, 1)]
print("Dijkstra's shortest paths from vertex 0:", weighted_graph.dijkstra(0))

print("Is the graph bipartite?", g.is_bipartite())
