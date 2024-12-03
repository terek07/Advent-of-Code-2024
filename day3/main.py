import re


with open("input.txt", "r") as file:
    data = file.read()
    correct = re.findall(r"mul\(\d{1,3},\d{1,3}\)", data) #finds all  mul(x, y)
    result = []
    for e in correct:
        i = e.index(",")
        x = int(e[4:i])
        y = int(e[i+1:-1])
        result.append(x * y) #multiplies x * y
    print(sum(result)) #task 1 solution