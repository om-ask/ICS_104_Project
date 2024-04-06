from mainInternal import take_inputs, wrap_function, gpa_check, name_check, id_check, search_input, display_menu


def add_record(students) -> tuple:
    success, record_info = take_inputs({
        "Enter ID: ": wrap_function(id_check, students),
        "Enter Name: ": name_check,
        "Enter GPA: ": gpa_check
    })

    if success == 0:
        student_id, name, gpa = record_info
        students[int(student_id)] = {'name': name, 'gpa': float(gpa)}

    return 0, None


def remove_record(students) -> tuple:
    success, record_info = take_inputs({
        "Enter ID: ": wrap_function(id_check, students)
    })

    if success == 0:
        student_id = record_info[0]
        students.pop(int(student_id))

    return 0, None


def modify_record(students, students_by_name, names, inverse_index) -> tuple:
    menu_choice, menu_response, menu_return = display_menu(
        {"Search For a Student": wrap_function(search_input, names, students_by_name, inverse_index)}, "Enter ID")

    if menu_choice == 1 and menu_response == 0:
        student_id = menu_return
        success, record_info = take_inputs({
            "Enter GPA: ": gpa_check
        })
        if success == 0:
            gpa = record_info[0]
            students[int(student_id)]['gpa'] = float(gpa)

    else:
        success, record_info = take_inputs({
            "Enter ID: ": wrap_function(id_check, students),
            "Enter GPA: ": gpa_check
        })

        if success == 0:
            student_id, gpa = record_info
            students[int(student_id)]['gpa'] = float(gpa)

    return 0, None


if __name__ == "__main__":
    from showData import show_data

    STUDENT_FILE_NAME = "students.txt"
    # student_records = read_file_to_data(,

    show_data(student_records)
    add_record(student_records)
    show_data(student_records)

    show_data(student_records)
    modify_record(student_records)
    show_data(student_records)

    show_data(student_records)
    remove_record(student_records)
    show_data(student_records)
