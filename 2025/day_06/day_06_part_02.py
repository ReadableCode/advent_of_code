# %%
# Imports #


# %%
# Vars #


def find_col_breaks(ls_strings, debug=False):
    ls_break_indexes = []
    for col_num in range(0, len(ls_strings[0])):
        if debug:
            print(f"checking col: {col_num}")

        not_break_col = False
        for string in ls_strings:
            if string[col_num] != " ":
                if debug:
                    print(f"Found non break at {col_num}")
                not_break_col = True
                break

        if debug:
            print(f"Found break at: {col_num}")
        if not not_break_col:
            ls_break_indexes.append(col_num)

    return ls_break_indexes


def get_text_input_lines(file_path, debug=False):
    with open(file_path, "r") as file:
        text_lines = file.readlines()

    text_lines = [line.replace("\n", "") for line in text_lines]

    if debug:
        print("-------- text file contents --------")
        for text_line in text_lines:
            print(text_line)
        print("------------------------------------")

    ls_break_indexes = find_col_breaks(text_lines)
    if debug:
        print(ls_break_indexes)

    ls_cleaned_row_lists = []
    for text_line in text_lines:
        prev_break_index = 0
        ls_this_line = []
        break_index = 0  # linter
        for break_index in ls_break_indexes:
            if debug:
                print(f"break_index: {prev_break_index}: {break_index}")

            ls_this_line.append(text_line[prev_break_index:break_index])
            prev_break_index = break_index + 1
        ls_this_line.append(text_line[break_index + 1 :])

        ls_cleaned_row_lists.append(ls_this_line)

    return ls_cleaned_row_lists


file_path = "day_06_part_01_input_test.txt"
ls_cleaned_row_lists = get_text_input_lines(file_path, debug=True)
for text_line in ls_cleaned_row_lists:
    print(text_line)


# %%


def get_list_problems(file_path, debug=False):
    ls_cleaned_row_lists = get_text_input_lines(file_path)

    ls_problems = []
    for col_num in range(0, len(ls_cleaned_row_lists[0])):
        if debug:
            print(f"col_num: {col_num}")

        ls_terms_this_problem = []
        for row_num in range(0, len(ls_cleaned_row_lists)):
            if debug:
                print(f"row_num: {row_num}")

            ls_terms_this_problem.append(ls_cleaned_row_lists[row_num][col_num])

        ls_problems.append(ls_terms_this_problem)

    return ls_problems


file_path = "day_06_part_01_input_test.txt"
ls_problems = get_list_problems(file_path, debug=True)
for problem in ls_problems:
    print(problem)


# %%


def get_list_problems_new(file_path, debug=False):
    ls_problems = get_list_problems(file_path)

    ls_problems_new = []
    for problem in ls_problems:
        if debug:
            print(problem)

        symbol = problem[-1].replace(" ", "")
        terms = problem[:-1]

        new_terms = []

        for digit_num in range(0, len(terms[0])):
            new_term = ""
            for term in terms:
                if term[digit_num] == " ":
                    continue
                new_term += term[digit_num]

            new_terms.append(new_term)

        print("new terms")
        print(new_terms)

        ls_problems_new.append(new_terms + [symbol])

    return ls_problems_new


file_path = "day_06_part_01_input_test.txt"
ls_problems = get_list_problems_new(file_path, debug=True)
for problem in ls_problems:
    print(problem)

# Finally, the leftmost problem is 356 * 24 * 1 = 8544


# %%


def solve_problem(problem, debug=False):
    symbol = problem[-1]

    terms = problem[:-1]

    if debug:
        print("terms before")
        print(terms)

    if debug:
        print(f"symbol: {symbol}")
        print(f"terms: {terms}")

    if symbol == "*":
        total = 1
        for term in terms:
            total = total * int(term)
    elif symbol == "+":
        total = 0
        for term in terms:
            total = total + int(term)
    else:
        raise ValueError(f"unknown symbol: {symbol}")

    return total


# %%


def solve_ls_problems(ls_problems, debug=False):
    total_answer = 0
    for problem in ls_problems:
        if debug:
            print(f"---------- problem: {problem} ----------")

        total = solve_problem(problem)

        if debug:
            print(f"total: {total}")

        total_answer = total_answer + total

    return total_answer


file_path = "day_06_part_01_input_test.txt"
ls_problems = get_list_problems_new(file_path, debug=False)
total_answer = solve_ls_problems(ls_problems, debug=True)
print(f"total_answer: {total_answer}")
assert total_answer == 3263827


# %%

file_path = "day_06_part_01_input.txt"
ls_problems = get_list_problems_new(file_path, debug=False)
total_answer = solve_ls_problems(ls_problems, debug=True)
print(f"total_answer: {total_answer}")
assert total_answer == 11708563470209  # part 02 answer


# %%
