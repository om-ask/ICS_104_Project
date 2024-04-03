from menu import take_inputs, wrap_function

def id_check(id, students) -> bool:
    try:
        id = int(id)
        if len(str(id)) == 9:
            if id not in list(students.keys()):
                return True
            else:
                print("the ID is already there")
        else:
            print("the ID should be 9 integer numbers")
    except:
        print("the ID should be 9 integer numbers")

    return False


def name_check(name) -> bool:
    if len(name.split()) >= 2:
        return True
    else:
        print("first and second name please")

    return False


def gpa_check(gpa) -> bool:
    try:
        gpa = float(gpa)
        if 0 <= gpa <= 4:
            return True
        else:
            print("the GPA should be a number between 0 and 4")
    except:
        print("the GPA should be a number between 0 and 4")

    return False


def add_record(students):

    record_info = take_inputs({
        "Enter ID:": wrap_function(id_check, students=students),
        "Enter Name": name_check,
        "Enter GPA": gpa_check
    })

    if record_info:
        id, name, gpa = record_info
        students[id] = {'name': name, 'gpa': gpa}

        return students

    else:
        return None



