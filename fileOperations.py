def read_file(file_name: str) -> dict:
    student_records_list = []
    student_records_by_id = {}
    student_records_by_name = {}
    names_set = set()

    with open(file_name, "r") as file:
        line = file.readline().strip()

        while line:
            student_record = line.split(",")
            student_id = int(student_record[0])
            student_name = student_record[1].strip()
            student_gpa = float(student_record[2])

            student_records_list.append({"id": student_id, "name": student_name, "gpa": student_gpa})
            student_records_by_id[student_id] = {"name": student_name, "gpa": student_gpa}
            student_records_by_name[student_name] = {"id": student_id, "gpa": student_gpa}
            names_set.add(student_name)

            line = file.readline().strip()

    return {"Records": student_records_list, "ID Records": student_records_by_id,
            "Name Records": student_records_by_name, "Names": names_set}


def update_file(file_name: str, data: dict):
    with open(file_name, "w") as file:
        for student_record in data["Records"]:
            student_id = student_record['id']
            student_name = student_record['name']
            student_gpa = student_record['gpa']

            file.write(f"{student_id}, {student_name}, {student_gpa}\n")
