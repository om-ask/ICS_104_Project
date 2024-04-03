from internal import take_inputs, wrap_function


def id_check(students, student_id) -> bool:
    try:
        student_id = int(student_id)
        if student_id not in list(students.keys()):
            if len(str(student_id)) == 9:
                return True
            else:
                print("the ID should be 9 integer numbers")
        else:
            print("the ID is already there")

    except ValueError:
        print("the ID should be 9 integer numbers")

    return False


def name_check(name) -> bool:
    if len(name.split()) >= 2:
        return True
    else:
        print("first and second name please")

    return False


def gpa_check(gpa) -> bool:
    try:
        gpa = float(gpa)
        if 0 <= gpa <= 4:
            return True
        else:
            print("the GPA should be a number between 0 and 4")
    except ValueError:
        print("the GPA should be a number between 0 and 4")

    return False


def add_record(students) -> bool:

    record_info = take_inputs({
        "Enter ID:": wrap_function(id_check, students),
        "Enter Name": name_check,
        "Enter GPA": gpa_check
    })

    if record_info:
        student_id, name, gpa = record_info
        students[student_id] = {'name': name, 'gpa': gpa}

    else:
        pass

    return True


if __name__ == "__main__":
    from readFileToDic import read_file_to_dic
    from showData import show_data
    STUDENT_FILE_NAME = "students.txt"
    student_records = read_file_to_dic(STUDENT_FILE_NAME)
    show_data(student_records)
    add_record(student_records)
    show_data(student_records)
