from mainInternal import show_data, RecordsTable, Inputs, menu, Back


def search_menu(record_table: RecordsTable):
    """Prompts the user for a search type then searches the record table and displays the results
    Supports going back
    """
    # Loop until the user goes back or a successful search is made
    while True:
        # Prompt the user to choose a search type
        print("Choose Search Type:")
        choice_number = menu(["Search by Name", "Search by ID"])
        print("\n\n")

        try:
            # Run each search type
            if choice_number == 1:  # Option Search by Name
                search_by_name(record_table)

            else:  # Option Search by ID
                search_by_id(record_table)

            # Exit
            return

        except Back:
            # If any of the options went back, display the search type menu again
            pass


def search_by_name(record_table: RecordsTable):
    """Takes a query from the user and searches the record table and displays the search results
    Supports going back
    """
    # Define an input for taking a search query
    inputs = Inputs()
    inputs.add_prompt("Search: ", None)

    # Take the query
    query = inputs.take_inputs()

    # Search the records table
    results_records = record_table.search_record(query)

    # Show the results
    show_data(results_records.raw())


def search_by_id(record_table: RecordsTable):
    """Takes an id from user and displays the info of the student with that id
    Supports going back
    """
    # Define an input for taking an id that is present in the records table
    inputs = Inputs()
    inputs.add_prompt("Enter ID: ", record_table.present_id_check)

    # Take the input
    student_id = int(inputs.take_inputs())

    # Get the record from the table
    student_record = record_table.get_record(student_id=student_id)

    # Show the record
    show_data([student_record.raw()])


if __name__ == "__main__":
    STUDENT_FILE_NAME = "students2.txt"
    # Create student records and read from file
    records = RecordsTable()
    records.read_file(STUDENT_FILE_NAME)

    show_data(records.raw())
    search_menu(records)
