from mainInternal import display_menu, take_inputs, id_check, show_data, Codes, menu_option, input_prompt


def search_menu(data: dict) -> tuple:
    sort_menu_options = {
        **menu_option("Search By ID", search_by_id, data)
    }

    code, menu_response, menu_return = display_menu(sort_menu_options, "Back", pre="Choose search type:", final="\n"*2)

    return code, menu_return


def search_by_id(data: dict) -> tuple:

    code, record_info = take_inputs({
        **input_prompt("Enter ID: ", (id_check, data["ID Records"]))
    })

    if code == Codes.SUCCESS:
        student_id = int(record_info[0])
        student_record = {student_id: data["ID Records"][student_id]}

        show_data(student_record)

    return code, record_info


if __name__ == "__main__":
    from fileOperations import read_file

    STUDENT_FILE_NAME = "students.txt"
    test_data = read_file(STUDENT_FILE_NAME)
    test_student_records = test_data["ID Records"]

    show_data(test_student_records)
    search_by_id(test_student_records)
