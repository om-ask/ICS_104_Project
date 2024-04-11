# TODO Make code readable here
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

    for string in sorted_strings:
        string = string.lower() if not case_sensitive else string
        character_index = 0

        while character_index < len(prev_str) and prev_str[character_index] == string[character_index]:
            if prev_str[character_index] != string[character_index] or character_index == len(string):
                edits = automatons[character_index - 1]
                break

            character_index += 1

        else:
            edits = list(range(len(comparison_string) + 1))

        automatons = automatons[:character_index]
        prev_str = string

        # If the minimum amount of edits possible is greater than the threshold, the loop exits into the else clause
        # and the word is not appended into the results
        # If the string ends, the loop exits and the word is not appended unless the total amount of edits is less than
        # the threshold
        while min(edits) <= threshold and character_index < len(string):
            if character_index == len(comparison_string):
                # If the comparison strings ends and the threshold is not exceeded, break and add the word to the
                # results
                break
            edits = calculate_next_levenshtein_row(string[character_index], comparison_string, edits)
            automatons.append(edits)
            character_index += 1

        else:
            if edits[-1] > threshold:
                continue

        # Add the word to results with the minimum possible amount of edits
        results[string] = min(edits)

    return *sorted(results, key=results.get),
