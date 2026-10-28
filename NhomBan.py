import sys
from collections import deque
input = sys.stdin.readline
def bfs(start,graph,visited):
    queue = deque()
    queue.append(start)
    visited[start] = True
    dem = 0
    while queue:
        u = queue.popleft()
        dem += 1
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)
    return dem


def solve():
    n,m = map(int,input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    visited = [False] * (n + 1)
    k = 0
    res = 0
    for i in range(1,n + 1):
        if not visited[i]:
            k += 1
            dem = bfs(i,graph,visited)
            res = max(dem,res)
    print(k)
    print(res)



if __name__ == '__main__':
    solve()