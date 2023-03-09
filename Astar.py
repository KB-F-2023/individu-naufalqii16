import heapq

class Node:
    def __init__(self, name, heuristic=float('inf')):
        self.name = name
        self.heuristic = heuristic
        self.neighbors = {}
        
    def add_neighbor(self, name, cost):
        self.neighbors[name] = cost
        
    def get_neighbors(self):
        return self.neighbors
        
class Graph:
    def __init__(self):
        self.vertices = {}
        
    def add_vertex(self, name, heuristic=float('inf')):
        self.vertices[name] = Node(name, heuristic)
        
    def add_edge(self, frm, to, cost):
        if frm not in self.vertices:
            self.add_vertex(frm)
        if to not in self.vertices:
            self.add_vertex(to)
        self.vertices[frm].add_neighbor(to, cost)
        self.vertices[to].add_neighbor(frm, cost)
        
    def get_node(self, name):
        return self.vertices[name]
    
def astar(graph, start, goal):
    visited = set()
    heap = [(0, start)]
    while heap:
        (cost, current) = heapq.heappop(heap)
        if current == goal:
            return cost
        if current in visited:
            continue
        visited.add(current)
        for neighbor, distance in graph.get_node(current).get_neighbors().items():
            if neighbor in visited:
                continue
            heuristic = graph.get_node(neighbor).heuristic
            heapq.heappush(heap, (cost + distance + heuristic, neighbor))
    return float('inf')

# generate graph
g = Graph()
g.add_vertex('A', 366)
g.add_vertex('B', 0)
g.add_vertex('C', 160)
g.add_vertex('D', 242)
g.add_vertex('E', 161)
g.add_vertex('F', 178)
g.add_vertex('G', 77)
g.add_vertex('H', 151)
g.add_vertex('I', 226)
g.add_vertex('J', 244)
g.add_vertex('K', 241)
g.add_vertex('L', 329)
g.add_vertex('M', 312)
g.add_vertex('N', 358)
g.add_vertex('O', 380)
g.add_vertex('P', 193)
g.add_vertex('Q', 420)
g.add_vertex('R', 400)

g.add_edge('A', 'B', 118)
g.add_edge('A', 'C', 140)
g.add_edge('A', 'D', 75)
g.add_edge('B', 'E', 80)
g.add_edge('C', 'F', 99)
g.add_edge('D', 'G', 120)
g.add_edge('E', 'H', 97)
g.add_edge('F', 'I', 211)
g.add_edge('G', 'J', 138)
g.add_edge('H', 'K', 101)
g.add_edge('I', 'L', 90)
g.add_edge('J', 'M', 75)
g.add_edge('K', 'N', 97)
g.add_edge('L', 'O', 146)
g.add_edge('M', 'P', 138)
g.add_edge('N', 'Q', 101)
g.add_edge('O', 'R', 97)

# set start and goal
# specify start and goal nodes
start = 'A'
goal = 'K'

# specify SLD values
g.get_node('A').heuristic = 366
g.get_node('B').heuristic = 0
g.get_node('C').heuristic = 160
g.get_node('D').heuristic = 242
g.get_node('E').heuristic = 161
g.get_node('F').heuristic = 178
g.get_node('G').heuristic = 77
g.get_node('H').heuristic = 151
g.get_node('I').heuristic = 226
g.get_node('J').heuristic = 244
g.get_node('K').heuristic = 241
g.get_node('L').heuristic = 329
g.get_node('M').heuristic = 312
g.get_node('N').heuristic = 358
g.get_node('O').heuristic = 380
g.get_node('P').heuristic = 193
g.get_node('Q').heuristic = 420
g.get_node('R').heuristic = 0

# perform A*
cost = astar(g, start, goal)

# print result
print("Shortest path from", start, "to", goal, "is", cost)


