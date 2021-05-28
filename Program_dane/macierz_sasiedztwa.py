import time
import copy
elem = [9, 500, 1000, 100, 200, 300, 400, 750]


class Graph:
    def __init__(self, n):
        self.v = n
        self.graph = [[0 for _ in range(n)] for _ in range(n)]

    def add(self, start, end):
        self.graph[start][end] = 1

    def DFS_rek(self, start, visited):
        #print(start, end=' ')
        visited[start] = True
        for i in range(self.v):
            if self.graph[start][i] == 1 and (not visited[i]):
                self.DFS_rek(i, visited)

    def DFS(self, visited):
        for i in range(self.v):
            if not visited[i]:
                self.DFS_rek(i, visited)

    def Kahn(self):
        in_degree = [0] * self.v
        top_order = []
        for v in self.graph:
            for k in range(self.v):
                if v[k] == 1:
                  in_degree[k] += 1

        queue = []
        for i in range(self.v):
            if in_degree[i] == 0:
                queue.append(i)
        #print("Dodaję pierwsze elementy: ",queue)
        count_visited = 0
        while queue and count_visited <= self.v:
            u = queue.pop(0)
            top_order.append(u)
            for i in range(self.v):
                if self.graph[u][i] == 1:
                    in_degree[i] -= 1
                    if in_degree[i] == 0 and i not in queue and i not in top_order:
                       queue.append(i)
            count_visited += 1

# 1. dodawanie wierzcholkow w grafie ----------------------------------------------------------------------------------
"""
def add(tab, file):
    for line in file:
        pos_start, pos_stop = line.split()
        pos_start = int(pos_start)
        pos_stop = int(pos_stop)
        tab[pos_stop - 1][pos_start - 1] = 1
    file.close()


def add_sample(tab):
    begin = time.time()
    plik = open("wejscie0.txt", "r")
    for line in plik:
        pos_start, pos_stop = line.split()
        pos_start = int(pos_start)
        pos_stop = int(pos_stop)
        tab[pos_stop - 1][pos_start - 1] = 1
    end = time.time()
    print(f"{end - begin}")
    plik.close()


# 2. rzedy w grafie - obliczanie ile ich jest -------------------------------------------------------------------------
def vertices_in_graph(tab):
    vertices = 0
    for i in range(n):
        sum_a = 0
        for j in range(n):
            if tab[i][j]:
                sum_a += 1
        if sum_a != 0:
            vertices += 1
    return vertices


# 3. czy istnieje luk? ------------------------------------------------------------------------------------------------
def if_edge_exist(tab, start, end):
    if tab[end][start]:
        return 1
    return 0



# -------------------------------------------------------- DFS --------------------------------------------------------
sample_visited = set()
visited = set()


def DFS(node, tab, n):
    global sample_visited
    global visited

    if node[1] not in visited:
        #    print(node[1]+1, end=" ")           # ta linijka wypisuje elementy za pomocą DFS poza pierwszym
        visited.add(node[1])
        for i in range(n):
            if tab[i][node[1]]:
                DFS([node[1], i], tab, n)


def start_DFS(n, tab):
    for start in range(n):
        for stop in range(n):
            if tab[stop][start]:
                if start not in visited:
                    #                print(start + 1, end=" ")   # wypisuje pierwszy element
                    visited.add(start)
                DFS([start, stop], tab, n)


# ------------------------------------------------------- Kahna -------------------------------------------------------
def find_0_set_list(tab, n, elements):
    S = set()
    for i in range(n):
        sum_a = 0
        if (i in elements) or (elements == [-1]):
            for j in range(n):
                if tab[i][j]:
                    sum_a += 1
            if sum_a == 0:
                S.add(i)
    return S

def start_Kahn(tab, n):
    c_tab = copy.copy(tab)
    S = find_0_set_list(c_tab, n, [-1])
    L = []
    while S:
        k = S.pop()
        L.append(k)
        potential_0s = []
        for i in range(n):
            if c_tab[i][k] == 1:
                c_tab[i][k] = 0
                potential_0s.append(i)
        S.update(find_0_set_list(c_tab, n, potential_0s))

"""

# sample na testy dla 9 wierzchołków
"""
sample_n = 9
sample_tab = [[0 for _ in range(sample_n)] for _ in range(sample_n)]

add_sample(sample_tab)
start_DFS(sample_n, sample_tab)
"""

for input_file in range(len(elem)):
    n = elem[input_file]
    graf = Graph(n)
    txt = "wejscie" + str(input_file) + ".txt"
    file = open(txt, "r")
    visited = [False] * n
    for line in file:
        pos_start, pos_stop = line.split()
        pos_start = int(pos_start)
        pos_stop = int(pos_stop)
        graf.add(pos_start-1, pos_stop-1)

    file.close()
    # --------------------------------------------------------------------------
    print(f"ms {int(n)} DFS {int(n * (n - 1) / 4)}", end=" ")
    begin = time.time()
    graf.DFS(visited)  # DFS
    end = time.time()
    print(f"{end - begin}")

for input_file in range(len(elem)):
    n = elem[input_file]
    graf = Graph(n)
    txt = "wejscie" + str(input_file) + ".txt"
    file = open(txt, "r")
    visited = [False] * n
    for line in file:
        pos_start, pos_stop = line.split()
        pos_start = int(pos_start)
        pos_stop = int(pos_stop)
        graf.add(pos_start-1, pos_stop-1)
    file.close()


    # --------------------------------------------------------------------------
    print(f"ms {int(n)} Kahn {int(n * (n - 1) / 4)}", end=" ")
    begin = time.time()
    graf.Kahn()
    end = time.time()
    print(f"{end - begin}")
    
