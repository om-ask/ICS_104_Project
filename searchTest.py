def update_inverse_index(inverse_index: dict[str, list[tuple[str, int]]], iterable, sep=" ", skip_tokens=None) \
        -> dict[str, list[tuple[str, int]]]:
    for i in iterable:
        if sep:
            tokens = i.split(sep)
        else:
            tokens = list(i)

        for token_index, token in enumerate(tokens):
            if skip_tokens is not None and token in skip_tokens:
                continue

            inverse_index.setdefault(token, [])
            inverse_index[token].append((i, token_index))

    return inverse_index


def create_names_inverse_index(full_names: set[str]) -> dict[str, list[tuple[str, int]]]:
    return update_inverse_index({}, full_names)


def levenshtein_distance(string1: str, string2: str, prev_state=None) -> tuple[int, list[int]]:
    if not prev_state:
        previous_row = list(range(0, len(string2) + 1))
    else:
        previous_row = prev_state

    for j, character1 in enumerate(string1, start=previous_row[0]+1):
        print(*previous_row)
        row = [j]
        for i, character2 in enumerate(string2, start=1):
            cost = min(row[i - 1] + 1, previous_row[i] + 1, previous_row[i-1] + (1 if character1 != character2 else 0))
            row.append(cost)
        previous_row = row
    print(*previous_row)
    return previous_row[-1], previous_row


def levenshtein_automaton(w_string: str, sorted_strings, threshold: int) -> tuple[str]:
    automatons = []
    results = []
    prev_str = None
    for string in sorted_strings:
        auto = []
        i = 0
        for a in range(len(automatons)):
            if a == len(string) or prev_str[a] != string[a]:
                if a:
                    auto = automatons[a-1]
                i = a
                break

        automatons = automatons[:i]
        while i < len(w_string) and i < len(string):
            if auto and min(auto) > threshold:
                break
            auto = levenshtein_distance(string[i], w_string, auto)[1]
            automatons.append(auto)
            i += 1
        else:
            results.append(string)

        prev_str = string

    return *results,


#
# def create_names_inverse_index(full_names: set[str]) \
#         -> tuple[dict[str, list[tuple[str, int]]], dict[str, list[tuple[str, int]]]]:
#     names = {name for full_name in full_names for name in full_name.split()}
#     return update_inverse_index({}, names, skip_tokens=' '), update_inverse_index({}, full_names, sep=" ")
#
#
# def update_names_inverse_index(
#         full_names: set[str],
#         names_inverse_index: tuple[dict[str, list[tuple[str, int]]], dict[str, list[tuple[str, int]]]]) \
#         -> tuple[dict[str, list[tuple[str, int]]], dict[str, list[tuple[str, int]]]]:
#     names = {name for full_name in full_names for name in full_name.split()}
#     return (update_inverse_index(names_inverse_index[0], names, skip_tokens=' '),
#             update_inverse_index(names_inverse_index[1], full_names, sep=" "))
#
#
# def search_names(names_inverse_index: tuple[dict[str, list[tuple[str, int]]], dict[str, list[tuple[str, int]]]],
#                  search_term: str, n_terms: int = -1) -> tuple[str, ...]:
#     letter_index, word_index = names_inverse_index
#
#     letter_ranking = {}
#     letter_previous_index = {}
#     for i, letter in enumerate(search_term):
#         possible_names = letter_index.get(letter, [])
#         if i:
#             prev_letter = search_term[i - 1]
#         else:
#             prev_letter = None
#
#         for name, l_ind in possible_names:
#             previous_index = letter_previous_index.get(name, None)
#             if previous_index is None:
#                 previous_index = [(l_ind, letter)]
#                 letter_previous_index[name] = previous_index
#
#             elif prev_letter:
#                 for n, (l_index, term) in enumerate(previous_index):
#                     if term[-1] == prev_letter and l_index + len(term) == l_ind:
#                         previous_index[n] = (l_index, term + letter)
#                         break
#
#                 else:
#                     pass
#                     # previous_index.append((l_ind, letter))
#
#             else:
#                 previous_index.append((l_ind, letter))
#
#             longest_term = max([x[1] for x in previous_index], key=len)
#             letter_ranking[name] = len(longest_term)
#
#     if len(search_term) > 1:
#         top_ranking = sorted({n: c for n, c in letter_ranking.items() if c > 1}, key=letter_ranking.get, reverse=True)
#
#     else:
#         top_ranking = sorted(letter_ranking, key=letter_ranking.get, reverse=True)
#
#     name_ranking = {}
#     for r, name in enumerate(top_ranking):
#         if r == n_terms:
#             break
#         possible_names = word_index.get(name, [])
#         for possible_name in possible_names:
#             name_ranking[possible_name[0]] = name_ranking.get(name, 0) + 1
#
#     return *name_ranking.keys(),


if __name__ == "__main__":
    list_of_searches = ["omar hf", "khalifa mohammed", "hashem khalifa", "krater omar", "kalifa moh", "mohammad abdu"]
    full_index = create_names_inverse_index(set(list_of_searches))
    print(levenshtein_automaton("kha", list_of_searches, 1))
