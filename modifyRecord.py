from internal import take_inputs, wrap_function


def id_check(students, student_id) -> tuple[bool, str]:
    try:
        student_id = int(student_id)
        if len(str(student_id)) == 9:
            if student_id in list(students.keys()):
                return True, ""
            else:
                return False, "the ID is not there"
        else:
            return False, "the ID should be 9 integer numbers"

    except ValueError:
        return False, "the ID should be 9 integer numbers"


def gpa_check(gpa) -> tuple[bool, str]:
    try:
        gpa = float(gpa)
        if 0 <= gpa <= 4:
            return True, ""
        else:
            return False, "the GPA should be a number between 0 and 4"
    except ValueError:
        return False, "the GPA should be a number between 0 and 4"


def modify_record(students) -> bool:
    record_info = take_inputs({
        "Enter ID: ": wrap_function(id_check, students),
        "Enter GPA: ": gpa_check
    })

    if record_info:
        student_id, gpa = record_info
        students[int(student_id)]['gpa'] = float(gpa)

    else:
        pass

    return True


if __name__ == "__main__":
    from readFileToDic import read_file_to_dic
    from showData import show_data

    STUDENT_FILE_NAME = "students.txt"
    student_records = read_file_to_dic(STUDENT_FILE_NAME)
    show_data(student_records)
    modify_record(student_records)
    show_data(student_records)
