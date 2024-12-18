with open("input.txt", "r") as file:
    map = [list(line.strip()) for line in file.readlines()]
heads = set()
for x, line in enumerate(map):
    for y, num in enumerate(line):
        if num == "0":
            heads.add((x, y))
sum1 = {}
def main(x, y):
    if map[x][y] == "9":
        sum1.append(1)
    try:
        if map[x + 1][y + 1] == int(map[x][y]) + 1:
            main(x + 1, y + 1)
    except IndexError:
        pass
    try:
        if map[x - 1][y + 1] == int(map[x][y]) + 1:
            main(x - 1, y + 1)
    except IndexError:
        pass
    try:
        if map[x + 1][y - 1] == int(map[x][y]) + 1:
            main(x + 1, y - 1)
    except IndexError:
        pass
    try:
        if map[x - 1][y - 1] == int(map[x][y]) + 1:
            main(x - 1, y - 1)
    except IndexError:
        pass
for e in heads:
    main(e[0], e[1])
print(sum(sum1))