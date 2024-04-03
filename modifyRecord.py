def modify_record(students:dict[int, dict[str, str or float]]):
    id = get_id(students)
    gpa = get_gpa()
    students[id]["gpa"] = gpa


def get_id(students:dict[int, dict[str, str or float]]) -> int:
    while True:  # ask for id
        id = input("ID: ")
        try:
            id = int(id)
            if len(str(id)) == 9:
                if id in list(students.keys()):
                    break
                else:
                    print("the ID is not there")
            else:
                print("the ID should be 9 integer numbers")
        except:
            print("the ID should be 9 integer numbers")

    return id

def get_gpa() -> float:
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

    return gpa
