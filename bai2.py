
import sys
input = sys.stdin.readline

MAX = 100000

def build(n):
    diff = [0] * (MAX + 2)

    for _ in range(n):
        l, r = map(int, input().split())
        diff[l] += 1
        diff[r + 1] -= 1

    dem = [0] * (MAX + 1)

    for i in range(1, MAX + 1):
        dem[i] = dem[i - 1] + diff[i]

    return dem[1:]


def tao_cay(a, tree, node, left, right):
    if left == right:
        tree[node] = a[left]
        return

    mid = (left + right) // 2

    tao_cay(a, tree, node * 2, left, mid)
    tao_cay(a, tree, node * 2 + 1, mid + 1, right)

    tree[node] = max(tree[node * 2], tree[node * 2 + 1])


def truy_van(tree, node, left, right, a, b):
    if b < left or right < a:
        return 0

    if a <= left and right <= b:
        return tree[node]

    mid = (left + right) // 2

    trai = truy_van(tree, node * 2, left, mid, a, b)
    phai = truy_van(tree, node * 2 + 1, mid + 1, right, a, b)

    return max(trai, phai)


def solve():
    n, q = map(int, input().split())

    dem = build(n)

    tree = [0] * (4 * MAX)
    tao_cay(dem, tree, 1, 0, MAX - 1)

    for _ in range(q):
        a, b = map(int, input().split())
        print(truy_van(tree, 1, 0, MAX - 1, a - 1, b - 1))


if __name__ == "__main__":
    solve()
