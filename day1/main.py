#task: https://adventofcode.com/2024/day/1
with open("input.txt","r") as file:
    data = file.readlines()
    print(data)
    left = []
    right = []
    for e in data:
        leftLine = e[:5]
        rightLine = e[8:-1]
        left.append(leftLine)
        right.append(rightLine)
    print(sum([int(e) * right.count(e) for e in left]))   #task 2 solution
    left.sort()
    right.sort()
    print(sum([abs(int(l) - int(r)) for l, r in zip(left, right)]))   #task 1 solution

