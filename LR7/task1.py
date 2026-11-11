# Варіант 44. Завдання 1. відбір на шляху від кореня.
# Класи мають підкласи: Tree містить Node, Node містить Record.


#Записи
class Record:

    def __init__(self, v):
        self.v = v

    def score(self):
        return self.v


class EnhancedRecord(Record):

    def score(self):
        return 2 * self.v


#Вузол
class Node:
    def __init__(self, id, record):
        self.id = id
        self.record = record   # власний запис
        self.parent = None     # батько
        self.children = []     # діти


#Дерево
class Tree:
    def __init__(self):
        self.nodes = {}        # номер -> вузол
        self.root = None

    def add_node(self, id, parent_id, record):
        node = Node(id, record)
        self.nodes[id] = node
        if parent_id == 0:
            self.root = node
        else:
            parent = self.nodes[parent_id]
            node.parent = parent
            parent.children.append(node)

    def traverse(self, node, result):
        result.append(node)
        for child in node.children:
            self.traverse(child, result)

    def path_to(self, id):
        path = []
        node = self.nodes[id]
        while node is not None:
            path.append(node)
            node = node.parent
        path.reverse()
        return path


def to_text(nodes):
    if len(nodes) == 0:
        return "-"
    return " ".join(str(node.id) for node in nodes)


#Головна частина
n = int(input())
tree = Tree()
for i in range(n):
    id, p, c, v = input().split()
    if c == "D":
        record = EnhancedRecord(int(v))
    else:
        record = Record(int(v))
    tree.add_node(int(id), int(p), record)
r, t = map(int, input().split())

order = []
path = []
if n > 0:
    tree.traverse(tree.root, order)
    path = tree.path_to(r)

selected = []
total = 0
for node in path:
    if node.record.score() <= t:     # однаковий виклик для N і D
        selected.append(node)
        total += node.record.score()

print("Обхід:", to_text(order))
print("Шлях:", to_text(path))
print("Відібрано:", to_text(selected))
print("Кількість:", len(selected))
print("Сума:", total)
