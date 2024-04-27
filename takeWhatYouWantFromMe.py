from mainInternal import show_data, RecordsTable, StudentRecord


def calculate_average(student_records: RecordsTable):
    try:
        gpa_sum = 0
        for student in student_records.records():
            gpa_sum += student.gpa()

        average = gpa_sum / len(student_records.records())

        print("The average is :", average)

    except ZeroDivisionError:
        print("There is no data to calculate the average.")


def top_performing_students(records: RecordsTable):
    sorted_student_records = sorted(records.records(), key=StudentRecord.gpa, reverse=True)

    # هنا ابغا زي اللي في sortRecord الlist اللي دخلت في الshow_data
    # ما عرفت استخدم اشياءك اللي حاطها

    counter = 0

    top_students = []
    top_gpas = []

    for student in sorted_student_records:

        if counter == 3:
            if student.gpa() in top_gpas:
                counter -= 1
            else:
                break

        top_students.append(student)
        top_gpas.append(student.gpa())
        counter += 1

    show_data(RecordsTable(top_students).raw())


if __name__ == "__main__":
    pass
