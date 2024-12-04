#task: https://adventofcode.com/2024/day/3
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
    
    
    splited = data.split("do()")
    dos = []
    result = []
    for e in splited:
        dos = e.split("don't()")[0] #everything between do() and don't()
        correct = re.findall(r"mul\(\d{1,3},\d{1,3}\)", dos)  # finds all  mul(x, y)
        for el in correct:
            i = el.index(",")
            x = int(el[4:i])
            y = int(el[i + 1:-1])
            result.append(x * y)
    print(sum(result)) #task 2 solution
