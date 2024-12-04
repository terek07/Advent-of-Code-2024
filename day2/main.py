#task: https://adventofcode.com/2024/day/2
with open("input.txt", "r") as file:
    data = [line.split() for line in file.readlines()]
    # my second solution task 1
    print(
        sum(  # sum of safe reports in decreasing order
            1 for e in data if all(
                0 < int(e[i - 1]) - int(e[i]) <= 3 for i in range(1, len(e))
            )
        )
        +
        sum(  # sum of safe reports in increasing order
            1 for e in data if all(
                0 < int(e[i]) - int(e[i - 1]) <= 3 for i in range(1, len(e))
            )
        )
    )

    counter = 0
    for e in data:
        safe = True
        for i in range(1, len(e)): #checks if is safe for decreasing order
            if not 0 < int(e[i - 1]) - int(e[i]) <=3:
                safe = False
                break
        if not safe: #checks if is safe after removing 1 number for decreasing order
            for i in range(len(e)):
                temp = e[ : i] + e[i + 1 : ]
                safeTemp = True
                for i in range(1, len(temp)):
                    if not 0 < int(temp[i - 1]) - int(temp[i]) <= 3:
                        safeTemp = False
                        break
                if safeTemp:
                    safe = True
                    break
        if safe:
            counter += 1
        safe = True
        for i in range(1, len(e)): #checks if is safe for increasing order
            if not 0 < int(e[i]) - int(e[i - 1]) <=3:
                safe = False
                break
        if not safe: #checks if is safe after removing 1 number for increasing order
            for i in range(len(e)):
                temp = e[ : i] + e[i + 1 : ]
                safeTemp = True
                for i in range(1, len(temp)):
                    if not 0 < int(temp[i]) - int(temp[i - 1]) <= 3:
                        safeTemp = False
                        break
                if safeTemp:
                    safe = True
                    break
        if safe:
            counter += 1

    print(counter) #result task 2
