from readFileToDic import read_file_to_dic
from showData import show_data
from  modifyRecord import modify_record
from updateFile import update_file


STUDENT_FILE_NAME = "students.txt"

student_records = read_file_to_dic(STUDENT_FILE_NAME)

show_data(student_records)

modify_record(student_records)

show_data(student_records)

update_file(student_records,STUDENT_FILE_NAME)