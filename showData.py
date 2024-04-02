def showData(students:dict[int,dict[str,str or float]]):
    lines = []

    lenNames = []
    for student in students:
        lenNames.append(len(students[student]["name"]))
    maxLenName = max(lenNames)

    lines.append("_" * (maxLenName + 23))
    lines.append(f"| ID        | Name{(maxLenName - 4) * ' ' } | GPA  |")
    for student in students:
        lines.append(f"| {student:8d} | {students[student]['name']}{(maxLenName - len(students[student]['name'])) * ' ' } | {students[student]['gpa']:4.2f} |")
    lines.append("_" * (maxLenName + 23))

    for line in lines:
        print(line)
