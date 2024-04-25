from mainInternal import show_data, RecordsTable


def calculate_average(student_records: RecordsTable):
    try:
        gpa_sum = 0
        for student in student_records.records():
            print(student.name())
            gpa_sum += student.gpa()

        average = gpa_sum / len(student_records.records())

        print("The average is :", average)

    except ZeroDivisionError:
        print("There is no data to calculate the average.")


def top_performing_students(studens_records):
    sorted_student_records: list
    # هنا ابغا زي اللي في sortRecord الlist اللي دخلت في الshow_data
    # ما عرفت استخدم اشياءك اللي حاطها

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
