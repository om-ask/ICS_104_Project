def read_file_to_dic(student_file) -> dict:
    file = open(student_file, "r")
    lines = file.readlines()
    file.close()

    students = {}

    for line in lines:
        student_data_list = line[:-1].split(",")
        id = int(student_data_list[0])
        name = student_data_list[1]
        gpa = float(student_data_list[2])
        students[id] = {"name": name, "gpa": gpa}

    return students
