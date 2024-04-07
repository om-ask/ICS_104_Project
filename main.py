from editRecords import add_record, remove_record, modify_record_menu
from fileOperations import update_file, read_file
from mainInternal import display_menu, update_inverse_index, show_data, Codes, menu_option
from searchFromRecords import search_menu
from sortRecord import sort_menu

STUDENT_FILE_NAME = "students.txt"


def main():
    # Read Data
    data = read_file(STUDENT_FILE_NAME)
    # print(data["Records"])
    data["Settings"] = {}
    data["Inverse Index"] = update_inverse_index({}, data["Names"])

    main_menu = {
        **menu_option("View Records", show_data, data["ID Records"]),
        **menu_option("Add Record", add_record, data),
        **menu_option("Remove Record", remove_record, data),
        **menu_option("Modify Record", modify_record_menu, data),
        **menu_option("Sort Records", sort_menu, data),
        **menu_option("Search Records", search_menu, data),

    }
    while True:
        code, menu_response, menu_return = display_menu(main_menu, "Save and Exit", pre="Choose:", final="\n" * 2)
        print(code, menu_response, menu_return)
        if code == Codes.BACK:
            try:
                update_file(STUDENT_FILE_NAME, data)

            except IOError:
                print(f"ERROR: Could not write to {STUDENT_FILE_NAME}")

            break

        else:
            print("\n")


if __name__ == "__main__":
    main()
