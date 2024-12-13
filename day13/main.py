import time
start = time.time()
with open("input.txt", "r") as file:
    tokens = 0
    for _ in range(320):
        a = file.readline()
        ax = int(a[a.index("X") + 2 : a.index(",")])
        ay = int(a[a.index("Y") + 2 :])
        
        b = file.readline()
        bx = int(b[b.index("X") + 2 : b.index(",")])
        by = int(b[b.index("Y") + 2 :])
        
        p = file.readline()
        px = int(p[p.index("X") + 2 : p.index(",")])
        py = int(p[p.index("Y") + 2 :])
        _ = file.readline()
        
        for i in range(101):
            breaker = False
            for j in range(101):
                # print(i, j, i * ax + j * bx == px, i * ay + j * by == py)
                if i * ax + j * bx == px and i * ay + j * by == py:
                    tokens = tokens + j + i * 3
                    print(i, j)
            if breaker:
                break
    print(tokens)
    print(time.time() - start)