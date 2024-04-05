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


def remove_record(students) -> bool:
    record_info = take_inputs({
        "Enter ID: ": wrap_function(id_check, students)
    })

    if record_info:
        student_id = record_info[0]
        students.pop(int(student_id))

    else:
        pass

    return True


if __name__ == "__main__":
    from readFileToDic import read_file_to_dic
    from showData import show_data

    STUDENT_FILE_NAME = "students.txt"
    student_records = read_file_to_dic(STUDENT_FILE_NAME)
    show_data(student_records)
    remove_record(student_records)
    show_data(student_records)
