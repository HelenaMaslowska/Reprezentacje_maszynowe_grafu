import time
import copy
elem = [9, 500, 1000, 100, 200, 300, 400, 750]

class Graph:
    def __init__(self, elem):
        self.V = elem
        self.graph = [[] for _ in range(self.V)]

    def add_one_edge(self, first, last):
        self.graph[first].append(last)
        self.graph[first].sort()

    def add(self):
        for line in file:
            pos_start, pos_stop = line.split()
            pos_start = int(pos_start)
            pos_stop = int(pos_stop)
            graf.add_one_edge(pos_start - 1, pos_stop - 1)
        file.close()

    def iteration(self):
        for i in range(self.V):
            print("Vertex:", str(i), end=" ")
            for last in self.graph[i]:
                print("-> {}".format(last), end = " ")
            print("")

    def vertices_in_graph(self):
        return self.V

    def if_edge_exist(self, first, last):
        if last in self.graph[first]:
            return True
        return False

    def start_DFS(self, start):
        path = []
        stack = [start]
        while len(stack) != 0:
            s = stack.pop()
            if s not in path:
                path.append(s)
                for neighbor in self.graph[s]:
                    stack.append(neighbor)
        return path

    def find_zero(self, element, tab):
        for i in tab:
            if element in i:
                return 1
        return 0

    def start_Kahn(self):
        c_tab = copy.copy(self.graph)
        path = []
        stack = []
        for i in range(len(c_tab)):
            if self.find_zero(i, c_tab) == 0:
                stack.append(i)
                path.append(i)
        while len(stack) != 0:
            i = stack.pop()
            c_mini_tab = c_tab[i]
            c_tab[i] = []
            for x in c_mini_tab:
                if self.find_zero(x, c_tab) == 0:
                    path.append(x)
                    stack.append(x)
        #print(path)


for input_file in range(len(elem)):
    n = elem[input_file]
    graf = Graph(n)
    txt = "wejscie" + str(input_file) + ".txt"
    file = open(txt, "r")

    graf.add()
    file.close()
    # --------------------------------------------------------------------------
    print(f"ls {int(n)} DFS {int(n * (n - 1) / 4)}", end=" ")
    begin = time.time()
    DFS_path = graf.start_DFS(0)
    end = time.time()
    print(f"{end - begin}")

for input_file in range(len(elem)):
    n = elem[input_file]
    graf = Graph(n)
    txt = "wejscie" + str(input_file) + ".txt"
    file = open(txt, "r")

    graf.add()
    file.close()
    # --------------------------------------------------------------------------
    print(f"ls {int(n)} Kahn {int(n * (n - 1) / 4)}", end=" ")
    begin = time.time()
    graf.start_Kahn()
    end = time.time()
    print(f"{end - begin}")