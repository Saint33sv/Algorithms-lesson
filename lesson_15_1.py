class Graph:
    def __init__(self, N: int):
        self.N = N
        self.c = [0] * N
        self.v = [[] for _ in range(N)]
        self.top_sort = []
        self.has_cycle = False

    def dfs(self, x: int) -> None:
        """Топологическая сортировка"""
        self.c[x] = 1
        for i in range(len(self.v[x])):
            next_v = self.v[x][i]
            if self.c[next_v] == 0:
                self.dfs(next_v)
            else:
                if self.c[next_v] == 1:
                    self.has_cycle = True
                    return
        self.c[x] = 2
        self.top_sort.append(x)


cnt = 5
dictionary = ['wrt', 'wrf', 'er', 'ett', 'rftt']
g = Graph(26)
for i in range(0, cnt-1):
    for j in range(0, len(dictionary[i])):
        if j >= len(dictionary[i]):  # если строчки разной длины
            print('No answer')  # лексиграфическая сортировка не коректна
            break
        if dictionary[i][j] != dictionary[i+1][j]:  # находим не совпадающие символы
            start = dictionary[i][j]  # с какого символа
            end = dictionary[i+1][j]  # в какой символ
            g.v[ord(start) - ord('a')].append(ord(end) -
                                              ord('a'))  # ребро от start к end
            break
for i in range(0, g.N):
    if g.c[i] == 0:
        g.dfs(i)
list.reverse(g.top_sort)
if g.has_cycle:
    print('No answer')
else:
    for i in range(0, g.N):
        print(chr(g.top_sort[i] + ord('a')), end='')
