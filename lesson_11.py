class Node:
    def __init__(self, id):
        self.id = id
        self.v = []


class Edge:
    def __init__(self):
        self.a = a
        self.b = b


n = 5  # количество вершин
e = []  # cписок ребер между (Edge)
ar = []  # список вершин

# хранение вершин в виде отдельных обьектов со ссылками
for i in range(n):
    ar.append(Node(i))

for i in range(len(e)):
    a = e[i].a
    b = e[i].b
    ar[a].v.append(b)
    ar[b].v.append(a)

# Второй вариант. Хранение массива со списками соседей (индексами) для каждой
# вершины (переменные n и e остаются как есть переменная ar заменяется на v )...

v = []  # список соседей i-того элемента
for i in range(n):
    v.append([])

for i in range(len(e)):
    a = e[i].a
    b = e[i].b
    v[a].append(b)
    v[b].append(a)


def dfsl(x, depth, p: int) -> None:  # int
    """Функция обхода в глубину где: 
    x - вершина с которой старрует функция
    depth - глуьина вершины
    p - предок вершины"""
    d[x] = depth
    # weight = 1 # для подсчета количества вершин в поддереве добавить все закомментированные строки
    for i in range(len(v[x])):
        a = v[x][i]
        if a == p:
            continue
        dfsl(a, depth+1, x)

        # weight += dfsl(a, depth+1, x)
 #  w[x] = weight
#   return weight


# Функция, проверяющая, лежит ли вершина в поддереве другой вершины:
t_in = [0]*n
t_out = [0]*n
T = 0


def dfsl(x, depth, p: int) -> None:
    d[x] = depth
    t_in[x] = T
    T += 1
    for i in range(len(v[x])):
        a = v[x][i]
        if a == p:
            continue
        dfsl(a, depth+1, x)
    t_out[x] = T
    T += 1


def dfs(x: int) -> None:
    dfsl(x, 0, -1)


def is_in_subtree(a, b: int) -> bool:
    if t_in[b] < t_in[a]:
        return False
    if t_out[b] > t_out[a]:
        return False
    return True


# Поиск наименьшего общего предка:
order = []
first = []
last = []


def dfsl2(x, depth, p: int) -> None:
    d[x] = depth
    first[x] = len(order)
    order.append(x)
    for i in range(len(v[x])):
        a = v[x][i]
        if a == p:
            continue
        dfsl2(a, depth+1, x)
        order.append(x)
    last[x] = len(order)
    order.append(x)


def get_lca(a, b: int) -> int:
    l = first[a]
    if first[b] < l:
        l = first[b]
    r = last[a]
    if last[b] > r:
        r = last[b]
    ans = 0
    D = d[a]
    for i in range(l, r):
        if d[order[i] < D]:
            ans = order[i]
            D = d[ans]
    return ans


root = 3
w = []
d = []  # глубина елемента по индексу
dfs(root)


def bfs(x: int) -> None:
    """Поиск в ширину
    Пример реализации алгоритма с использованием двух массивов:"""
    cur = []
    next_n = []
    next_n.append(x)
    D = 0
    visited = [False] * n
    while next_n:
        cur = next_n
        next_n = []
        for i in range(len(cur)):
            a = cur[i]
            visited[a] = True
            d[a] = D
            for j in range(len(v[a])):  # перебераем соседей а
                b = v[a][j]
                if visited[b]:
                    continue
                next_n.append(b)
        D += 1
