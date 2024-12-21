# %%
# Imports

import re

# %%
# Functions


def get_text_input_lists(file_path):
    with open(file_path, "r") as file:
        text_lines = file.readlines()

    return text_lines


def split_line_to_functions(line):
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


print(perform_str_function("mul(970,37)"))

# %%
# Main #


list_lines = get_text_input_lists("day_03_input.txt")

running_total = 0
for line_item in list_lines:
    print("-" * 100)
    print(line_item)
    ls_line_funcs = split_line_to_functions(line_item)

    for line_func in ls_line_funcs:
        print("-" * 50)
        print(line_func)

        line_func_result = perform_str_function(line_func)
        print(f"Line result: {line_func_result}")
        running_total += line_func_result

print(f"Total: {running_total}")

# %%
