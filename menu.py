def display_menu(options: dict, pre=None, post=None) -> bool:
    pass


def take_inputs(input_prompts: dict):
    results = []
    current_prompt_index = 0
    prompts = list(input_prompts.keys())

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

        check_result = input_prompts[prompt]
        if check_result:
            results.append(response)
            current_prompt_index += 1

    return results


def wrap_function(function, *args):
    def wrapped_function():
        arguments = args
        return function(*arguments)

    return wrapped_function




inputs = {
    "Enter student id": check1,
    "Enter student name:": check2,
    "Enter student gpa": check3,
}

take_inputs(inputs)

