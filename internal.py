def display_menu(options: dict, pre=None, post=None) -> bool:
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

        check_result = input_prompts[prompt](response)
        if check_result:
            results.remove(current_prompt_index)
            results.insert(current_prompt_index, response)
            current_prompt_index += 1

    return results


def wrap_function(function, *args, **kwargs):
    def wrapped_function(*args2, **kwargs2):
        return function(*args, *args2, **kwargs, **kwargs2)

    return wrapped_function
