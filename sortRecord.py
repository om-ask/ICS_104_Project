from mainInternal import show_data, RecordsTable, StudentRecord, menu, Back


# TODO Sort by name (hashem)
def sort_menu(student_records: RecordsTable):
    """Prompts the user to select a sort type and order and then displays the results
    Supports going back
    """
    # Loop until the user goes back or a successful sort occurs
    while True:
        # Prompt the user for a sort type
        print("Choose Sort Type:")
        sort_type_number = menu(["Sort by ID", "Sort by GPA"])
        print("\n")

        try:
            # Prompt the user for a sort order
            print("Choose Sort Order:")
            sort_order_number = menu(["Ascending", "Descending"])
            print("\n")

        except Back:
            # If the user goings back here, return to the first menu
            continue  # Retry menu selection

        # Define a boolean depending on the sort order response from the menu
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

        # Create a new records table with the sorted records
        sorted_record_table = RecordsTable(sorted_student_records)

        # Display the sorted results
        show_data(sorted_record_table.raw())

        # Exit
        return


if __name__ == "__main__":
    STUDENT_FILE_NAME = "students2.txt"
    # Create student records and read from file
    records = RecordsTable()
    records.read_file(STUDENT_FILE_NAME)

    show_data(records.raw())
    sort_menu(records)
