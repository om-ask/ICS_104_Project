from mainInternal import take_inputs, gpa_check, name_check, id_check, search_input_analyzer, \
    display_menu, show_data, add_id_check, update_inverse_index, Codes, menu_option, input_prompt


def add_record(data: dict) -> tuple:

    code, record_info = take_inputs({
        **input_prompt("Enter ID:", (add_id_check, data["ID Records"])),
        **input_prompt("Enter Name:", (name_check,)),
        **input_prompt("Enter ID:", (gpa_check,)),
    })

    if code == Codes.SUCCESS:
        student_id = int(record_info[0])
        student_name = record_info[1]
        student_gpa = float(record_info[2])

        data["Records"].append({"id": student_id, "name": student_name, "gpa": student_gpa})
        data["ID Records"][student_id] = {"name": student_name, "gpa": student_gpa}
        data["Name Records"][student_name] = {"id": int(student_id), "gpa": student_gpa}
        data["Names"].add(student_name)

        update_inverse_index(data["Inverse Index"], (student_name,))

    return code, record_info


def remove_record(data: dict) -> tuple:
    code, record_info = take_inputs({
        **input_prompt("Enter ID:", (add_id_check, data["ID Records"])),
    })

    if code == Codes.SUCCESS:
        student_id = int(record_info[0])
        student_name = data["ID Records"][student_id]["name"]

        data["ID Records"].pop(student_id)
        data["Name Records"].pop(student_name)
        data["Names"].remove(student_name)
        # data["Names"] &= set(data["Name Records"].keys())
        for record in data["Records"]:
            if record["id"] == student_id:
                data["Records"].remove(record)
                break

    return code, record_info


def modify_by_search(data) -> tuple:
    return take_inputs({
        **input_prompt("Search: ", check=(id_check, data["ID Records"]), analyzer=(search_input_analyzer, data)),
        **input_prompt("Enter GPA: ", check=(gpa_check,))
    })


def modify_by_id(data) -> tuple:
    return take_inputs({
        **input_prompt("Enter ID: ", check=(id_check, data["ID Records"])),
        **input_prompt("Enter GPA: ", check=(gpa_check,))
    })


def modify_record_menu(data) -> tuple:
    show_data(data["ID Records"])

    modify_menu = {
        **menu_option("By Searching For a Student", modify_by_search, data),
        **menu_option("By ID", modify_by_id, data),
    }

    code, menu_response, menu_return = display_menu(modify_menu, "Back")

    if code == Codes.SUCCESS:
        student_id, student_gpa = int(menu_return[0]), float(menu_return[1])
        student_name = data["ID Records"][student_id]["name"]

        data["ID Records"][student_id]["gpa"] = student_gpa
        data["Name Records"][student_name]["gpa"] = student_gpa
        for record in data["Records"]:
            if record["id"] == student_id:
                record["gpa"] = student_gpa
                break

    return code, menu_return


if __name__ == "__main__":
    from fileOperations import read_file

    STUDENT_FILE_NAME = "students.txt"
    test_data = read_file(STUDENT_FILE_NAME)
    test_student_records = test_data["ID Records"]

    show_data(test_student_records)
    add_record(test_student_records)
    show_data(test_student_records)

    show_data(test_student_records)
    modify_record_menu(test_student_records)
    show_data(test_student_records)

    show_data(test_student_records)
    remove_record(test_student_records)
    show_data(test_student_records)
