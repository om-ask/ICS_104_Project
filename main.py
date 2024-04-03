from readFileToDic import read_file_to_dic
from showData import show_data
from menu import display_menu, wrap_function

STUDENT_FILE_NAME = "students.txt"


def main():
    # Read students
    student_records = read_file_to_dic(STUDENT_FILE_NAME)

    main_menu_options = {
        "View Records": wrap_function(show_data, student_records),
        "Add Record": wrap_function(add_record, student_records),
        "Remove Record": wrap_function(remove_record, student_records),
        "Modify Record": wrap_function(modify_record, student_records),
        "Sort Records": wrap_function(sort_records, student_records)
    }

    display_menu(main_menu_options, "Choose:", "Thank you")

    while display_menu(main_menu_options):
        continue


if __name__ == "__main__":
    main()
