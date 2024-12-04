with open("input.txt", "r") as file:
    data = [line.strip() for line in file.readlines()]
    counter = 0
    for i, e in enumerate(data):
        for j, c in enumerate(e):
            if c == "X":
                try:
                    if e[j + 1] == "M" and e[j + 2] == "A" and e[j + 3] == "S":
                        counter += 1
                except IndexError:
                    pass
                try:
                    if data[i + 1][j] == "M" and data[i + 2][j] == "A" and data[i + 3][j] == "S":
                        counter += 1
                except IndexError:
                    pass
                try:
                    if data[i + 1][j + 1] == "M" and data[i + 2][j + 2] == "A" and data[i + 3][j + 3] == "S":
                        counter += 1
                except IndexError:
                    pass
                try:
                    if i >= 3 and data[i - 1][j + 1] == "M" and data[i - 2][j + 2] == "A" and data[i - 3][j + 3] == "S":
                        counter += 1
                except IndexError:
                    pass
            if c == "S":
                try:
                    if e[j + 1] == "A" and e[j + 2] == "M" and e[j + 3] == "X":
                        counter += 1
                except IndexError:
                    pass
                try:
                    if data[i + 1][j] == "A" and data[i + 2][j] == "M" and data[i + 3][j] == "X":
                        counter += 1
                except IndexError:
                    pass
                try:
                    if data[i + 1][j + 1] == "A" and data[i + 2][j + 2] == "M" and data[i + 3][j + 3] == "X":
                        counter += 1
                except IndexError:
                    pass
                try:
                    if i >= 3 and data[i - 1][j + 1] == "A" and data[i - 2][j + 2] == "M" and data[i - 3][j + 3] == "X":
                        counter += 1
                except IndexError:
                    pass
    print(counter)
