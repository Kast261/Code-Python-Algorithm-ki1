
import sys
sys.setrecursionlimit(200000)

def find_important(u, parent, graph, num, low, timer, important):
    timer[0] += 1
    num[u] = low[u] = timer[0]
    cnt = 0

    for v in graph[u]:
        if v == parent:
            continue

        if num[v] == 0:
            cnt += 1
            find_important(v, u, graph, num, low, timer, important)
            low[u] = min(low[u], low[v])

            if parent != -1 and low[v] >= num[u]:
                important[u] = True
        else:
            low[u] = min(low[u], num[v])

    if parent == -1 and cnt > 1:
        important[u] = True


def find_bridges(u, parent, graph, num, low, timer, bridges):
    timer[0] += 1
    num[u] = low[u] = timer[0]

    for v in graph[u]:
        if v == parent:
            continue

        if num[v] == 0:
            find_bridges(v, u, graph, num, low, timer, bridges)
            low[u] = min(low[u], low[v])

            if low[v] > num[u]:
                bridges.append((u, v))
        else:
            low[u] = min(low[u], num[v])


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 2:
        return

    n, m = data[0], data[1]

    if len(data) < 2 + 2 * m:
        return

    graph = [[] for _ in range(n + 1)]
    pos = 2

    for _ in range(m):
        u = data[pos]
        v = data[pos + 1]
        pos += 2
        graph[u].append(v)
        graph[v].append(u)

    num = [0] * (n + 1)
    low = [0] * (n + 1)
    timer = [0]
    bridges = []

    for u in range(1, n + 1):
        if num[u] == 0:
            find_bridges(u, -1, graph, num, low, timer, bridges)

    num = [0] * (n + 1)
    low = [0] * (n + 1)
    timer = [0]
    important = [False] * (n + 1)

    for u in range(1, n + 1):
        if num[u] == 0:
            find_important(u, -1, graph, num, low, timer, important)

    print(sum(important), len(bridges))


if __name__ == '__main__':
    solve()
