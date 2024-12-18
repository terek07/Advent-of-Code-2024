#task: https://adventofcode.com/2024/day/7
with open("input.txt", "r") as file:
    data = [line.strip() for line in file.readlines()]
sum1 = set()
sum2 = set()
def task1(i, x, e, result):
    if result == x:
        sum1.add(result)
    elif result < x and i < len(e):
        for sign in range(2):
            task1(i + 1, x, e, result + e[i]) if sign else task1(i + 1, x, e, result * e[i])
def task2(i, x, e, result):
    if result == x:
        sum2.add(result)
    elif result < x and i < len(e):
        for sign in range(3):
            if sign == 0:
                task2(i + 1, x, e, result + e[i])
            elif sign == 1:
                task2(i + 1, x, e, result * e[i])
            else:
                task2(i + 1, x, e, int(str(result) + str(e[i])))
for e in data:
    x = int(e[ : e.index(":")])
    calcs = e[e.index(":")+1:].split()
    calcs = [int(x) for x in calcs]
    task1(1, x, calcs, int(calcs[0]))
    task2(1, x, calcs, int(calcs[0]))
print(sum(sum1)) #task 1 solution
print(sum(sum2)) #task 2 solution

