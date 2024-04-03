def remove_record(students:dict[int, dict[str, str or float]]):
    students.pop(get_id(students))


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