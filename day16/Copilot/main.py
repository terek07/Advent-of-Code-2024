# Working solution with help from Github Copilot

import heapq

with open('input.txt', 'r') as file:
    data = [e.strip() for e in file.readlines()]

sx, sy, end = 0, 0, 0
for i, line in enumerate(data):
    if 'S' in line:
        sx, sy = i, line.index('S')
    if 'E' in line:
        end = (i, line.index('E'))
    if sx and end:
        break

def dijkstra(start, end):
    heap = [(0, start[0], start[1], 'east')]
    visited = set()
    directions = {
        'east': [(0, 1, 'east', 1), (-1, 0, 'north', 1001), (1, 0, 'south', 1001)],
        'south': [(1, 0, 'south', 1), (0, 1, 'east', 1001), (0, -1, 'west', 1001)],
        'west': [(0, -1, 'west', 1), (-1, 0, 'north', 1001), (1, 0, 'south', 1001)],
        'north': [(-1, 0, 'north', 1), (0, -1, 'west', 1001), (0, 1, 'east', 1001)]
    }

    while heap:
        score, x, y, facing = heapq.heappop(heap)

        if (x, y) == end:
            return score

        if (x, y, facing) in visited:
            continue
        visited.add((x, y, facing))

        for dx, dy, new_facing, cost in directions[facing]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(data) and 0 <= ny < len(data[0]) and data[nx][ny] in ('.', 'E'):
                heapq.heappush(heap, (score + cost, nx, ny, new_facing))

    return -1  # If no path is found

result = dijkstra((sx, sy), end)
print(result)