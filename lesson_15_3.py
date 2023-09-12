class Graph:
    def __init__(self, N: int):
        self.N = N  # количество вершин
        # список дистанций до вершин(изначально бесконечность потом поновляется)
        self.d = [10000000] * N
        # список булевых значений посетили или нет вершину
        self.used = [False] * N
        self.v = [[] for _ in range(N)]  # список рёбер
        self.w = [[] for _ in range(N)]  # список весов рёбер


"""Алгоритм Дейкстры"""
N = 100
g = Graph(N)

for i in range(N):
    mx = 10000001
    ind = 0
    for j in range(N):
        if not g.used[j]:
            if g.d[j] < mx:
                ind = j
                mx = g.d[j]
    g.used[ind] = True
    for j in range(len(g.v[ind])):
        next = g.v[ind][j]
        nw = g.d[ind] + g.w[ind][j]
        if g.d[next] > nw:
            g.d[next] = nw

"""С использованием очереди с приоритетами:"""


class Data:
    def __init__(self, w, ind: int):
        self.w = w
        self.ind = ind


N = 100
gg = Graph(N)


start = 0
gg.d[start] = 0
q = []
q.append(Data(0, start))

while q:
    q.sort(key=lambda x: x.w)  # сортируем очередь вершин по весу рёбер
    ind = q[0].ind
    d = q[0].w
    q.pop(0)  # выбираем первую вершину и удаляем её из очереди
    if g.used[ind]:  # проверка просмотрена ли вершина ранее
        continue
    g.used[ind] = True  # если нет тогда помечаем её как просмотренную
    for i in range(len(g.v[ind])):  # просмотр соседей вершины
        next = g.v[ind][i]  # сосед
        nd = d + g.w[ind][i]  # записываем новую дистанцию до соседа
        if g.d[next] > nd:  # если растояние до вершины next больше чем новое
            g.d[next] = nd  # обновляем растояние до вершины next
            # добавляем вершину в очередь с приоритетом
            q.append(Data(nd, next))
