def display_menu(options: dict, back_option, pre=None, post=None, default_question_override=None, final=None) -> bool:
    if not default_question_override:
        default_question_override = "Enter a number to choose: "

    if pre:
        print(pre)

    back_number = 1
    choice_dict = {}
    for option_number, option in enumerate(options.keys()):
        back_number += 1
        choice_dict[option_number+1] = options[option]
        print(f"{option_number+1} {option}")

    print(f"{back_number} {back_option}")

    if post:
        print(post)

    while True:
        response = input(default_question_override).strip()
        if response.isdigit():
            if int(response) == back_number:
                return False

            choice = choice_dict.get(int(response), None)
            if choice is not None:
                break
            else:
                print("Please enter a number that is present.")

        else:
            print("Please enter a number only.")

    if final:
        print(final)

    return choice()


def take_inputs(input_prompts: dict):
    current_prompt_index = 0
    prompts = list(input_prompts.keys())
    results = [''] * len(prompts)

    print("Type 'cancel' to stop taking input or 'back' to undo.")

    while current_prompt_index < len(prompts):
        prompt = prompts[current_prompt_index]
        response = input(prompt)

        if response.lower() == "cancel":
            return None

        elif response.lower() == "back":
            if current_prompt_index:
                current_prompt_index -= 1
                continue

            else:
                return None

        check_result, check_message = input_prompts[prompt](response)
        if check_result:
            results.pop(current_prompt_index)
            results.insert(current_prompt_index, response)
            current_prompt_index += 1

        else:
            # Erase the previous line and print the message
            print(check_message)

    return *results,


def wrap_function(function, *args, **kwargs):
    def wrapped_function(*args2, **kwargs2):
        return function(*args, *args2, **kwargs, **kwargs2)

    return wrapped_function


if __name__ == "__main__":
    take_inputs({
        "Test me:": lambda r: (False, "blah blah")
    })

