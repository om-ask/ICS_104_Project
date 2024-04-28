from mainInternal import RecordsTable, Inputs, StudentRecord, show_data, valid_name_check, valid_gpa_check, menu, Back


def add_record(student_records: RecordsTable):
    """Prompts the user for new student info and then adds it to the given records table
    Supports going back
    """
    show_data(student_records.raw())

    # Define an input for taking student info
    inputs = Inputs()
    inputs.add_prompt("Enter ID:", student_records.new_id_check)
    inputs.add_prompt("Enter Name:", valid_name_check)
    inputs.add_prompt("Enter GPA:", valid_gpa_check)

    # Take the inputs
    input_return = inputs.take_inputs()

    # Extract the user's response
    student_id, student_name, student_gpa = int(input_return[0]), input_return[1], float(input_return[2])

    # Create a new StudentRecord with the info the user gave
    new_record = StudentRecord(student_id, student_name, student_gpa)

    # Add it to the records table
    student_records.add_record(new_record)

    print("Successfully added student.")


def remove_record(student_records: RecordsTable):
    """Prompts the user for a student to delete from the given records table and removes it if found
    Supports going back
    """
    # Loop until the user goes back or the remove is successful
    while True:
        # Show the records table so that the user can see the current student info
        show_data(student_records.raw())

        # Allow the user to choose the method of choosing a student to remove
        print("Choose a student to modify:")
        choice_number = menu(["By Searching For a Student",
                              "By ID"])

        # Each method takes different input prompts
        if choice_number == 1:  # Option Searching for Student
            # Define an input for searching for a student to remove
            inputs = Inputs()
            inputs.add_prompt("Search:", student_records.present_id_check, analyzer=student_records.search_analyzer)

        else:  # Option By ID:
            # Define an input for taking a present student id
            inputs = Inputs()
            inputs.add_prompt("Enter ID:", student_records.present_id_check)

        try:
            # Take the input from the user and convert into an integer
            student_id = int(inputs.take_inputs())
        except Back:
            # If the user goes back here, return to the choice menu at the beginning
            continue  # Retry

        # Get the record from the records table
        record_to_remove = student_records.get_record(student_id=student_id)

        # Remove the record from the records table
        student_records.remove_record(record_to_remove)

        # Exit
        return


def modify_record_menu(student_records: RecordsTable):
    """Prompts user for a student to modify the gpa of
    Supports going back
    """
    # Loop until the user goes back or the modification is successful
    while True:
        # Show the records table so that the user can see the current student info
        show_data(student_records.raw())

        # Allow the user to choose the method of choosing a student
        print("Choose a student to modify:")
        choice_number = menu(["By Searching For a Student",
                              "By ID"])

        # Each method takes different input prompts
        if choice_number == 1:  # Option Searching for Student
            # Define an input for searching for a student then taking a new valid gpa to modify to
            inputs = Inputs()
            inputs.add_prompt("Search:", student_records.present_id_check, analyzer=student_records.search_analyzer)
            inputs.add_prompt("Enter GPA:", valid_gpa_check)

        else:  # Option By ID:
            # Define an input for taking a present student id and a new valid gpa to modify to
            inputs = Inputs()
            inputs.add_prompt("Enter ID:", student_records.present_id_check)
            inputs.add_prompt("Enter GPA:", valid_gpa_check)

        try:
            # Take the input from the user
            input_response = inputs.take_inputs()
        except Back:
            # If the user goes back here, return to the choice menu at the beginning
            continue  # Retry

        # Get the id and gpa from the user's response
        student_id, student_gpa = int(input_response[0]), float(input_response[1])

        # Get the StudentRecord from the records table using the id the user provided
        record_to_modify = student_records.get_record(student_id=student_id)

        # Modify to StudentRecord's GPA to the new value the user provided
        record_to_modify.modify_gpa(student_gpa)

        # Exit
        return


if __name__ == "__main__":
    STUDENT_FILE_NAME = "students2.txt"
    # Create student records and read from file
    records = RecordsTable()
    records.read_file(STUDENT_FILE_NAME)

    show_data(records.raw())
    add_record(records)
    show_data(records.raw())

    show_data(records.raw())
    modify_record_menu(records)
    show_data(records.raw())

    show_data(records.raw())
    remove_record(records)
    show_data(records.raw())
