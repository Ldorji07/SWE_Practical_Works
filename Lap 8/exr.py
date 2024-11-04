from collections import deque
import heapq

class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2, weight=1):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append((vertex2, weight))
        self.graph[vertex2].append((vertex1, weight))  # For undirected graph
    
    def print_graph(self):
        for vertex in self.graph:
            print(f"{vertex}: {' '.join(f'{neighbor} (weight={weight})' for neighbor, weight in self.graph[vertex])}")

    def dfs(self, start_vertex):
        visited = set()
        self._dfs_recursive(start_vertex, visited)
    
    def _dfs_recursive(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=' ')
        
        for neighbor, _ in self.graph[vertex]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)

    def bfs(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])
        visited.add(start_vertex)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=' ')

            for neighbor, _ in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in self.graph:
            return []
        paths = []
        for neighbor, _ in self.graph[start_vertex]:
            if neighbor not in path:
                new_paths = self.find_all_paths(neighbor, end_vertex, path)
                for new_path in new_paths:
                    paths.append(new_path)
        return paths

    def is_connected(self):
        if not self.graph:
            return True
        start_vertex = next(iter(self.graph))
        visited = set()
        self._dfs_recursive(start_vertex, visited)
        return len(visited) == len(self.graph)

    def shortest_path(self, start_vertex, end_vertex):
        if start_vertex not in self.graph or end_vertex not in self.graph:
            return None

        visited = set()
        queue = deque([[start_vertex]])
        
        while queue:
            path = queue.popleft()
            vertex = path[-1]

            if vertex == end_vertex:
                return path

            for neighbor, _ in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    new_path = list(path)  
                    new_path.append(neighbor)
                    queue.append(new_path)
        return None

    def has_cycle(self):
        visited = set()
        
        def dfs(vertex, parent):
            visited.add(vertex)
            for neighbor, _ in self.graph[vertex]:
                if neighbor not in visited:
                    if dfs(neighbor, vertex):
                        return True
                elif neighbor != parent:
                    return True
            return False

        for v in self.graph:
            if v not in visited:
                if dfs(v, None):
                    return True
        return False

    def dijkstra(self, start_vertex):
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start_vertex] = 0
        priority_queue = [(0, start_vertex)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        return distances

    def is_bipartite(self):
        color = {}
        
        for vertex in self.graph:
            if vertex not in color:
                color[vertex] = 0
                queue = deque([vertex])
                
                while queue:
                    v = queue.popleft()
                    for neighbor, _ in self.graph[v]:
                        if neighbor not in color:
                            color[neighbor] = 1 - color[v] 
                            queue.append(neighbor)
                        elif color[neighbor] == color[v]:
                            return False
        return True

# Example Usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(1, 3, 2)  # Adding weight to an edge

g.print_graph()

print("\nDFS starting from vertex 0:")
g.dfs(0)

print("\nBFS starting from vertex 0:")
g.bfs(0)

print("\nAll paths from vertex 0 to vertex 3:")
all_paths = g.find_all_paths(0, 3)
for path in all_paths:
    print(' -> '.join(map(str, path)))

print("\nIs the graph connected?", g.is_connected())

print("\nShortest path from vertex 0 to vertex 3:", g.shortest_path(0, 3))

print("\nDoes the graph have a cycle?", g.has_cycle())

print("\nDijkstra's shortest paths from vertex 0:", g.dijkstra(0))

print("\nIs the graph bipartite?", g.is_bipartite())
