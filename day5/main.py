with open("input.txt", "r") as file:
    data = [e.strip() for e in file.readlines()]
with open("rules.txt", "r") as file:
    rules = [e.strip() for e in file.readlines()]
left = [e[0 : 2] for e in rules]
right = [e[3 : 5] for e in rules]
result = []
for line in data:
    line = line.split(",")
    correct = True
    for l, r in zip(left, right):
        if l in line and r in line:
            if line.index(l) >= line.index(r):
                    correct = False
                    break

    if correct:
        print(line)
        print(line[len(line) // 2 + 1])
        result.append(int(line[len(line) // 2]))
# print(rules)
print(left)
# print(right)
print(data)
print(result)
print(sum(result))
