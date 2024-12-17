#task: https://adventofcode.com/2024/day/16

#My own solution - works with small example input but causes "RecursionError: maximum recursion depth exceeded" on actual input

with open("input.txt", "r") as file:
    data = [e.strip() for e in file.readlines()]

sx, end = 0, 0
sfacing = "east"
for i, line in enumerate(data): #gets staring coordinates and end coordinates
    if 'S' in line:
        sx, sy = (i, line.index("S"))
    if 'E' in line:
        end = (i, line.index("E"))
    if sx and end:
        break

scores = []
visiteds = []

def main(score, x, y, facing, visited):
    if (x, y, facing) in visited:
        return
    visited.add((x, y, facing))
    if x == end[0] and y == end[1]:
        scores.append(score)
        visiteds.append(visited)
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

main(0, sx, sy, sfacing, set())
print(min(scores)) # task 1 solution
result2 = set()
for score, visited in zip(scores, visiteds):
    if score == min(scores):
        for x, y, _ in visited:
            result2.add((x, y))
print(len(result2)) #task 2 solution
