def find(x,parent):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x
def union(u,v,parent,size):
    u = find(u,parent)
    v = find(v,parent)
    if u == v:
        return False
    if size[u] < size[v]:
        u,v = v,u
    parent[v] = u
    size[u] += size[v]
    return True
def solve():
    n,m = map(int,input().split())
    arr = []
    for _ in range(m):
        u,v,w,t = input().split()
        arr.append((int(u),int(v),int(w),t))
    size = [1] * (n + 1)
    parent = list(range(n + 1))
    ans = 0
    cnt = 1
    for u,v,w,t in arr:
        if t == 'B':
            if not union(u,v,parent,size):
                print(-1)
                return
            ans += w
            cnt += 1
    arr.sort(key=lambda x : x[2])
    for u,v,w,t in arr:
        if t == 'N':
            if union(u,v,parent,size):
                ans += w
                cnt += 1
    if cnt == n:
        print(ans)
    else:
        print(-1)

if __name__ == '__main__':
    solve()