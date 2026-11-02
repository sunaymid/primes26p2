import random 

def checkpath(grid,n):
    s = []
    visited = []
    for _ in range(n):
        l = []
        for _ in range(n):
            l.append(False)
        visited.append(l)
    for row in range(n):
        if grid[row][0] == 1:
            s.append((row, 0))
            visited[row][0] = True
    while len(s)>0:
        (r,c)=s.pop()
        if c == n-1:
            return True
        for dx,dy in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
            if 0 <= dx < n and 0 <= dy < n:
                if grid[dx][dy] == 1 and not visited[dx][dy]:
                    visited[dx][dy] = True
                    s.append((dx, dy))
    return False 

def estimatetheta(n,p,m):
    count = 0
    for _ in range(m):
        grid = []
        for _ in range(n):
            row = []
            for _ in range(n):
                if random.random() < p:
                    row.append(1)
                else: 
                    row.append(0)
            grid.append(row)
        if checkpath(grid, n):
            count += 1
    return count / m

def exact1(p):
    return p

def exact2(p):
    return 2*(p**2) - p**4

M = 738
testcases = [
    (1, 0.3, exact1(0.3)),
    (1, 0.5, exact1(0.5)),
    (1, 0.8, exact1(0.8)),
    (2, 0.3, exact2(0.3)),
    (2, 0.5, exact2(0.5)),
    (2, 0.8, exact2(0.8))
]

for n, p, exact in testcases:
    est = estimatetheta(n, p, M)
    err = abs(est-exact)
    print(n,p,exact,est,err)