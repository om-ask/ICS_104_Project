from editRecords import add_record, remove_record, modify_record_menu
from mainInternal import RecordsTable, show_data, Inputs, create_file, valid_filename_check, menu, Back
from searchFromRecords import search_menu
from sortRecord import sort_menu

from takeWhatYouWantFromMe import calculate_average

# Define the default file to read from
DEFAULT_STUDENT_FILE_NAME = "students.txt"


def main():
    filename = DEFAULT_STUDENT_FILE_NAME

    # Define an input for taking in filenames from the user in case the current file cannot be opened for any reason
    new_file_name_input = Inputs()
    new_file_name_input.add_prompt("Enter a new filename: ", valid_filename_check)

    # Create student records and read from file while handling any errors
    while True:
        try:
            records = RecordsTable(filename=filename)
            print(f"Successfully opened and read from file '{filename}'")
            print()
            break

        except FileNotFoundError:
            print(f"ERROR: Could not find file '{filename}'")
            print()

            print("Do you want to?")
            choice_number = menu([f"Create File '{filename}'", "Set New Filename"])
            print("\n")

            if choice_number == 0:  # Back
                print("Exiting Program Prematurely")
                return

            elif choice_number == 1:  # Option Create File
                return_value = create_file(filename)

            else:  # Option Set New Filename
                return_value = new_file_name_input.take_inputs()

        except IndexError:
            print(f"ERROR: '{filename}' File format is incorrect")
            print()
            return_value = new_file_name_input.take_inputs()

        except IOError:
            print(f"ERROR: Unexpected error occurred while trying to read '{filename}'")
            print()
            return_value = new_file_name_input.take_inputs()

        if not return_value:  # Means the user went back and cancelled giving input
            print("Exiting Program Prematurely")
            return

        filename = return_value

    # Define the menu options
    menu_options = ["View Records",
                    "Add Record",
                    "Remove Record",
                    "Modify Record",
                    "Search Records",
                    "Sort Records",
                    "Top Performing Students",  # TODO Implement this (hashem) - Display the top 3 students
                    "Calculate Average",  # TODO Implement this (hashem) - Calculate the average of all the gpas
                    "Save to Current File",  # TODO Implement this (hashem)- update file without exiting
                    "Switch File",  # TODO Implement this (hashem) - clear current records and then read new file
                    "Write to File",  # TODO Implement this (hashem) - Take a valid filename and write to it
                    "Merge Files"]  # TODO Implement this (thenextyay)- merge 2 student files

    # Loop and display a menu while responding to user input
    while True:
        print("Choose: ")

        try:
            option_number = menu(options=menu_options, back_option="Save and Exit")

        except Back:
            break

        print("\n\n")
        try:
            if option_number == 1:  # Option View Records
                show_data(records.raw())

            elif option_number == 2:  # Option Add Record
                add_record(records)

            elif option_number == 3:  # Option Remove Record
                remove_record(records)

            elif option_number == 4:  # Option Modify Record
                modify_record_menu(records)

            elif option_number == 5:  # Option Search Record
                search_menu(records)

            elif option_number == 6:  # Option Sort Records
                sort_menu(records)

            elif option_number == 7:  # Option Top Performing
                print("Not Implemented")

            elif option_number == 8:  # Option Average
                calculate_average(records)

            elif option_number == 9:  # Option Save to Current File
                print("Not Implemented")

            elif option_number == 10:  # Option Switch File
                print("Not Implemented")

            elif option_number == 11:  # Option Write to File
                print("Not Implemented")

            elif option_number == 12:  # Option Merge Files
                print("Not Implemented")

        except Back:  # If any of these options go back, ignore it and continue loop
            pass

    # After exiting the main menu, update the current student file
    while True:
        try:
            records.update_file(filename)
            print(f"Successfully updated file '{filename}'")
            print()
            break

        except IOError:
            print(f"ERROR: Could not write to '{filename}'")
            filename = new_file_name_input.take_inputs()

            if not filename:
                print("Exiting program without saving.")
                return

    print("Program Closed")


# Run the program
if __name__ == "__main__":
    main()
