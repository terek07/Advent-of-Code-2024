#task: https://adventofcode.com/2024/day/10
with open("input.txt", "r") as file:
    map = [list(line.strip()) for line in file.readlines()]

heads = set()
for x, line in enumerate(map):
    for y, num in enumerate(line):
        if num == "0":
            heads.add((x, y))

score = 0

def main(visited, x, y):
    if (x, y) in visited:
        return 0
    visited.add((x, y))
    if map[x][y] == "9":
        return 1
    count = 0
    if x + 1 < len(map) and map[x + 1][y] == str(int(map[x][y]) + 1):
        count += main(visited, x + 1, y)
    if x - 1 >= 0 and map[x - 1][y] == str(int(map[x][y]) + 1):
        count += main(visited, x - 1, y)
    if y + 1 < len(map[0]) and map[x][y + 1] == str(int(map[x][y]) + 1):
        count += main(visited, x, y + 1)
    if y - 1 >= 0 and map[x][y - 1] == str(int(map[x][y]) + 1):
        count += main(visited, x, y - 1)
    visited.remove((x, y))
    return count

for e in heads:
    score += main(set(), e[0], e[1])

print(score)# task 1 solution