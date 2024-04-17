from editRecords import add_record, remove_record, modify_record_menu
from mainInternal import Codes, RecordsTable, Menu, show_data, Inputs, create_file, valid_filename_check
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

            file_creation_menu = Menu()
            file_creation_menu.add_option(f"Create File '{filename}'", create_file, filename)
            file_creation_menu.add_option("Set New Filename", new_file_name_input.take_inputs)

            return_value = Codes.INCONCLUSIVE
            while return_value == Codes.INCONCLUSIVE:
                choice_number, return_value = file_creation_menu.display(pre="Do you want to?")

        except IndexError:
            print(f"ERROR: '{filename}' File format is incorrect")
            print()
            return_value = new_file_name_input.take_inputs()

        except IOError:
            print(f"ERROR: Unexpected error occurred while trying to read '{filename}'")
            print()
            return_value = new_file_name_input.take_inputs()

        if return_value == Codes.BACK:
            print("Exiting Program Prematurely")
            return

        else:
            filename = return_value

    # Create main menu
    main_menu = Menu(back_option="Save and Exit")
    main_menu.add_option("View Records", show_data, records.raw())
    main_menu.add_option("Add Record", add_record, records)
    main_menu.add_option("Remove Record", remove_record, records)
    main_menu.add_option("Modify Record", modify_record_menu, records)
    main_menu.add_option("Search Records", search_menu, records)
    main_menu.add_option("Sort Records", sort_menu, records)
    main_menu.add_option("Top Performing Students")  # TODO Implement this (hashem) - Display the top 3 students
    main_menu.add_option("Calculate Average", calculate_average, records)  # TODO Implement this (hashem) - Calculate the average of all the gpas
    main_menu.add_option("Save to Current File")  # TODO Implement this (hashem)- update file without exiting
    main_menu.add_option("Switch File")  # TODO Implement this (hashem) - clear current records and then read new file
    main_menu.add_option("Write to File")  # TODO Implement this (hashem) - Take a valid filename and write to it
    main_menu.add_option("Merge Files")  # TODO Implement this (thenextyay)- merge 2 student files

    # Loop and display main menu until a BACK code is received
    menu_return = None
    while menu_return != Codes.BACK:
        choice_number, menu_return = main_menu.display(pre="Choose:", final="\n" * 2)

    # After exiting the main menu, update the current student file
    while True:
        try:
            records.update_file(filename)
            print(f"Successfully updated file '{filename}'")
            print()
            break

        except IOError:
            print(f"ERROR: Could not write to '{filename}'")
            return_value = new_file_name_input.take_inputs()

        if return_value == Codes.BACK:
            print("Exiting program without saving.")
            return

        else:
            filename = return_value

    print("Program Closed")


# Run the program
if __name__ == "__main__":
    main()
