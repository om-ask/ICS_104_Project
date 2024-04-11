from mainInternal import show_data, Codes, RecordsTable, Menu, StudentRecord


# TODO Sort by name (hashem)
def sort_menu(student_records: RecordsTable):
    sort_type_menu = Menu()
    sort_type_menu.add_option("Sort by ID", sort_records, student_records, "id")
    sort_type_menu.add_option("Sort by GPA", sort_records, student_records, "gpa")

    menu_return = Codes.INCONCLUSIVE
    while menu_return == Codes.INCONCLUSIVE:
        choice_number, menu_return = sort_type_menu.display(pre="Choose sort type:", final="\n" * 2)

    if menu_return == Codes.BACK:
        return Codes.BACK


def sort_records(student_records: RecordsTable, sort_type="gpa"):
    sort_order_menu = Menu()
    sort_order_menu.add_option("Ascending")
    sort_order_menu.add_option("Descending")

    choice_number, menu_return = sort_order_menu.display(pre="Choose sort order:", final="\n" * 2)
    if menu_return == Codes.BACK:
        return Codes.BACK

    elif choice_number == 1:
        descending = False

    else:
        descending = True

    if sort_type == "id":
        sorted_student_records = sorted(student_records.records(), key=StudentRecord.id, reverse=descending)

    else:
        sorted_student_records = sorted(student_records.records(), key=StudentRecord.gpa, reverse=descending)

    sorted_record_table = RecordsTable(sorted_student_records)
    show_data(sorted_record_table.raw())


if __name__ == "__main__":
    STUDENT_FILE_NAME = "students2.txt"
    # Create student records and read from file
    records = RecordsTable()
    records.read_file(STUDENT_FILE_NAME)

    show_data(records.raw())
    sort_menu(records)


