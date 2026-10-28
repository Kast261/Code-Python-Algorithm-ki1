import sys

def build(n):
    MAX = 100000
    diff = [0] * (MAX + 2)

    for _ in range(n):
        l, r = map(int, input().split())
        diff[l] += 1
        diff[r + 1] -= 1

    dem = [0] * (MAX + 1)

    for i in range(1, MAX + 1):
        dem[i] = dem[i - 1] + diff[i]

    st = [dem[:]]
    k = MAX.bit_length()

    for j in range(1, k):
        prev = st[j - 1]
        cur = [0] * (MAX + 1)
        length = 1 << (j - 1)

        for i in range(1, MAX - (1 << j) + 2):
            cur[i] = max(prev[i], prev[i + length])

        st.append(cur)

    return st


def solve():
    input = sys.stdin.readline
    n, q = map(int, input().split())

    st = build(n)

    for _ in range(q):
        a, b = map(int, input().split())
        j = (b - a + 1).bit_length() - 1
        length = 1 << j

        ans = max(st[j][a], st[j][b - length + 1])
        print(ans)


if __name__ == "__main__":
    solve()