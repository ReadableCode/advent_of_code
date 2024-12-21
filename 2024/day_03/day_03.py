# %%
# Imports

import re

# %%
# Functions


def get_text_input_lists(file_path):
    with open(file_path, "r") as file:
        text_lines = file.readlines()

    return text_lines


def combine_ls_strings(ls_strings):
    all_text = ""
    for str_item in ls_strings:
        all_text = all_text + str_item

    return all_text


def split_string_to_do_dont(string):
    # add a do at the beginning to default to starting with do
    string = "do()" + string
    # Use a positive lookahead to split by "do()" or "don't()" but keep the delimiters
    split_parts = re.split(r"(?=do\(\)|don't\(\))", string)
    return split_parts


ls_do_donts = split_string_to_do_dont(
    "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
)
for do_dont in ls_do_donts:
    print(do_dont)


def split_string_to_functions(line):
    ls_line_funcs = re.findall(r"mul\(\d{1,3},\d{1,3}\)", line)
    return ls_line_funcs


def perform_str_function(string_func):
    string_func = string_func.replace("mul(", "")
    string_func = string_func.replace(")", "")
    item_1, item_2 = string_func.split(",")
    item_1, item_2 = int(item_1), int(item_2)

    print(f"item_1: {item_1}")
    print(f"item_2: {item_2}")

    return item_1 * item_2


# %%
# Main #


list_lines = get_text_input_lists("day_03_input.txt")
all_text = combine_ls_strings(list_lines)

ls_do_donts = split_string_to_do_dont(all_text)

ABIDE_BY_DO_DONTS = True


running_total = 0
for do_dont in ls_do_donts:
    if ABIDE_BY_DO_DONTS and do_dont.startswith("don't"):
        continue

    ls_line_funcs = split_string_to_functions(do_dont)

    for line_func in ls_line_funcs:
        print("-" * 50)
        print(line_func)

        line_func_result = perform_str_function(line_func)
        print(f"Line result: {line_func_result}")
        running_total += line_func_result

print(f"Total: {running_total}")

# %%
