from mainInternal import wrap_function, display_menu
from showData import show_data


def sort_menu(student_records: dict) -> tuple:
    sort_menu_options = {
        "Sort By ID": wrap_function(sort_by_id, student_records),
        "Sort By GPA": wrap_function(sort_by_gpa, student_records)
    }

    display_menu(sort_menu_options, "Back", pre="Choose sort type:", final="\n"*2)

    return 0, None


def sort_by_id(student_records: dict) -> tuple:
    student_records = {k: v for k, v in sorted(student_records.items())}
    show_data(student_records)

    return 0, None


def sort_by_gpa(student_records: dict) -> tuple:
    student_records = {k: v for k, v in sorted(student_records.items(), key=lambda v: v[1]['gpa'], reverse=True)}
    show_data(student_records)

    return 0, None


if __name__ == "__main__":
    from fileOperations import read_file_to_data

    STUDENT_FILE_NAME = "students.txt"
    # test_student_records = read_file_to_data(,
    show_data(test_student_records)
    sort_by_id(test_student_records)

    sort_by_gpa(test_student_records)
