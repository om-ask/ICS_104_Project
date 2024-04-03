def add_record(students):
    stu_id, name, gpa = ask_for_inputs(students)

    students[stu_id] = {'name': name, 'gpa': gpa}

    return students


def ask_for_inputs(students):
    while True:  # ask for id
        id = input("ID: ")
        try:
            id = int(id)
            if id not in list(students.keys()):
                if len(str(id)) == 9:
                    break
                else:
                    print("the ID should be 9 integer numbers")
            else:
                print("the ID is already there")
        except:
            print("the ID should be 9 integer numbers")

    while True:  # ask for name
        name = input("Name: ")
        if len(name.split()) >= 2:
            break
        else:
            print("first and second name please")

    while True:  # ask for gpa
        gpa = input("GPA: ")
        try:
            gpa = float(gpa)
            if 0 <= gpa <= 4:
                break
            else:
                print("the GPA should be a number between 0 and 4")
        except:
            print("the GPA should be a number between 0 and 4")

    return id, name, gpa
