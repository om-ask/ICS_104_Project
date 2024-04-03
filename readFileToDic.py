def read_file_to_dic(STUDENT_FILE_NAME) -> dict:
    file = open(STUDENT_FILE_NAME,"r")
    lines = file.readlines()
    file.close()

    students = {}

    for line in lines:
        student_data_list = line[:-1].split(",")
        id = int(student_data_list[0])
        name = student_data_list[1]
        gpa = float(student_data_list[2])
        students[id] = {"name" : name, "gpa": gpa}

    return students

