
def levenshtein_distance(string1: str, string2: str, prev_state=None) -> tuple[int, list[int]]:
    if not prev_state:
        previous_row = list(range(0, len(string2) + 1))
        # print('-' * 10)
        # print(*previous_row)
    else:
        previous_row = prev_state

    for j, character1 in enumerate(string1, start=previous_row[0] + 1):
        row = [j]
        for i, character2 in enumerate(string2, start=1):
            cost = min(row[i - 1] + 1, previous_row[i] + 1,
                       previous_row[i - 1] + (1 if character1 != character2 else 0))
            row.append(cost)
        previous_row = row
    # print(*previous_row)
    return previous_row[-1], previous_row


def levenshtein_automaton(w_string: str, sorted_strings, threshold: int, case_sensitive=False) -> tuple[str]:
    w_string = w_string.lower() if not case_sensitive else w_string
    automatons = []
    results = {}
    prev_str = None
    for string in sorted_strings:
        # print("checking", string)
        string = string.lower() if not case_sensitive else string
        auto = []
        i = 0
        for a in range(len(automatons)):
            if a == len(string) or prev_str[a] != string[a]:
                if a:
                    # print("Found auto!", prev_str, string)
                    auto = automatons[a - 1]
                    # print(auto, automatons[a])
                i = a
                break

        automatons = automatons[:i]
        prev_str = string

        if auto and min(auto) > threshold:
            # print("threshold passed for", string)
            continue
        while i < len(w_string) and i < len(string):
            auto = levenshtein_distance(string[i], w_string, auto)[1]
            # print(string[i], auto)
            automatons.append(auto)
            i += 1
            if min(auto) > threshold:
                # print("threshold passed for", string)
                break
        else:
            if i != len(string) or auto[-1] <= threshold:
                results[string] = min(auto)

    print(results)
    return *sorted(results, key=results.get),


def search_names(query: str, names, inverse_index: dict[str, list[tuple[str, int]]]) -> tuple[str]:
    query = query.strip()
    query_names = query.split()
    if len(query_names) == 1:
        possible_names = levenshtein_automaton(query, sorted(inverse_index.keys()), len(query) // 3)
        results = {full_name: order for name in possible_names for full_name, order in inverse_index[name]}
        return *sorted(results, key=results.get),

    else:
        return levenshtein_automaton(query, sorted(names), len(query) // 3)


def search_ids(query: int):
    return NotImplemented
