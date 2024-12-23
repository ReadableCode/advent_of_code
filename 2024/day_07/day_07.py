# %%
# Imports #

from itertools import product

from tqdm import tqdm

# %%
# Vars #


def get_text_input_lists(file_path):
    with open(file_path, "r") as file:
        text_lines = file.readlines()

    text_lines = [line.strip() for line in text_lines]

    return text_lines


# %%
# Funcs #


def pprint_ls(
    ls,
):
    for item in ls:
        print(item)


def get_all_possible_combinations_symbols(num_numbers):
    num_symbols = num_numbers - 1
    symbol_options = ["+", "*"]

    # Generate all combinations of symbols
    ls_possbile_symbols_combinations = list(product(symbol_options, repeat=num_symbols))

    return ls_possbile_symbols_combinations


def get_all_possible_equations(ls_numbers, ls_possbile_symbols_combinations):
    ls_possible_equations = []
    for possible_symbol_combination in ls_possbile_symbols_combinations:
        print(
            f"Combining ls_numbers: {ls_numbers} with ls_symbols: {possible_symbol_combination}"
        )
        this_equation_string = []
        for i in range(0, len(ls_numbers)):
            this_equation_string.append(ls_numbers[i])
            if i <= len(possible_symbol_combination) - 1:
                this_equation_string.append(possible_symbol_combination[i])
        print(f"Adding possible equation: {this_equation_string} to list")
        ls_possible_equations.append(this_equation_string)

    return ls_possible_equations


def evaluate_equation_in_order(ls_equation_items):
    ls_equation_items = ls_equation_items.copy()
    running_num = ls_equation_items[0]

    for i in range(1, len(ls_equation_items) - 1, 2):
        symbol = ls_equation_items[i]
        number = ls_equation_items[i + 1]
        if symbol == "+":
            running_num = running_num + number
        if symbol == "*":
            running_num = running_num * number

    return running_num


def process_trasaction(transaction_string):
    print(f"Processing transaction: {transaction_string}")

    expected_answer, equation = transaction_string.split(": ")
    expected_answer = int(expected_answer)
    print(f"expected_answer: {expected_answer}")
    print(f"equation: {equation}")
    ls_equation_numbers = equation.strip().split(" ")
    ls_equation_numbers = [int(x) for x in ls_equation_numbers]
    print(f"ls_equation_numbers: {ls_equation_numbers}")
    ls_possbile_symbols_combinations = get_all_possible_combinations_symbols(
        len(ls_equation_numbers)
    )
    print(f"all_combinations: {ls_possbile_symbols_combinations}")
    ls_possible_equations = get_all_possible_equations(
        ls_equation_numbers, ls_possbile_symbols_combinations
    )
    print("ls_possible_equations:")
    pprint_ls(ls_possible_equations)

    for ls_equation_items in ls_possible_equations:
        evaluation = evaluate_equation_in_order(ls_equation_items)
        print(f"evaluation: {evaluation}")
        did_match = evaluation == expected_answer
        print(f"Does evaluation = {expected_answer} === {did_match}")
        if did_match:
            return expected_answer

    return 0


# %%
# Main #

TEST_MODE = False
if TEST_MODE:
    input_equations = get_text_input_lists("day_07_input_test.txt")
else:
    input_equations = get_text_input_lists("day_07_input.txt")

print("-" * 100)
print("input_map")
pprint_ls(input_equations)

print("-" * 100)
running_total_expected_answers_when_true = 0
for transaction_string in input_equations:
    print("-" * 50)
    value_to_add = process_trasaction(transaction_string)
    print(f"value_to_add: {value_to_add}")
    running_total_expected_answers_when_true = (
        running_total_expected_answers_when_true + value_to_add
    )

print(
    f"running_total_expected_answers_when_true: {running_total_expected_answers_when_true}"
)


# %%
# Main Part One #


# %%
# Main Part Two #


# %%
