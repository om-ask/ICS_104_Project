from readFileToDic import read_file_to_dic
from showData import show_data
from internal import display_menu, wrap_function
from addRecord import add_record
from removeRecord import remove_record
from updateFile import update_file
from modifyRecord import modify_record
from sortRecord import sort_menu

STUDENT_FILE_NAME = "students.txt"


def main():
    # Read students
    student_records = read_file_to_dic(STUDENT_FILE_NAME)

    main_menu_options = {
        "View Records": wrap_function(show_data, student_records),
        "Add Record": wrap_function(add_record, student_records),
        "Remove Record": wrap_function(remove_record, student_records),
        "Modify Record": wrap_function(modify_record, student_records),
        "Sort Records": wrap_function(sort_menu, student_records),
    }

    while display_menu(main_menu_options, "Save and Exit", pre="Choose", final="\n"*2):
        continue

    update_file(student_records, STUDENT_FILE_NAME)


if __name__ == "__main__":
    main()
