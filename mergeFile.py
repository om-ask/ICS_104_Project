from mainInternal import RecordsTable, read_file_into_record, Back, menu, StudentRecord


def merge_records(current_student_records: RecordsTable):
    """Prompts the user for a new filename, reads the student data, and then merges it with
    the current data. If any conflicts occur while merging, solves conflict according to the
    behaviour the user chooses.
    Supports going back.
    """
    # Read a new file into records
    new_student_records = RecordsTable()
    read_file_into_record(new_student_records)

    # Take behaviour type of merge from user
    print("Choose what to do when encountering info conflicts:")
    behaviour_type = menu(["Ask before merging",
                           "Keep old",
                           "Overwrite old with new"])
    print()

    # Merge new file records into current student records
    for new_record in new_student_records.records():
        try:
            old_record = current_student_records.get_record(student_id=new_record.id())

        except KeyError:
            # The record is not present
            # Add it to the current records table
            current_student_records.add_record(new_record)
            continue  # Move on to the next record

        # If an old record was found, compare its contents to the new record and merge according to behaviour type
        merged_name = old_record.name()
        merged_gpa = old_record.gpa()
        merge = False
        try:
            if old_record.name() != new_record.name():
                if behaviour_type == 1:  # Ask user
                    print("A conflict in names has been detected for id:", old_record.id())
                    print("Old name in current file:", old_record.name())
                    print("New name in new file:", new_record.name())
                    print()
                    print("Choose which name to keep for", old_record.id())
                    choice = menu([old_record.name(),
                                   new_record.name()], back_option="Skip Record")

                    if choice == 1:  # Keep old name
                        merged_name = old_record.name()

                    else:  # Set new name
                        merged_name = new_record.name()
                        merge = True

                elif behaviour_type == 2:  # Keep old
                    merged_name = old_record.name()

                else:  # Overwrite old with new
                    merged_name = new_record.name()
                    merge = True

            if old_record.gpa() != new_record.gpa():
                if behaviour_type == 1:  # Ask user
                    print(f"A conflict in gpa has been detected for {merged_name} with id:", old_record.id())
                    print("Old gpa in current file:", old_record.gpa())
                    print("New gpa in new file:", new_record.gpa())
                    print()
                    print(f"Choose which gpa to keep for {merged_name}")
                    choice = menu([str(old_record.gpa()),
                                   str(new_record.gpa())], back_option="Skip Record")

                    if choice == 1:  # Keep old name
                        merged_gpa = old_record.gpa()

                    else:  # Set new name
                        merged_gpa = new_record.gpa()
                        merge = True

                elif behaviour_type == 2:  # Keep old
                    merged_gpa = old_record.gpa()

                else:  # Overwrite old with new
                    merged_gpa = new_record.gpa()
                    merge = True

            # If any merge was required, create a new record with the merged contents and add it to the table

            if merge:
                merged_record = StudentRecord(old_record.id(), merged_name, merged_gpa)

                # Delete old record
                current_student_records.remove_record(old_record)

                # Add new merged record
                current_student_records.add_record(merged_record)

            else:
                # Otherwise don't add anything
                pass

        except Back:
            # If the user goes back, skip adding the record
            print("Skipping", new_record.id())

    print("Finished merging from file:", new_student_records.filename)
