from showData import *
from readFileToDic import *

STUDENT_FILE_NAME = "students.txt"


def main():
    students = read_file_to_dic(STUDENT_FILE_NAME)

    print(students)

    show_data(students)


main()
