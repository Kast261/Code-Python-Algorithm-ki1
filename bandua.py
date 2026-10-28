import sys

def solve():
    input = sys.stdin.readline
    n = int(input())
    stack = []
    ans = 0

    for i in range(n + 1):
        h = int(input()) if i < n else 0
        start = i

        while stack and stack[-1][1] > h:
            pos, cao = stack.pop()
            width = i - pos

            if width >= cao:
                ans = max(ans, cao)

            start = pos

        if not stack or stack[-1][1] < h:
            stack.append((start, h))

    print(ans)

if __name__ == "__main__":
    solve()