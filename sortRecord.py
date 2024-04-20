from mainInternal import show_data, RecordsTable, StudentRecord, menu, Back


# TODO Sort by name (hashem)
def sort_menu(student_records: RecordsTable):
    while True:
        print("Choose Sort Type:")
        sort_type_number = menu(["Sort by ID", "Sort by GPA"])
        print("\n\n")

        try:
            print("Choose Sort Order:")
            sort_order_number = menu(["Ascending", "Descending"])
            print("\n\n")

        except Back:
            continue  # Retry menu selection

        if sort_order_number == 1:  # Option Ascending
            descending = False

        else:  # Option Descending
            descending = True

        # Sort
        if sort_type_number == 1:  # Sort by ID
            # noinspection PyTypeChecker
            sorted_student_records = sorted(student_records.records(), key=StudentRecord.id, reverse=descending)

        else:
            # noinspection PyTypeChecker
            sorted_student_records = sorted(student_records.records(), key=StudentRecord.gpa, reverse=descending)

        # Display the sorted results
        sorted_record_table = RecordsTable(sorted_student_records)
        show_data(sorted_record_table.raw())
        return  # Exit


if __name__ == "__main__":
    STUDENT_FILE_NAME = "students2.txt"
    # Create student records and read from file
    records = RecordsTable()
    records.read_file(STUDENT_FILE_NAME)

    show_data(records.raw())
    sort_menu(records)
