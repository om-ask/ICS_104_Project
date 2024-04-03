from internal import wrap_function, display_menu, take_inputs
from showData import show_data


def search_menu(student_records: dict) -> bool:
    sort_menu_options = {
        "Search By ID": wrap_function(search_by_id, student_records)
    }

    display_menu(sort_menu_options, "Back", pre="Choose search type:", final="\n"*2)

    return True


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


def search_by_id(students) -> bool:

    record_info = take_inputs({
        "Enter ID: ": wrap_function(id_check, students)
    })

    if record_info:
        student_id = record_info[0]
        the_student = {}
        the_student[int(student_id)] = students[int(student_id)]

        show_data(the_student)

    else:
        pass

    return True


if __name__ == "__main__":
    from readFileToDic import read_file_to_dic
    from showData import show_data
    STUDENT_FILE_NAME = "students.txt"
    student_records = read_file_to_dic(STUDENT_FILE_NAME)
    show_data(student_records)
    search_by_id(student_records)
