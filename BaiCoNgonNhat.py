import sys
from collections import deque

input = sys.stdin.readline

def bfs(i, j, a, r, c, visited):
    queue = deque([(i, j)])
    visited[i][j] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < r and 0 <= ny < c:
                if a[nx][ny] == '#' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

def solve():
    r, c = map(int, input().split())
    a = [input().strip() for _ in range(r)]

    visited = [[False] * c for _ in range(r)]
    dem = 0

    for i in range(r):
        for j in range(c):
            if a[i][j] == '#' and not visited[i][j]:
                dem += 1
                bfs(i, j, a, r, c, visited)

    print(dem)

if __name__ == '__main__':
    solve()
