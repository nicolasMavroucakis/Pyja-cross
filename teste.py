rowsAmount = 20
columnsAmount = 20

base = { "enabled": False, "letter": "", "written": "", "words": [], "number": "" }
table = []

for i in range(columnsAmount):
    row = []
    for j in range(rowsAmount):
        row.append(base)

    table.append(row)

for i in table:
    print(i)
    print("\n")