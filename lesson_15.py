class Graph:
    def __init__(self, N: int):
        self.N = N
        self.c = [0] * N
        self.v = [[] for _ in range(N)]

    def dfs(self, x, component_id: int) -> None:
        """Рекурсивный поиск в одной компоненте связности в неориентированном графе"""
        self.c[x] = component_id  # присвоение номера компоненты по индексу элемента
        for i in range(len(self.v[x])):  # просмотр соседей
            next_v = self.v[x][i]  # сосед
            # проверка(просмотрен или нет) по компоненте
            if self.c[next_v] == 0:
                # рекурсивный запуск от не просмотренного соседа
                self.dfs(next_v, component_id)


N = 8
g = Graph(N)

g.v[0].append(1)

g.v[1].append(0)
g.v[1].append(2)

g.v[2].append(1)

g.v[3].append(4)

g.v[4].append(3)

g.v[5].append(6)
g.v[6].append(5)
g.v[6].append(7)
g.v[7].append(6)


last_component = 0
for i in range(N):  # просмотр всех узлов графа по индексам
    if g.c[i] == 0:  # если узел не просмотрен значит он в другой компоненте
        last_component += 1  # номер компоненты
        print(f"узел {i} компонента {last_component}")
        g.dfs(i, last_component)  # запуск поиска всех узлов кмпоненты
