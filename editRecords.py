from mainInternal import RecordsTable, Inputs, StudentRecord, show_data, Menu, valid_name_check, valid_gpa_check


def add_record(student_records: RecordsTable):
    inputs = Inputs()
    inputs.add_prompt("Enter ID:", student_records.new_id_check)
    inputs.add_prompt("Enter Name:", valid_name_check)
    inputs.add_prompt("Enter GPA:", valid_gpa_check)

    input_return = inputs.take_inputs()
    student_id, student_name, student_gpa = int(input_return[0]), input_return[1], float(input_return[2])

    new_record = StudentRecord(student_id, student_name, student_gpa)
    student_records.add_record(new_record)


# TODO Implement search here (hashem)
def remove_record(student_records: RecordsTable):
    inputs = Inputs()
    inputs.add_prompt("Enter ID:", student_records.present_id_check)

    input_return = inputs.take_inputs()
    student_id = int(input_return)

    record_to_remove = student_records.get_record(student_id=student_id)
    student_records.remove_record(record_to_remove)


def modify_by_search(student_records: RecordsTable):
    inputs = Inputs()
    inputs.add_prompt("Search:", student_records.present_id_check, analyzer=student_records.search_analyzer)
    inputs.add_prompt("Enter GPA:", valid_gpa_check)

    return inputs.take_inputs()


def modify_by_id(student_records: RecordsTable):
    inputs = Inputs()
    inputs.add_prompt("Enter ID:", student_records.present_id_check)
    inputs.add_prompt("Enter GPA:", valid_gpa_check)

    return inputs.take_inputs()


def modify_record_menu(student_records: RecordsTable):
    show_data(student_records.raw())

    modify_menu = Menu()
    modify_menu.add_option("By Searching For a Student", modify_by_search, student_records)
    modify_menu.add_option("By ID", modify_by_id, student_records)

    response_number, menu_return = modify_menu.display()

    student_id, student_gpa = int(menu_return[0]), float(menu_return[1])
    record_to_modify = student_records.get_record(student_id=student_id)
    record_to_modify.modify_gpa(student_gpa)


if __name__ == "__main__":
    STUDENT_FILE_NAME = "students2.txt"
    # Create student records and read from file
    records = RecordsTable()
    records.read_file(STUDENT_FILE_NAME)

    show_data(records.raw())
    add_record(records)
    show_data(records.raw())

    show_data(records.raw())
    modify_record_menu(records)
    show_data(records.raw())

    show_data(records.raw())
    remove_record(records)
    show_data(records.raw())
