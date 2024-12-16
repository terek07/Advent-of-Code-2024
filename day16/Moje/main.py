#My own solution - work with small example input but causes "RecursionError: maximum recursion depth exceeded" on actual input

with open("input.txt", "r") as file:
    data = [e.strip() for e in file.readlines()]

sx, end = 0, 0
sfacing = "east"
for i, line in enumerate(data):
    if 'S' in line:
        sx, sy = (i, line.index("S"))
    if 'E' in line:
        end = (i, line.index("E"))
    if sx and end:
        break

sscore = 0
scores = []

def main(score, x, y, facing, visited):
    if (x, y, facing) in visited:
        return
    visited.add((x, y, facing))
    if x == end[0] and y == end[1]:
        scores.append(score)
        # print(score)
        return
    if facing == "east":
        if data[x][y + 1] in ('.', 'E'):
            main(score + 1, x, y + 1, facing, visited.copy())
        if data[x - 1][y] in ('.', 'E'):
            main(score + 1001, x - 1, y, "north", visited.copy())
        if data[x + 1][y] in ('.', 'E'):
            main(score + 1001, x + 1, y, "south", visited.copy())
    elif facing == "south":
        if data[x + 1][y] in ('.', 'E'):
            main(score + 1, x + 1, y, facing, visited.copy())
        if data[x][y + 1] in ('.', 'E'):
            main(score + 1001, x, y + 1, "east", visited.copy())
        if data[x][y - 1] in ('.', 'E'):
            main(score + 1001, x, y - 1, "west", visited.copy())
    elif facing == "west":
        if data[x][y - 1] in ('.', 'E'):
            main(score + 1, x, y - 1, facing, visited.copy())
        if data[x - 1][y] in ('.', 'E'):
            main(score + 1001, x - 1, y, "north", visited.copy())
        if data[x + 1][y] in ('.', 'E'):
            main(score + 1001, x + 1, y, "south", visited.copy())
    elif facing == "north":
        if data[x - 1][y] in ('.', 'E'):
            main(score + 1, x - 1, y, facing, visited.copy())
        if data[x][y - 1] in ('.', 'E'):
            main(score + 1001, x, y - 1, "west", visited.copy())
        if data[x][y + 1] in ('.', 'E'):
            main(score + 1001, x, y + 1, "east", visited.copy())

main(sscore, sx, sy, sfacing, set())
print(min(scores))