from editRecords import add_record, remove_record, modify_record_menu
from mainInternal import Codes, RecordsTable, Menu, show_data
from searchFromRecords import search_menu
from sortRecord import sort_menu

STUDENT_FILE_NAME = "students.txt"


def main():
    # Create student records and read from file
    records = RecordsTable()
    records.read_file(STUDENT_FILE_NAME)

    # Create main menu
    main_menu = Menu(back_option="Save and Exit")
    main_menu.add_option("View Records", show_data, records.raw())
    main_menu.add_option("Add Record", add_record, records)
    main_menu.add_option("Remove Record", remove_record, records)
    main_menu.add_option("Modify Record", modify_record_menu, records)
    main_menu.add_option("Sort Records", sort_menu, records)
    main_menu.add_option("Search Records", search_menu, records)

    # Loop and display main menu until a BACK code is received
    menu_return = None
    while menu_return != Codes.BACK:
        choice_number, menu_return = main_menu.display(pre="Choose:", final="\n" * 2)

    # After exiting the main menu, update the current student file
    try:
        records.update_file(STUDENT_FILE_NAME)

    # If anything wrong occurs, notify the user
    except IOError:
        print(f"ERROR: Could not write to {STUDENT_FILE_NAME}")


# Run the program
if __name__ == "__main__":
    main()
