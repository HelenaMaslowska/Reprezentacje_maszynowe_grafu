from operator import itemgetter
import time
elem = [9, 500, 1000, 100, 200, 300, 400, 750]
class ListaKrawedzi:
    def __init__(self, n):
        self.lista = []
        self.indegree = [0 for n in range(n+1)]
        self.rzad = n

    def add(self, v, u):
        self.lista.append((v,u))
        #self.lista.sort()

    def czy_istnieje(self, v, u):
        if (v, u) in self.lista:
            return True
        return False

    def get_nastepniki(self, v):
        w = []
        for krawedz in self.lista:
            if krawedz[0] == v:
                w.append(krawedz[1])
        return w

    def get_indegree(self):
        for krawedz in self.lista:
            self.indegree[krawedz[1]] += 1

    def start_Kahn(self):
        self.get_indegree()
        q = []
        vis = 0
        self.Ksort = []
        for i in range(1,self.rzad+1):
            if self.indegree[i] == 0:
                q.append(i)

        while len(q) > 0 and vis < self.rzad:
            v = q.pop(0)
            self.Ksort.append(v)
            nastepniki = self.get_nastepniki(v)
            for u in nastepniki:
                self.indegree[u] -= 1
            for i in range(1,self.rzad+1):
                if self.indegree[i] == 0 and i not in self.Ksort and i not in q:
                    q.append(i)
            vis += 1
        #print(self.Ksort)

    def DFS(self, v):
        if v not in self.Dsort:
            nast = self.get_nastepniki(v)
            for u in nast:
                self.DFS(u)
            self.Dsort.insert(0,v)

    def start_DFS(self):
        self.get_indegree()
        self.Dsort = []
        for i in range(1, self.rzad + 1):
            self.DFS(i)
        #print(self.Dsort)



for input_file in range(len(elem)):
    n = elem[input_file]
    graf = ListaKrawedzi(n)
    txt = "wejscie" + str(input_file) + ".txt"
    file = open(txt, "r")

    for line in file:
        pos_start, pos_stop = line.split()
        pos_start = int(pos_start)
        pos_stop = int(pos_stop)
        graf.add(pos_start, pos_stop)
    file.close()
    # --------------------------------------------------------------------------
    print(f"lk {int(n)} DFS {int(n * (n - 1) / 4)}", end=" ")
    begin = time.time()
    graf.start_DFS()  # DFS
    end = time.time()
    print(f"{end - begin}")

for input_file in range(len(elem)):
    n = elem[input_file]
    graf = ListaKrawedzi(n)
    txt = "wejscie" + str(input_file) + ".txt"
    file = open(txt, "r")

    for line in file:
        pos_start, pos_stop = line.split()
        pos_start = int(pos_start)
        pos_stop = int(pos_stop)
        graf.add(pos_start, pos_stop)
    file.close()
    # --------------------------------------------------------------------------
    print(f"lk {int(n)} Kahn {int(n * (n - 1) / 4)}", end=" ")
    begin = time.time()
    graf.start_Kahn()
    end = time.time()
    print(f"{end - begin}")