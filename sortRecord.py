from mainInternal import display_menu, show_data, Codes, menu_option


def sort_menu(data: dict) -> tuple:
    sort_menu_options = {
        **menu_option("Sort by ID", sort_by_id, data),
        **menu_option("Sort by GPA", sort_by_gpa, data),
    }

    code, menu_response, menu_return = display_menu(sort_menu_options, "Back", pre="Choose sort type:", final="\n" * 2)

    return code, menu_return


def sort_by_id(data: dict, descending=False) -> tuple:
    sorted_student_records = {student_id: student_record
                              for student_id, student_record
                              in sorted(data["ID Records"].items(), reverse=descending)}

    show_data(sorted_student_records)
    return Codes.SUCCESS, Codes.NO_RETURN


def sort_by_gpa(data: dict, descending=True) -> tuple:
    def gpa(student_info):
        student_id = student_info[0]
        return data["ID Records"][student_id]["gpa"]

    sorted_student_records = {student_id: student_record
                              for student_id, student_record
                              in sorted(data["ID Records"].items(), key=gpa, reverse=descending)}

    show_data(sorted_student_records)
    return Codes.SUCCESS, Codes.NO_RETURN


if __name__ == "__main__":
    from fileOperations import read_file

    STUDENT_FILE_NAME = "students.txt"
    test_data = read_file(STUDENT_FILE_NAME)
    test_student_records = test_data["ID Records"]

    show_data(test_student_records)
    sort_by_id(test_student_records)

    sort_by_gpa(test_student_records)
