from enum import Enum
from searchInternal import search_names

# noinspection PyArgumentList
Codes = Enum("Code", 'SUCCESS INCONCLUSIVE BACK NO_RETURN')


def add_id_check(student_id_records: dict, response: str) -> tuple[bool, str]:
    student_ids_list = list(student_id_records.keys())
    try:
        student_id = int(response)

    except ValueError:
        return False, "the ID should be 9 integer numbers"

    if len(response) != 9:
        return False, "the ID should be 9 integer numbers"

    if student_id not in student_ids_list:
        return True, ""

    else:
        return False, "the ID is already there"


def id_check(student_id_records: dict, response: str) -> tuple[bool, str]:
    student_ids_list = list(student_id_records.keys())
    try:
        student_id = int(response)

    except ValueError:
        return False, "the ID should be 9 integer numbers"

    if len(response) != 9:
        return False, "the ID should be 9 integer numbers"

    if student_id in student_ids_list:
        return True, ""

    else:
        return False, "the ID is not there"


def gpa_check(response: str) -> tuple[bool, str]:
    try:
        student_gpa = float(response)

    except ValueError:
        return False, "the GPA should be a number between 0 and 4"

    if 0 <= student_gpa <= 4:
        return True, ""
    else:
        return False, "the GPA should be a number between 0 and 4"


def name_check(response: str) -> tuple[bool, str]:
    if len(response.split()) >= 2:
        return True, ""
    else:
        return False, "first and second name please"


# TODO
#   Make this a general function so that we can print menus in an appealing format. The new general function should
#   take a list of dictionaries where each dict is a ROW and each key in the the dict is a COLUMN
#   Use the following to test:
#   >records = [
#   {'id': 123456789, 'name': 'mohammed khalifa', 'gpa': 2.25},
#   {'id': 202312340, 'name': 'khalid ahmed', 'gpa': 3.5},
#   {'id': 202345771, 'name': 'Mohammad Abdu', 'gpa': 0.0}
#   ]
#   >show_data(records)
#   _______________________________________
#   | ID        | Name             | GPA  |
#   _______________________________________
#   | 123456789 | mohammed khalifa | 2.25 |
#   | 202312340 | khalid ahmed     | 3.50 |
#   | 202345771 | Mohammad Abdu    | 0.00 |
#   _______________________________________

def show_data(student_id_records: dict[int, dict[str, str or float]]) -> tuple:
    lines = []

    max_name_length = 0
    for student_record in student_id_records:
        name_length = len(student_id_records[student_record]["name"])
        if name_length > max_name_length:
            max_name_length = name_length

    lines.append("_" * (max_name_length + 23))
    lines.append(f"| ID        | Name{(max_name_length - 4) * ' '} | GPA  |")
    lines.append("_" * (max_name_length + 23))
    for student in student_id_records:
        lines.append(
            f"| {student:8d} | {student_id_records[student]['name']}"
            f"{(max_name_length - len(student_id_records[student]['name'])) * ' '} |"
            f" {student_id_records[student]['gpa']:4.2f} |")
    lines.append("_" * (max_name_length + 23))

    for line in lines:
        print(line)

    return Codes.SUCCESS, Codes.NO_RETURN


# TODO Make code readable for all functions below
def display_menu(options_menu: dict, back_option, pre='', post='', default_question_override='', final='') \
        -> tuple:
    if not default_question_override:
        default_question_override = "Enter a number to choose: "

    if pre:
        print(pre)

    choice_dict = {}
    back_number = 1
    for option_number, option in enumerate(options_menu.keys(), start=1):
        back_number += 1
        choice_dict[option_number] = options_menu[option]
        print(f"{option_number} {option}")

    print(f"{back_number} {back_option}")

    if post:
        print(post)

    while True:
        response = input(default_question_override).strip()
        if not response.isdigit():
            print("Please enter a number only.")
            continue

        response_number = int(response)
        if response_number == back_number:
            return Codes.BACK, response_number, Codes.NO_RETURN

        choice = choice_dict.get(response_number, ...)
        if choice is ...:
            print("Please enter a number that is present.")
            continue

        if final:
            print(final)

        if choice is None:
            return Codes.SUCCESS, response_number, Codes.NO_RETURN

        choice_code, choice_return = choice()
        if choice_code == Codes.BACK:
            return Codes.INCONCLUSIVE, response_number, choice_return

        else:
            return choice_code, response_number, choice_return


def take_inputs(input_prompts: dict) -> tuple:
    print("Type 'cancel' to stop taking input or 'back' to undo.")

    prompts = list(input_prompts.keys())
    results = [''] * len(prompts)

    current_prompt_index = 0
    while current_prompt_index < len(prompts):
        prompt = prompts[current_prompt_index]
        response = input(prompt)

        if response.lower() == "cancel" or (current_prompt_index == 0 and response.lower() == "back"):
            return Codes.BACK, Codes.NO_RETURN

        elif response.lower() == "back":
            current_prompt_index -= 1
            continue

        input_analyzer, input_check = input_prompts[prompt]
        if input_analyzer:
            code, analyzed_response = input_analyzer(response)
            if code == Codes.BACK:
                continue

        else:
            analyzed_response = response

        check_success, check_message = input_check(analyzed_response)
        if check_success:
            results.pop(current_prompt_index)
            results.insert(current_prompt_index, analyzed_response)
            current_prompt_index += 1

        else:
            print(check_message)

    return Codes.SUCCESS, (*results,)


def search_input_analyzer(data: dict, response: str) -> tuple:
    possible_names = search_names(response, data["Names"], data["Inverse Index"])
    results = {data["Name Records"][name]["id"]: {"name": name, "gpa": data["Name Records"][name]["gpa"]}
               for name in possible_names}

    if not results:
        print("No results")
        return Codes.BACK, Codes.NO_RETURN

    # Show data
    show_data(results)

    code, menu_response, menu_return = display_menu({"Choose": None}, "Search Again")

    if code == Codes.SUCCESS:
        return Codes.SUCCESS, input("Enter ID")

    else:
        return code, menu_return


def wrap_function(function, *args):
    def wrapped_function(*args2):
        return function(*args, *args2)

    return wrapped_function


def menu_option(option_text: str, function=None, *args):
    if function:
        return {option_text: wrap_function(function, *args)}
    else:
        return {option_text: None}


def input_prompt(prompt_text: str, check: tuple, analyzer: tuple = ()):
    wrapped_check = wrap_function(check[0], *check[1:])
    if analyzer:
        wrapped_analyzer = wrap_function(analyzer[0], *analyzer[1:])
    else:
        wrapped_analyzer = None

    return {prompt_text: (wrapped_analyzer, wrapped_check)}


def valid_option(input_response: str, option: str, threshold: int) -> bool:
    return NotImplemented  # TODO Implement this


def update_inverse_index(inverse_index: dict[str, list[tuple[str, int]]], iterable) \
        -> dict[str, list[tuple[str, int]]]:
    for i in iterable:
        tokens = i.split()
        for token_index, token in enumerate(tokens):
            token = token.lower()

            inverse_index.setdefault(token, [])
            inverse_index[token].append((i, token_index))

    return inverse_index


if __name__ == "__main__":
    display_menu({**menu_option("Haha"),
                  **menu_option("gogo")},
                 "Back")
