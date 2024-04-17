from mainInternal import StudentRecord, show_data, RecordsTable
from sortRecord import sort_records

def calculate_average(studens_records):
    gpas = []

    for student in studens_records:
        gpas.append(student["GPA"])

    average = sum(gpas) / len(gpas)




def top_performing_students(studens_records):
    sorted_student_records:list
    #هنا ابغا زي اللي في sortRecord الlist اللي دخلت في الshow_data
    #ما عرفت استخدم اشياءك اللي حاطها

    counter = 0

    top_students = []
    top_gpas = []

    for student in sorted_student_records:

        if counter == 3:
            if student["GPA"] in top_gpas:
                counter -= 1
            else:
                break

        top_students.append(student)
        top_gpas.append(student["GPA"])
        counter += 1

    show_data(top_students)

if __name__ == "__main__":
    pass