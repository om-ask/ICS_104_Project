def add_record(students:dict[int, dict[str, str or float]]):
    id,name,gpa = get_inputs(students)

    students[id] = {'name' : name, 'gpa': gpa}


def get_inputs(students:dict[int, dict[str, str or float]]) -> int:
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

    return id,name,gpa

