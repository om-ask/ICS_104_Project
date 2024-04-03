from internal import wrap_function
from showData import show_data


def sort_menu(student_records):
    sort_menu_options = {
        "Sort By ID": wrap_function(sort_by_id, student_records),
        "Sort By GPA": wrap_function(sort_by_gpa, student_records)
    }

    pass


def sort_by_id(student_records):
    student_records = {k: v for k, v in sorted(student_records.items())}
    show_data(student_records)


def sort_by_gpa(student_records):
    student_records = {k: v for k, v in sorted(student_records.items(), key=lambda v: v[1]['gpa'], reverse=True)}
    show_data(student_records)


if __name__ == "__main__":
    from readFileToDic import read_file_to_dic

    STUDENT_FILE_NAME = "students.txt"
    student_records = read_file_to_dic(STUDENT_FILE_NAME)
    show_data(student_records)
    sort_by_id(student_records)

    sort_by_gpa(student_records)
