def read_file_to_data(student_file, student_records_list, student_records_by_id, student_records_by_name, names_set):
    with open(student_file, "r") as file:
        lines = file.readlines()

    for line in lines:
        student_data_list = line[:-1].split(",")
        student_id = int(student_data_list[0])
        name = student_data_list[1]
        gpa = float(student_data_list[2])

        student_records_list.append({"id": student_id, "name": name, "gpa": gpa})
        student_records_by_id[student_id] = {"name": name, "gpa": gpa}
        student_records_by_name[name] = {"id": student_id, "gpa": gpa}
        names_set.add(name)


def update_file(student_records: dict, file_name: str):
    lines = []

    for student_id in student_records:
        lines.append(f"{student_id},{student_records[student_id]['name']},{student_records[student_id]['gpa']}")

    file = open(file_name, "w")
    for line in lines:
        file.write(line + '\n')
