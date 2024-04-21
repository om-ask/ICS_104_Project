from editRecords import add_record, remove_record, modify_record_menu
from mainInternal import RecordsTable, show_data, menu, Back, \
    read_file_into_record, update_file_from_record
from searchFromRecords import search_menu
from sortRecord import sort_menu
from takeWhatYouWantFromMe import calculate_average

# Define the default file to read from
DEFAULT_STUDENT_FILE_NAME = "students.txt"


def main():
    """The main program
    """
    # Initialise a new RecordsTable where all the student records are
    records = RecordsTable()

    # Attempt to read from the default file
    try:
        read_file_into_record(DEFAULT_STUDENT_FILE_NAME, records)

    except Back:
        # If the user goes back, continue the program without reading from the file
        print("No student records file was read from.")
        pass

    # Define the menu options
    menu_options = ["View Records",
                    "Add Record",
                    "Remove Record",
                    "Modify Record",
                    "Search Records",
                    "Sort Records",
                    "Top Performing Students",  # TODO Implement this (hashem) - Display the top 3 students
                    "Calculate Average",  # TODO Implement this (hashem) - Calculate the average of all the GPAs
                    "Save to Current File",  # TODO Implement this (hashem)- update file without exiting
                    "Switch File",  # TODO Implement this (hashem) - clear current records and then read new file
                    "Write to File",  # TODO Implement this (hashem) - Take a valid filename and write to it
                    "Merge Files"]  # TODO Implement this (thenextyay)- merge 2 student files

    # Loop and display the main menu while responding to user input
    while True:
        print("Choose: ")

        try:  # Display the menu
            selected_option = menu(options=menu_options, back_option="Save and Exit")

        except Back:
            break  # If the user goes back, exit the main menu loop

        print("\n\n")
        # Run the function the user chose from the menu, while ignoring if the option goes back
        try:
            if selected_option == 1:  # Option View Records
                show_data(records.raw())

            elif selected_option == 2:  # Option Add Record
                add_record(records)

            elif selected_option == 3:  # Option Remove Record
                remove_record(records)

            elif selected_option == 4:  # Option Modify Record
                modify_record_menu(records)

            elif selected_option == 5:  # Option Search Record
                search_menu(records)

            elif selected_option == 6:  # Option Sort Records
                sort_menu(records)

            elif selected_option == 7:  # Option Top Performing
                print("Not Implemented")

            elif selected_option == 8:  # Option Average
                calculate_average(records)

            elif selected_option == 9:  # Option Save to Current File
                print("Not Implemented")

            elif selected_option == 10:  # Option Switch File
                print("Not Implemented")

            elif selected_option == 11:  # Option Write to File
                print("Not Implemented")

            elif selected_option == 12:  # Option Merge Files
                print("Not Implemented")

        except Back:  # If any of these options go back, ignore it and continue loop
            pass

    # After exiting the main menu, update the current student file
    try:
        update_file_from_record(records.filename, records)

    except Back:
        print("Exiting program without saving.")
        return

    print("Program Closed")


# Run the program
if __name__ == "__main__":
    main()
