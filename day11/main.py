stones = [2701, 64945, 0, 9959979, 93, 781524, 620, 1]

for _ in range(75):
    new = []
    for e in stones:
        e_str = str(e)
        if e_str == "0":
            new.append("1")
        elif len(e_str) % 2 == 0:
            mid = len(e_str) // 2
            new.append(e_str[:mid])
            r = e_str[mid:].lstrip("0")
            new.append(r if r else "0")
        else:
            new.append(str(int(e_str) * 2024))
    stones = new

print(len(stones))
