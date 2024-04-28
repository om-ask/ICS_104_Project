from mainInternal import show_data, RecordsTable, StudentRecord


def calculate_average(student_records: RecordsTable):
    """Calculate the average of all students
    """
    try:
        gpa_sum = 0

        # Get the sum
        for student in student_records.records():
            gpa_sum += student.gpa()

        # Calculate the average
        average = gpa_sum / len(student_records.records())

        # display the average
        print("The average is: %.2f" % average)

    except ZeroDivisionError:
        # If there is no records for any student
        print("There is no data to calculate the average.")


def top_performing_students(records: RecordsTable):
    """Give the top 3 students
    """
    # Take the students sorted by gpa
    sorted_student_records = sorted(records.records(), key=StudentRecord.gpa, reverse=True)

    counter = 0

    top_students = []
    top_gpas = []

    # To take the first 3 students, and take more if necessary
    for student in sorted_student_records:

        if counter == 3:
            if student.gpa() in top_gpas:
                counter -= 1
            else:
                break

        top_students.append(student)
        top_gpas.append(student.gpa())
        counter += 1

    # Display the top students
    show_data(RecordsTable(top_students).raw())


if __name__ == "__main__":
    pass
