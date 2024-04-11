# TODO Make code readable here (thenextyay)
def calculate_next_levenshtein_row(character1: str, main_string: str, previous_row: list) -> list[int]:
    starting_column = previous_row[0] + 1
    next_row: list = [starting_column, ]

    for column_number, character2 in enumerate(main_string, start=1):
        next_row.append(min(
            next_row[column_number - 1] + 1,
            previous_row[column_number] + 1,
            previous_row[column_number - 1] + (character1 != character2)))

    return next_row


def levenshtein_automaton(comparison_string: str, sorted_strings, threshold: int, case_sensitive=False) -> tuple[str]:
    comparison_string = comparison_string.lower() if not case_sensitive else comparison_string
    automatons = []
    results = {}
    prev_str = ''

    for original_string in sorted_strings:
        string = original_string.lower() if not case_sensitive else original_string
        character_index = 0

        while prev_str and prev_str[character_index] == string[character_index]:
            character_index += 1

            if prev_str[character_index] != string[character_index] or character_index == len(string) or\
                    character_index == len(automatons):
                edits = automatons[character_index - 1]
                break

        else:
            edits = list(range(len(comparison_string) + 1))

        automatons = automatons[:character_index]
        prev_str = string

        # If the minimum amount of edits possible is greater than the threshold, the loop exits into the else clause
        # and the word is not appended into the results
        # If the string ends, the loop exits and the word is not appended unless the total amount of edits is less than
        # the threshold
        while min(edits) <= threshold and character_index < len(string) and character_index < len(comparison_string):
            # If the comparison strings ends and the threshold is not exceeded, break and add the word to the
            # results
            edits = calculate_next_levenshtein_row(string[character_index], comparison_string, edits)
            automatons.append(edits)
            character_index += 1

        if edits[-1] > threshold:
            continue

        # Add the word to results with the minimum possible amount of edits
        results[original_string] = min(edits)

    return *sorted(results, key=results.get),
