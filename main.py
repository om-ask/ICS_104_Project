from editRecords import add_record, remove_record, modify_record_menu
from mainInternal import RecordsTable, show_data, menu, Back, \
    read_file_into_record, update_file_from_record, write_to_new_file, switch_file
from mergeFile import merge_records
from searchFromRecords import search_menu
from sortRecord import sort_menu
from takeWhatYouWantFromMe import calculate_average, top_performing_students

# Define the default file to read from
DEFAULT_STUDENT_FILE_NAME = "students2.txt"


def main():
    """The main program
    """
    # Initialise a new RecordsTable where all the student records are
    records = RecordsTable()

    # Attempt to read from the default file
    try:
        read_file_into_record(records, DEFAULT_STUDENT_FILE_NAME)

    except Back:
        # If the user goes back, exit the program
        print("Exiting program prematurely without doing anything")
        return

    # Define the menu options
    menu_options = ["View Records",
                    "Add Record",
                    "Remove Record",
                    "Modify Record",
                    "Search Records",
                    "Sort Records",
                    "Top Performing Students",
                    "Calculate Average",
                    "Save to Current File",
                    "Switch File",
                    "Write to File",
                    "Merge Files"]

    # Loop and display the main menu while responding to user input
    while True:
        print("CURRENT FILE:", records.filename)
        print("Choose: ")

        try:  # Display the menu
            selected_option = menu(options=menu_options, back_option="Save and Exit")

        except Back:
            break  # If the user goes back, exit the main menu loop

        print("\n")
        # Run the function the user chose from the menu, while ignoring if the option goes back
        try:
            if selected_option == 1:  # Option View Records
                print("Viewing Records")
                show_data(records.raw())

            elif selected_option == 2:  # Option Add Record
                print("Adding Record")
                add_record(records)

            elif selected_option == 3:  # Option Remove Record
                print("Removing Record")
                remove_record(records)

            elif selected_option == 4:  # Option Modify Record
                print("Modifying Record")
                modify_record_menu(records)

            elif selected_option == 5:  # Option Search Record
                print("Searching Records")
                search_menu(records)

            elif selected_option == 6:  # Option Sort Records
                print("Sorting Records")
                sort_menu(records)

            elif selected_option == 7:  # Option Top Performing
                print("Display Top Students")
                top_performing_students(records)

            elif selected_option == 8:  # Option Average
                print("Calculate Average")
                calculate_average(records)

            elif selected_option == 9:  # Option Save to Current File
                print("Save to Current File")
                update_file_from_record(records, records.filename)

            elif selected_option == 10:  # Option Switch File
                print("Switch File")
                switch_file(records)

            elif selected_option == 11:  # Option Write to File
                print("Write to File")
                write_to_new_file(records)

            elif selected_option == 12:  # Option Merge Files
                print("Merge Records")
                merge_records(records)

            input("Press ENTER to continue")

        except Back:  # If any of these options go back, ignore it and continue loop
            pass

    # After exiting the main menu, update the current student file
    try:
        update_file_from_record(records, records.filename)

    except Back:
        print("Exiting program without saving.")
        return

    print("Program Closed")


# Run the program
if __name__ == "__main__":
    main()
