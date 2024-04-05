def read_file_to_dic(student_records, student_file):
    with open(student_file, "r") as file:
        lines = file.readlines()

    for line in lines:
        student_data_list = line[:-1].split(",")
        student_id = int(student_data_list[0])
        name = student_data_list[1]
        gpa = float(student_data_list[2])
        student_records[student_id] = {"name": name, "gpa": gpa}

