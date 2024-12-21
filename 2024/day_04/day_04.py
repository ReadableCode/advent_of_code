# %%
# Imports

import re

# %%
# Functions


def pprint_ls(ls, ls_title="List"):
    """
    Pretty prints a list with a title.

    Args:
        ls (list): The list to print.
        ls_title (str): The title of the list.

    Returns:
        None
    """

    # if list is empty return
    if len(ls) == 0:
        item_max_len = 0
    else:
        item_max_len = 0
        for item in ls:
            try:
                this_length = len(str(item))
            except Exception:
                this_length = 0
            if this_length > item_max_len:
                item_max_len = this_length

    # get the longest item in the list
    max_len = max(item_max_len, len(ls_title)) + 8

    # print the top of the box
    print(f"{'-' * (max_len + 4)}")

    # print the title with padding
    print(f"| {ls_title.center(max_len)} |")

    # print the bottom of the title box
    print(f"{'-' * (max_len + 4)}")

    # print each item in the list
    for item in ls:
        if isinstance(item, str):
            print(f"| {item.ljust(max_len)} |")
        else:
            print(f"| {str(item).ljust(max_len)} |")

    # print the bottom of the list box
    print(f"{'-' * (max_len + 4)}")


def get_text_input_list_of_lists(file_path):
    with open(file_path, "r") as file:
        text_lines = file.readlines()

    ls_all_lines = []
    for text_line in text_lines:
        print(text_line)
        ls_chars = list(text_line)
        ls_all_lines.append(ls_chars)

    return ls_all_lines


def get_left_to_right_string_at_coords(ls_ls_text, start_row, start_col, num_chars=4):
    end_col = start_col + num_chars

    # drop end_col if exceeds len
    end_col = min(end_col, len(ls_ls_text[start_row]))

    ls_return_string = ls_ls_text[start_row][start_col:end_col]

    print(f"ls_left_to_right_string: {ls_return_string}")

    return ls_return_string


def get_right_to_left_string_at_coords(ls_ls_text, start_row, start_col, num_chars=4):
    # Calculate the end column as the inclusive lower bound
    end_col = start_col - (num_chars)

    # If end_col is less than 0, use None to include the first element
    if end_col < 0:
        end_col = None

    # Slice from start_col to end_col in reverse
    ls_return_string = ls_ls_text[start_row][start_col:end_col:-1]

    print(f"ls_right_to_left_string: {ls_return_string}")

    return ls_return_string


ls_ls_text = [
    ["M", "M", "S", "A", "M", "X", "S", "M", "M", "M"],
    ["M", "M", "S", "X", "M", "A", "S", "M", "M", "M"],
    ["M", "M", "S", "A", "M", "X", "S", "M", "M", "M"],
    ["M", "M", "S", "A", "M", "X", "S", "M", "M", "M"],
    ["M", "M", "S", "A", "M", "X", "S", "M", "M", "M"],
]
start_row = 1
start_col = 8

ls_return_string = get_right_to_left_string_at_coords(
    ls_ls_text, start_row, start_col, num_chars=4
)

print(ls_return_string)
assert ls_return_string == ["M", "M", "S", "A"]

start_row = 1
start_col = 3

ls_return_string = get_right_to_left_string_at_coords(
    ls_ls_text, start_row, start_col, num_chars=4
)

print(ls_return_string)
assert ls_return_string == ["X", "S", "M", "M"]

start_row = 1
start_col = 2

ls_return_string = get_right_to_left_string_at_coords(
    ls_ls_text, start_row, start_col, num_chars=4
)

print(ls_return_string)
assert ls_return_string == ["S", "M", "M"]


# %%


def find_occurances_at_coords(
    ls_ls_text, start_row, start_col, search_text, num_chars=4
):
    search_text = list(search_text)

    occruances_found = 0

    ls_left_to_right_string = get_left_to_right_string_at_coords(
        ls_ls_text, start_row, start_col, num_chars=num_chars
    )
    if ls_left_to_right_string == search_text:
        occruances_found += 1

    ls_right_to_left_string = get_right_to_left_string_at_coords(
        ls_ls_text, start_row, start_col, num_chars=num_chars
    )
    if ls_right_to_left_string == search_text:
        occruances_found += 1

    # find top to bottom occurance
    ls_top_to_bottom_string = []
    for parse_row in range(start_row, start_row + num_chars):
        ls_top_to_bottom_string.append(ls_ls_text[parse_row][start_col])
    print(f"ls_top_to_bottom_string: {ls_top_to_bottom_string}")
    if ls_top_to_bottom_string == search_text:
        occruances_found += 1

    # find top to bottom occurance
    ls_bottom_to_top_string = []
    for parse_row in range(start_row, start_row + num_chars):
        ls_bottom_to_top_string.append(ls_ls_text[parse_row][start_col])
    ls_bottom_to_top_string = ls_bottom_to_top_string[::-1]
    print(f"ls_bottom_to_top_string: {ls_bottom_to_top_string}")
    if ls_bottom_to_top_string == search_text:
        occruances_found += 1

    return occruances_found


ls_ls_text = [
    ["M", "M", "S", "A", "M", "X", "S", "M", "M", "M"],
    ["M", "M", "S", "X", "M", "A", "S", "M", "M", "M"],
    ["M", "M", "S", "A", "M", "X", "S", "M", "M", "M"],
    ["M", "M", "S", "A", "M", "X", "S", "M", "M", "M"],
    ["M", "M", "S", "A", "M", "X", "S", "M", "M", "M"],
]
start_row = 1
start_col = 3
search_text = "XMAS"

occruances_found = find_occurances_at_coords(
    ls_ls_text, start_row, start_col, search_text
)

print(occruances_found)


# %%


def find_horizonatal_occurances(line_list, both_directions=True):
    print(f"Searching for occruances in line:\n{line_list}")
    ls_search_strings = [list("XMAS")]
    if both_directions:
        ls_search_strings.append(list("SAMX"))

    print(f"Searching for: {ls_search_strings}")
    count_occurances = 0
    for i in range(len(line_list)):
        if line_list[i : i + 4] in ls_search_strings:
            print(f"Found {line_list[i:i+4]} at position {i}")
            count_occurances += 1

    return count_occurances


ls_all_lines = get_text_input_list_of_lists("day_04_input.txt")
pprint_ls(ls_all_lines)
for line_list in ls_all_lines:
    count_occurances = find_horizonatal_occurances(line_list, both_directions=True)
    break


# %%
