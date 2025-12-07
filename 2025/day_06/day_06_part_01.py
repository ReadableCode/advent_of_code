# %%
# Imports #


# %%
# Vars #


def get_text_input_lines(file_path, debug=False):
    with open(file_path, "r") as file:
        text_lines = file.readlines()

    text_lines = [line.strip() for line in text_lines]

    if debug:
        print("-------- text file contents --------")
        for text_line in text_lines:
            print(text_line)
        print("------------------------------------")

    ls_cleaned_row_lists = []
    for row in text_lines:
        if debug:
            print(row)

        ls_cleaned_row_lists.append(row.split())

    return ls_cleaned_row_lists


def get_problems(file_path, debug=False):
    ls_problems = []

    ls_cleaned_row_lists = get_text_input_lines(file_path)

    for row in ls_cleaned_row_lists:
        if debug:
            print(row)

    for col_num in range(0, len(ls_cleaned_row_lists[0])):
        if debug:
            print(f"col_num: {col_num}")
        parts_this_problem = []
        for row_num in range(0, len(ls_cleaned_row_lists)):
            if debug:
                print(f"row_num: {row_num}")
            parts_this_problem.append(ls_cleaned_row_lists[row_num][col_num])

        ls_problems.append(parts_this_problem)

    return ls_problems


def solve_problem(problem, debug=False):
    symbol = problem[-1]

    terms = problem[:-1]

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


problem = ["123", "45", "6", "*"]
answer = solve_problem(problem)
assert answer == 33210

problem = ["328", "64", "98", "+"]
answer = solve_problem(problem)
assert answer == 490

problem = ["51", "387", "215", "*"]
answer = solve_problem(problem)
assert answer == 4243455

problem = ["64", "23", "314", "+"]
answer = solve_problem(problem)
assert answer == 401


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
ls_problems = get_problems(file_path, debug=False)
total_answer = solve_ls_problems(ls_problems, debug=True)
print(f"total_answer: {total_answer}")
assert total_answer == 4277556


file_path = "day_06_part_01_input.txt"
ls_problems = get_problems(file_path, debug=False)
total_answer = solve_ls_problems(ls_problems, debug=True)
print(f"total_answer: {total_answer}")
assert total_answer == 4277556  # part 01 answer


# %%
