with open("input.txt", "r") as file:
    data = [e.strip() for e in file.readlines()]
with open("rules.txt", "r") as file:
    rules = [e.strip() for e in file.readlines()]
left = [e[0 : 2] for e in rules]
right = [e[3 : 5] for e in rules]
result = []
for line in data:
    correct = True
    for l, r in zip(left, right):
        if l in line and r in line:
            for i, char in enumerate(line.split(",")):
                try:
                    if line.index(r) > i:
                        correct = False
                        break
                except ValueError:
                    pass
    if correct:
        result.append(line)
print(rules)
print(data)
print(result)
