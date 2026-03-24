from collections import deque


class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = []
        
    def __repr__(self):
        return f"Vertex(value={self.value!r})"

    def add_adjacent_vertex(self, vertex):
        self.adjacent_vertices.append(vertex)


roald = Vertex("Roald")
drift = Vertex("Drift")
fauna = Vertex("Fauna")
maple = Vertex("Maple")
sprocket = Vertex("Sprocket")
niko  = Vertex("Niko")


roald.add_adjacent_vertex(fauna)
roald.add_adjacent_vertex(drift)
fauna.add_adjacent_vertex(drift)
fauna.add_adjacent_vertex(maple)
drift.add_adjacent_vertex(maple)
maple.add_adjacent_vertex(sprocket)
sprocket.add_adjacent_vertex(niko)
niko.add_adjacent_vertex(drift)

'''
Exercise 1

    DFS Traversal
'''

def dfs_traverse(vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex.value)
    print(vertex.value)

    for neighbour in vertex.adjacent_vertices:
        if neighbour.value not in visited:
            dfs_traverse(neighbour, visited)

dfs_traverse(roald)

'''
Exercise 2

    BFS Traversal
'''

def bfs_traverse(start_vertex):
    visited = {start_vertex.value}
    queue = deque([start_vertex])

    while queue:
        current = queue.popleft()
        print(current.value)

        for neighbour in current.adjacent_vertices:
            if neighbour.value not in visited:
                visited.add(neighbour.value)
                queue.append(neighbour)
            

bfs_traverse(roald)

'''
Exercise 3

    BFS Search
'''

def bfs(start_vertex, search_value):
    visited = {start_vertex.value}
    queue = deque([start_vertex])
    visit_count = 0

    while queue:
        current = queue.popleft()
        visit_count += 1
        
        if current.value == search_value:
            return current, visit_count

        for neighbour in current.adjacent_vertices:
            if neighbour.value not in visited:
                visited.add(neighbour.value)
                queue.append(neighbour)
    
    return None, visit_count


result, count = bfs(roald, "Niko")
print(f"Found: {result}, Vertices: {count}")

