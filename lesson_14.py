from typing import List


class Graph:
    def __init__(self, v):
        self.v = v
        self.adj = [[] for _ in range(v)]

    def addEdge(self, v, w: int) -> None:
        self.adj[v].append(w)

    def bfs(self, vertex: int) -> None:
        seen = set()
        queue = []
        seen.add(vertex)
        queue.append(vertex)
        while queue:
            current = queue[0]
            queue.remove(queue[0])
            print(f"Узел {current}")
            for i in self.adj[current]:
                if i not in seen:
                    seen.add(i)
                    queue.append(i)

    def dfs(self, vertex: int) -> None:
        seen = set()
        stack = []
        seen.add(vertex)
        stack.append(vertex)
        while stack:
            current = stack.pop()
            print(f"Узел {current}")
            for i in self.adj[current]:
                if i not in seen:
                    seen.add(i)
                    stack.append(i)

    def dfsUtil(self, v: int, seen: set) -> None:
        seen.add(v)
        print(v)
        for i in self.adj[v]:
            if i not in seen:
                self.dfsUtil(i, seen)

    def dfs_recursive(self, vertex: int) -> None:
        seen = set()
        self.dfsUtil(vertex, seen)


class Solution:

    def canVisitAllRooms(self, rooms: List[int]) -> bool:
        seen = set()
        queue = []

        seen.add(0)
        queue.append(0)

        while queue:
            opened_room = queue[0]
            queue.remove(queue[0])

            for i in rooms[opened_room]:
                if i not in seen:
                    seen.add(i)
                    queue.append(i)
        return len(seen) == len(rooms)


solution = Solution()
rooms = []

keys0 = []
keys0.append(1)
rooms.append(keys0)

keys1 = []
keys1.append(2)
rooms.append(keys1)

keys2 = []
rooms.append(keys2)

print(solution.canVisitAllRooms(rooms))

rooms = []

keys0 = []
keys0.append(2)
keys0.append(3)
rooms.append(keys0)

keys1 = []
keys1.append(1)
rooms.append(keys1)

keys2 = []
keys2.append(0)
keys2.append(2)
keys2.append(3)
rooms.append(keys2)

keys3 = []
keys3.append(2)
rooms.append(keys3)

print(solution.canVisitAllRooms(rooms))
