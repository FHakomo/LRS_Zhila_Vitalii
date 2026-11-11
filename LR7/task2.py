# Варіант 44. Завдання 2. доступність за обмеженням оцінки.
# Класи мають підкласи: Graph містить Vertex, Vertex містить Record.


#Записи
class Record:

    def __init__(self, v):
        self.v = v

    def score(self):
        return self.v


class EnhancedRecord(Record):

    def score(self):
        return 2 * self.v


#Вершина
class Vertex:
    def __init__(self, id, record):
        self.id = id
        self.record = record   # власний запис
        self.neighbors = []    # сусіди


#Граф
class Graph:
    def __init__(self):
        self.vertices = {}     # номер -> вершина

    def add_vertex(self, id, record):
        self.vertices[id] = Vertex(id, record)

    def add_edge(self, u, w):
        self.vertices[u].neighbors.append(self.vertices[w])
        self.vertices[w].neighbors.append(self.vertices[u])

    def sort_neighbors(self):
        #Сортування сусідів по номеру
        for vertex in self.vertices.values():
            vertex.neighbors.sort(key=lambda x: x.id)

    def dfs(self, vertex, limit, visited, result):
        #Відвідування вершини та її невідвіданих сусідів
        visited.add(vertex.id)
        result.append(vertex)
        for neighbor in vertex.neighbors:
            if neighbor.id not in visited and neighbor.record.score() <= limit:
                self.dfs(neighbor, limit, visited, result)


def to_text(ids):
    #Виведення значень
    if len(ids) == 0:
        return "-"
    return " ".join(str(i) for i in ids)


#Головна частина
n, m, s = map(int, input().split())
graph = Graph()
for i in range(n):
    id, c, v = input().split()
    if c == "D":
        record = EnhancedRecord(int(v))
    else:
        record = Record(int(v))
    graph.add_vertex(int(id), record)
for i in range(m):
    u, w = map(int, input().split())
    graph.add_edge(u, w)
l, t = map(int, input().split())

graph.sort_neighbors()

order = []
if n > 0 and graph.vertices[s].record.score() <= t:   # стартова вершина має бути дозволена
    graph.dfs(graph.vertices[s], t, set(), order)

selected = []
total = 0
for vertex in order:
    if vertex.record.score() >= l:    # однаковий виклик для N і D
        selected.append(vertex.id)
        total += vertex.record.score()

visited_ids = [vertex.id for vertex in order]
unvisited = []
for id in sorted(graph.vertices):
    if id not in visited_ids:
        unvisited.append(id)

print("Обхід:", to_text(visited_ids))
print("Відібрано:", to_text(selected))
print("Кількість:", len(selected))
print("Сума:", total)
print("Невідвідані:", to_text(unvisited))
