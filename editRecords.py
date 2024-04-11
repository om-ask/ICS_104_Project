from mainInternal import RecordsTable, Inputs, StudentRecord, Codes, show_data, Menu


def add_record(student_records: RecordsTable):
    inputs = Inputs()
    inputs.add_prompt("Enter ID:", student_records.new_id_check)
    inputs.add_prompt("Enter Name:", StudentRecord.valid_name_check)
    inputs.add_prompt("Enter GPA:", StudentRecord.valid_gpa_check)

    input_return = inputs.take_inputs()

    if input_return == Codes.BACK:
        return Codes.BACK

    student_id, student_name, student_gpa = int(input_return[0]), input_return[1], float(input_return[2])

    new_record = StudentRecord(student_id, student_name, student_gpa)
    student_records.add_record(new_record)


def remove_record(student_records: RecordsTable):
    inputs = Inputs()
    inputs.add_prompt("Enter ID:", student_records.present_id_check)

    input_return = inputs.take_inputs()

    if input_return == Codes.BACK:
        return Codes.BACK

    student_id = int(input_return[0])

    record_to_remove = student_records.get_record(student_id=student_id)
    student_records.remove_record(record_to_remove)


def modify_by_search(student_records: RecordsTable):
    inputs = Inputs()
    inputs.add_prompt("Search:", student_records.present_id_check, analyzer=student_records.search_analyzer)
    inputs.add_prompt("Enter GPA:", StudentRecord.valid_gpa_check)

    return inputs.take_inputs()


def modify_by_id(student_records: RecordsTable):
    inputs = Inputs()
    inputs.add_prompt("Enter ID:", student_records.present_id_check)
    inputs.add_prompt("Enter GPA:", StudentRecord.valid_gpa_check)

    return inputs.take_inputs()


def modify_record_menu(student_records: RecordsTable):
    show_data(student_records.raw())

    modify_menu = Menu()
    modify_menu.add_option("By Searching For a Student", modify_by_search, student_records)
    modify_menu.add_option("By ID", modify_by_id, student_records)

    response_number, menu_return = modify_menu.display()

    if menu_return == Codes.BACK:
        return Codes.BACK

    student_id, student_gpa = int(menu_return[0]), float(menu_return[1])
    record_to_modify = student_records.get_record(student_id=student_id)
    record_to_modify.modify_gpa(student_gpa)


if __name__ == "__main__":
    STUDENT_FILE_NAME = "students.txt"
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

