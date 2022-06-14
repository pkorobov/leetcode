from collections import deque, defaultdict


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        if len(connections) < n - 1:
            return -1

        g = defaultdict(list)
        for conn in connections:
            node, neighbour = conn
            g[node].append(neighbour)
            g[neighbour].append(node)

        self.visited = set()
        components = 0

        for i in range(n):
            if i not in self.visited:
                components += 1
                self.bfs(g, i)

        return components - 1

    def bfs(self, graph, start):
        queue = deque()
        queue.append(start)
        self.visited.add(start)

        while len(queue) > 0:
            cur = queue.popleft()
            for nxt in graph[cur]:
                if nxt not in self.visited:
                    queue.append(nxt)
                    self.visited.add(nxt)
