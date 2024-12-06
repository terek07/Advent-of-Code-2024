with open("input.txt", "r") as file:
    map = [line.strip() for line in file.readlines()]
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
while -1 < x < maxx and -1 < y < maxy :
  try:
    if facing % 4 == 0:
        if map[y - 1][x] == "#":
            facing += 1
            
        else:
            y -= 1
            print(x,y)
            positions.add((x, y))
    if facing % 4 == 1:
        if map[y][x + 1] == "#":
            facing += 1
            
        else:
            x += 1
            print(x,y)
            positions.add((x, y))
            
    if facing % 4 == 2:
        if map[y + 1][x] == "#":
            facing += 1
            
        else:
            y += 1
            print(x,y)
            positions.add((x, y))
            
    if facing % 4 == 3:
        if map[y][x - 1] == "#":
            facing += 1
            
        else:
            x -= 1
            print(x,y)
            positions.add((x, y))
  except:
    print(len(positions))
            
print(len(positions))
print(facing)
        
        
        
        
        
        
            