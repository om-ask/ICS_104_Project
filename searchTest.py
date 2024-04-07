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
    from mainInternal import update_inverse_index
    from searchInternal import search_names
    # noinspection SpellCheckingInspection

    list_of_searches = ["omar hf", "khalifa mohammed", "hashem khalifa", "krater omar", "kalifa moh", "mohammad abdu"]

    full_index = update_inverse_index({}, set(list_of_searches))
    sorted_names = sorted(list_of_searches)

    print(sorted_names)

    while True:
        test_query = input("Search: ")
        print(len(test_query) // 3)
        print("Search Results:", search_names(test_query, sorted_names, full_index))
