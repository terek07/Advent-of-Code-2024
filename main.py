with open("input.txt", "r") as file:
    map = [list(line.strip()) for line in file.readlines()]
for i, line in enumerate(map):
    print(line)
    maxx = len(line)
    if "^" in line:
        x = line.index("^")
        y = i
        break
maxy = len(map)
print(x, y)
facing = 0
positions = set()

loops = 0
for i in range(len(map)):
    for j in range(len(map[i])):
        breaker = false
        newmap = map[:]
        newmap[i][j] = "#"
        positions2 = []
        while -1 < x < maxx and -1 < y < maxy :
            if (x, y, facing) in positions2:
                loops += 1;
                breaker = True
                break
            if facing % 4 == 0:
                if newmap[y - 1][x] == "#":
                    facing += 1
            
                else:
                    y -= 1
                    print(x,y)
                    positions.add((x, y))
                    positions2.append((x, y, facing))
            if facing % 4 == 1:
                if newmap[y][x + 1] == "#":
                    facing += 1
            
                else:
                    x += 1
                    print(x,y)
                    positions.add((x, y))
                
            if facing % 4 == 2:
                if newmap[y + 1][x] == "#":
                    facing += 1
                
                else:
                    y += 1
                    print(x,y)
                    positions.add((x, y))
            
            if facing % 4 == 3:
                if newmap[y][x - 1] == "#":
                    facing += 1
            
                else:
                    x -= 1
                    print(x,y)
                    positions.add((x, y))
        if breaker:
            break
            
print(len(positions))
print(facing)
