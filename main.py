from editRecords import add_record, remove_record, modify_record
from fileOperations import update_file, read_file_to_data
from mainInternal import display_menu, wrap_function, update_inverse_index
from searchFromRecords import search_menu
from showData import show_data
from sortRecord import sort_menu

STUDENT_FILE_NAME = "students.txt"


def main():
    # Read Data
    student_records = []
    student_records_by_id = {}
    student_records_by_name = {}
    names = set()

    settings = {}
    inverse_index = {}

    read_file_to_data(STUDENT_FILE_NAME, student_records, student_records_by_id, student_records_by_name, names)
    update_inverse_index(inverse_index, names)

    data = {"Records": student_records, "ID Records": student_records_by_id, "Name Records": student_records_by_name,
            "Names": names, "Settings": settings, "Inverse Index": inverse_index}

    main_menu_options = {
        "View Records": wrap_function(show_data, student_records_by_id),
        "Add Record": wrap_function(add_record, student_records_by_id),
        "Remove Record": wrap_function(remove_record, student_records_by_id),
        "Modify Record": wrap_function(modify_record, student_records_by_id,
                                       student_records_by_name, names, inverse_index),
        "Sort Records": wrap_function(sort_menu, student_records_by_id),
        "Search For Records": wrap_function(search_menu, student_records_by_id),
    }

    while True:
        menu_choice, menu_response, menu_return = display_menu(main_menu_options, "Save and Exit",
                                                               pre="Choose", final="\n" * 2)
        if menu_choice == -1:
            break

    update_file(student_records_by_id, STUDENT_FILE_NAME)


if __name__ == "__main__":
    main()
