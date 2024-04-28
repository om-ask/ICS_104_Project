def calculate_next_levenshtein_row(character1: str, main_string: str, previous_row: list) -> list[int]:
    """Calculates the next levenshtein row according to the levenshtein algorithm.
    A character from a string, the main string to compare it against, and the previous row need to be provided.
    """
    # The column number is the first number in the previous row
    starting_column = previous_row[0] + 1
    # Set the first number in the new row to the previous row's column number + 1
    next_row: list = [starting_column, ]

    # Loop over every character in the main string while comparing it the character1
    for column_number, character2 in enumerate(main_string, start=1):
        # Apply the levenshtein algorithm to calculate the next element in the row
        next_row.append(min(
            next_row[column_number - 1] + 1,
            previous_row[column_number] + 1,
            previous_row[column_number - 1] + (character1 != character2)))

    # Return the next row
    return next_row


def levenshtein_automaton(comparison_string: str, sorted_strings, threshold: int, case_sensitive=False) -> tuple[str]:
    """Basically a search function.
    This is an optimized algorithm that takes a list of strings and compares them against a
    comparison string. It discards any strings that are less similar than a given threshold.
    The list of strings should be sorted for maximum speed.
    """
    if not comparison_string or not sorted_strings:
        return tuple()
    # Set the comparison string to lowercase if not case-sensitive
    comparison_string = comparison_string.lower() if not case_sensitive else comparison_string

    # Initialise the results dictionary
    results = {}

    # A list to store previously calculated levenshtein rows
    automatons = []

    # Initialise the previous string to use when optimizing
    prev_str = ''

    # Loop over every string in the sorted strings and compare them against the comparison string
    # Add each string to results that is similar to the comparison string
    for original_string in sorted_strings:
        # Set the string to lowercase if not case-sensitive
        string = original_string.lower() if not case_sensitive else original_string

        # Start from the first index of the string
        character_index = 0

        # The following loop is an optimization to skip any characters in the string that were already
        # previously calculated
        # It sets the edits to a previously calculated levenshtein row in the automatons list
        # Loop if the there is a previous string and if the letters are identical in both the prev and current string
        while prev_str and prev_str[character_index] == string[character_index]:
            # Move to the next character
            character_index += 1

            # If the next character is not identical or the end of either string is reached, break out of loop
            if (character_index == len(automatons) or character_index == len(string)
                    or prev_str[character_index] != string[character_index]):
                # Set the current edits to the previous character
                edits = automatons[character_index - 1]
                break

        else:
            # If no similarity between the current string and the previous string is present, or there is no prev string
            # then initialise edits to a default starting levenshtein row
            edits = list(range(len(comparison_string) + 1))

        # Cut out the levenshtein rows that are no longer useful
        automatons = automatons[:character_index]

        # Update the previous string for the next iteration of the loop
        prev_str = string

        # If the minimum amount of edits possible is greater than the threshold, the loop exits
        # and the word is not appended into the results
        # If the string ends, the loop exits and the word is not appended unless the total amount of edits is less than
        # the threshold
        while min(edits) <= threshold and character_index < len(string) and character_index < len(comparison_string):
            # If the comparison strings ends and the threshold is not exceeded, break and add the word to the
            # results
            edits = calculate_next_levenshtein_row(string[character_index], comparison_string, edits)

            # Add the calculated row to automatons for possible optimization
            automatons.append(edits)

            # Move to next character
            character_index += 1

        # The final index in edits is the total number of edits required
        if edits[-1] > threshold:
            # If the total number of edits required for the current string to be equal to comparison string is greater
            # than the threshold, skip to next string
            continue

        # Add the word to results with the minimum possible amount of edits (similarity)
        results[original_string] = min(edits)

    # Return a tuple of the results sorted by the edit number (Lower edits means more similar)
    return *sorted(results, key=results.get),
