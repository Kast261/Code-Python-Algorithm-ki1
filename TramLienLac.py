import sys
input = sys.stdin.readline

def dfs(u,parent,graph,num,low,timer,important):
    timer[0] += 1
    num[u] = low[u] = timer[0]
    count = 0

    for v in graph[u]:
        if v == parent:
            continue
        if num[v] == 0:
            count += 1
            dfs(v,u,graph,num,low,timer,important)
            low[u] = min(low[u],low[v])
            if parent != -1 and low[v] >= num[u]:
                important[u] = True
        else:
            low[u] = min(low[u],num[v])
    if parent == -1 and count > 1:
        important[u] =  True
def solve():
    n,m = map(int,input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    num = [0] *(n + 1)
    low = [0] * (n + 1)
    timer = [0]
    important = [False] * (n + 1)
    dfs(1,-1,graph,num,low,timer,important)
    ans = []
    for u in range(1,n + 1):
        if important[u]:
            ans.append(u)
    print(len(ans))
    if ans:
        print(*ans)


if __name__ == '__main__':
    solve()