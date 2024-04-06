from searchInternal import search_names
from showData import show_data


def id_check(students, student_id) -> tuple[bool, str]:
    try:
        student_id = int(student_id)
        if len(str(student_id)) == 9:
            if student_id in list(students.keys()):
                return True, ""
            else:
                return False, "the ID is not there"
        else:
            return False, "the ID should be 9 integer numbers"

    except ValueError:
        return False, "the ID should be 9 integer numbers"


def gpa_check(gpa) -> tuple[bool, str]:
    try:
        gpa = float(gpa)
        if 0 <= gpa <= 4:
            return True, ""
        else:
            return False, "the GPA should be a number between 0 and 4"
    except ValueError:
        return False, "the GPA should be a number between 0 and 4"


def name_check(name) -> tuple[bool, str]:
    if len(name.split()) >= 2:
        return True, ""
    else:
        return False, "first and second name please"


def display_menu(options: dict, back_option, pre=None, post=None, default_question_override=None, final=None) -> tuple:
    if not default_question_override:
        default_question_override = "Enter a number to choose: "

    if pre:
        print(pre)

    back_number = 1
    choice_dict = {}
    for option_number, option in enumerate(options.keys()):
        back_number += 1
        choice_dict[option_number + 1] = options[option]
        print(f"{option_number + 1} {option}")

    print(f"{back_number} {back_option}")

    if post:
        print(post)

    while True:
        response = input(default_question_override).strip()
        if response.isdigit():
            if int(response) == back_number:
                return -1, -1, None

            choice = choice_dict.get(int(response), None)
            if choice is not None:
                break
            else:
                print("Please enter a number that is present.")

        else:
            print("Please enter a number only.")

    if final:
        print(final)

    return int(response), *choice()


def take_inputs(input_prompts: dict) -> tuple:
    current_prompt_index = 0
    prompts = list(input_prompts.keys())
    results = [''] * len(prompts)

    print("Type 'cancel' to stop taking input or 'back' to undo.")

    while current_prompt_index < len(prompts):
        prompt = prompts[current_prompt_index]
        response = input(prompt)

        if response.lower() == "cancel":
            return -1, None

        elif response.lower() == "back":
            if current_prompt_index:
                current_prompt_index -= 1
                continue

            else:
                return -1, None

        check_result, check_message = input_prompts[prompt](response)
        if check_result:
            results.pop(current_prompt_index)
            results.insert(current_prompt_index, response)
            current_prompt_index += 1

        else:
            # Erase the previous line and print the message
            print(check_message)

    return 0, (*results, )


def search_input(names, student_records_by_name, index) -> tuple:
    print("Type 'cancel' to stop taking input or 'back' to undo.")
    print(names)
    while True:
        search_query = input("Search: ")
        if search_query.lower() == "cancel" or search_query.lower() == "back":
            return -1, None

        possible_names = search_names(search_query, names, index)
        results = {student_records_by_name[name]["id"]: {"name": name, "gpa": student_records_by_name[name]["gpa"]}
                   for name in possible_names}
        if not results:
            print("No results")
            continue
        # Show data
        show_data(results)
        menu_choice, menu_response, student_id = display_menu({
            "Choose": wrap_function(take_inputs, {"Enter ID:": wrap_function(id_check, results)})}, "Search Again")

        if menu_response == -1:
            continue

        # print(menu_response)

        return 0, int(student_id[0])


def wrap_function(function, *args, **kwargs):
    def wrapped_function(*args2, **kwargs2):
        return function(*args, *args2, **kwargs, **kwargs2)

    return wrapped_function


def valid_option(input_response: str, option: str, threshold: int) -> bool:
    return NotImplemented


def update_inverse_index(inverse_index: dict[str, list[tuple[str, int]]], iterable, sep=" ", skip_tokens=None) \
        -> dict[str, list[tuple[str, int]]]:
    for i in iterable:
        if sep:
            tokens = i.split(sep)
        else:
            tokens = list(i)

        for token_index, token in enumerate(tokens):
            token = token.lower()
            if skip_tokens is not None and token in skip_tokens:
                continue

            inverse_index.setdefault(token, [])
            inverse_index[token].append((i, token_index))

    return inverse_index


if __name__ == "__main__":
    take_inputs({
        "Test me:": lambda r: (False, "blah blah")
    })

