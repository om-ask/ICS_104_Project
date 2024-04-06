from mainInternal import wrap_function, display_menu, take_inputs, id_check


def search_menu(student_records: dict) -> tuple:
    sort_menu_options = {
        "Search By ID": wrap_function(search_by_id, student_records)
    }

    display_menu(sort_menu_options, "Back", pre="Choose search type:", final="\n"*2)

    return 0, None


def search_by_id(students) -> bool:

    success, record_info = take_inputs({
        "Enter ID: ": wrap_function(id_check, students)
    })

    if success == 0:
        student_id = record_info[0]
        the_student = {int(student_id): students[int(student_id)]}

        show_data(the_student)

    else:
        pass

    return True


if __name__ == "__main__":
    from fileOperations import read_file_to_data
    from showData import show_data
    STUDENT_FILE_NAME = "students.txt"
    # test_student_records = read_file_to_data(,
    show_data(test_student_records)
    search_by_id(test_student_records)
