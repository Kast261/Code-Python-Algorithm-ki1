from collections import deque

def bfs(start,graph,visited,t):
    queue = deque()
    queue.append(start)
    visited[start] = True
    best = start
    while queue:
        u = queue.popleft()
        if t[u] > t[best]:
            best = u
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)
    return best
def solve():
    n,m = map(int,input().split())
    t = [0] + list(map(int,input().split()))
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    ans = []
    visited = [False] * (n + 1)
    for i in range(1,n + 1):
        if not visited[i]:
            best = bfs(i,graph,visited,t)
            ans.append(best)
    ans.sort()
    print(len(ans))
    print(*ans)



if __name__ =='__main__':
    solve()