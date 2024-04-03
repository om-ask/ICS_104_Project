def show_data(students: dict[int, dict[str, str or float]]) -> bool:
    lines = []

    len_names = []
    for student in students:
        len_names.append(len(students[student]["name"]))
    max_len_name = max(len_names)

    lines.append("_" * (max_len_name + 23))
    lines.append(f"| ID        | Name{(max_len_name - 4) * ' '} | GPA  |")
    lines.append("_" * (max_len_name + 23))
    for student in students:
        lines.append(
            f"| {student:8d} | {students[student]['name']}{(max_len_name - len(students[student]['name'])) * ' '} | {students[student]['gpa']:4.2f} |")
    lines.append("_" * (max_len_name + 23))

    for line in lines:
        print(line)

    return True
