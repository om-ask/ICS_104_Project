from mainInternal import show_data, RecordsTable, Menu, Inputs


def search_menu(record_table: RecordsTable):
    search_type_menu = Menu()
    search_type_menu.add_option("Search by Name", search_by_name, record_table)
    search_type_menu.add_option("Search by ID", search_by_id, record_table)

    search_type_menu.display(pre="Choose search type:", final="\n" * 2)


def search_by_name(record_table: RecordsTable):
    inputs = Inputs()
    inputs.add_prompt("Search: ", None)
    input_return = inputs.take_inputs()

    query = input_return
    results_records = record_table.search_record(query)

    show_data(results_records.raw())


def search_by_id(record_table: RecordsTable):
    inputs = Inputs()
    inputs.add_prompt("Enter ID: ", record_table.present_id_check)

    input_return = inputs.take_inputs()

    student_id = int(input_return)
    student_record = record_table.get_record(student_id=student_id)

    show_data([student_record.raw()])


if __name__ == "__main__":
    STUDENT_FILE_NAME = "students2.txt"
    # Create student records and read from file
    records = RecordsTable()
    records.read_file(STUDENT_FILE_NAME)

    show_data(records.raw())
    search_menu(records)
