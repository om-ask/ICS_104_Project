def display_menu(options: dict, back_option, pre=None, post=None, default_question_override=None) -> bool:
    if default_question_override:
        input(default_question_override)

    else:
        default_question_override = "Enter a number to choose: "

    if pre:
        print(pre)

    option_number = 0
    for option_number, option in enumerate(options.keys()):
        print(f"{option_number+1} {option}")

    print(f"{option_number + 1} {back_option}")

    if post:
        print(post)

    while True:
        pass


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
            print(check_message)

    return *results,


def wrap_function(function, *args, **kwargs):
    def wrapped_function(*args2, **kwargs2):
        return function(*args, *args2, **kwargs, **kwargs2)

    return wrapped_function


if __name__ == "__main__":
    pass
