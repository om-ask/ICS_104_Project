def update_file(student_records: dict, file_name: str):
    lines = []

    for student_id in student_records:
        lines.append(f"{student_id},{student_records[student_id]['name']},{student_records[student_id]['gpa']}")

    file = open(file_name,"w")
    for line in lines:
        file.write(line + '\n')
