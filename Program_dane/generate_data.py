import random
N = 400
f = open("wejscie6.txt", "w")
random.seed(a=None, version=2)
from collections import defaultdict

class Graph():
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        if not (v in self.graph[u]):
            self.graph[u].append(v)

    def printAll(self):
        print(self.graph)

    def delete_wrong(self, u):
        self.graph[u].pop()

    def DFS(self, u, color):
        color[u] = "GRAY"
        for v in self.graph[u]:
            if color[v] == "GRAY":
                return True
            if color[v] == "WHITE" and self.DFS(v, color):
                return True
        color[u] = "BLACK"
        return False

    def isCyclic(self):
        color = ["WHITE"] * self.V

        for i in range(self.V):
            if color[i] == "WHITE":
                if self.DFS(i, color):
                    return True
        return False


g = Graph(N+1)
copy_g = g
counter = 0
first = 1
second = 2
for i in range(1000000):
    first = random.randrange(1, N + 1)
    second = random.randrange(1, N + 1)
    while first == second:
        first = random.randrange(1, N + 1)
        second = random.randrange(1, N + 1)
    g.addEdge(first, second)
    if g.isCyclic():
        g.delete_wrong(first)
    else:
     #   g.printAll()
        counter += 1
        copy_g = g
        third = str(first) + " " + str(second) + "\n"
        f.write(third)
    if counter >= int(((N-1) * N) / 4):
        break

print(".")
if g.isCyclic():
    print("Graph contains cycle")
else:
    print("Graph doesn't contain cycle")
f.close()

