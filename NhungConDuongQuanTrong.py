import sys
input = sys.stdin.readline
def dfs(u,parent,graph,num,low,timer,bridges):
    timer[0] += 1
    num[u] = low[u] = timer[0]

    for v in graph[u]:
        if v == parent:
            continue
        if num[v] == 0:
            dfs(v,u,graph,num,low,timer,bridges)
            low[u] = min(low[v],low[u])
            if low[v] > num[u]:
                bridges.append((min(u,v),max(u,v)))
        else:
            low[u] = min(low[u],num[v])
def solve():
    n,m = map(int,input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    num = [0] * (n + 1)
    low = [0] * (n + 1)
    timer = [0]
    bridges = []
    dfs(1,-1,graph,num,low,timer,bridges)
    bridges.sort()
    print(len(bridges))
    for u,v in bridges:
        print(u,v)


if __name__ == '__main__':
    solve()