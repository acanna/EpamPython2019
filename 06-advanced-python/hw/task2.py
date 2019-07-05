"""
E - dict(<V> : [<V>, <V>, ...])
Ключ - строка, идентифицирующая вершину графа
значение - список вершин, достижимых из данной

Сделать так, чтобы по графу можно было итерироваться(обходом в ширину)

"""
from collections import deque


class Graph:
    def __init__(self, E):
        self.E = E
        self._used = set()
        self._q = deque()
        if E:
            v = list(E)[0]
            self._used.add(v)
            self._q.append(v)

    def __iter__(self):
        return self

    def __next__(self):
        if not self._q:
            raise StopIteration
        v = self._q.popleft()
        for u in self.E[v]:
            if u not in self._used:
                self._q.append(u)
                self._used.add(u)
        return v

if __name__ == '__main__':

    E = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A']}
    graph = Graph(E)

    for vertice in graph:
        print(vertice)
