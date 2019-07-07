"""
E - dict(<V> : [<V>, <V>, ...])
Ключ - строка, идентифицирующая вершину графа
значение - список вершин, достижимых из данной

Сделать так, чтобы по графу можно было итерироваться(обходом в ширину)

"""
from collections import deque


class GraphIterator:
    def __init__(self, graph):
        self.E = graph.E
        self._used = set()
        self._q = deque()
        if self.E:
            v = list(self.E)[0]
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


class Graph:
    def __init__(self, E):
        self.E = E

    def __iter__(self):
        return GraphIterator(self)


if __name__ == '__main__':

    E = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A']}
    graph = Graph(E)

    for vertice in graph:
        print(vertice)
    for i in graph:
        for j in graph:
            print(i,j)