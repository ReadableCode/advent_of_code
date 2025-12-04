# %%
# Imports #


# %%
# Vars #


# %%
# Vars #


def get_text_input_lists(file_path):
    with open(file_path, "r") as file:
        text_lines = file.readlines()

    text_lines = [line.strip() for line in text_lines]

    return text_lines


# %%


def get_max_joltage(text_line, num_digits=2, debug=False):
    ls_batteries = list(text_line)
    ls_return_digits = []

    num_digits_left = len(ls_batteries)
    ls_batteries_left = ls_batteries

    if debug:
        print("-" * 500)
        print("-" * 500)
        print(f"initial ls_batteries: {ls_batteries}")
        print(f"initial num_digits_left: {num_digits_left}")
        print("-" * 500)
        print("-" * 500)

    while len(ls_return_digits) < num_digits:
        num_digits_still_needed = num_digits - len(ls_return_digits)
        if debug:
            print(
                f"---------- len(ls_return_digits): {len(ls_return_digits)} ----------"
            )
            print(f"num_digits_left: {num_digits_left}")
        if num_digits_still_needed > 1:
            list_to_consider = ls_batteries_left[: -(num_digits_still_needed - 1)]
        else:
            list_to_consider = ls_batteries_left
        if debug:
            print(f"list_to_consider: {list_to_consider}")

        max_value = max(list_to_consider)
        # get the first instance of this number so
        # we have the best chances for a high second num
        max_value_index = ls_batteries_left.index(max_value)

        if debug:
            print(f"max_value: {max_value} found at {max_value_index}")

        ls_return_digits.append(max_value)

        # set len of list left to num digits left
        start_index = max_value_index + 1
        ls_batteries_left = ls_batteries_left[start_index:]
        num_digits_left = len(ls_batteries_left)
        if debug:
            print(f"New list starts at index: {start_index}")
            print(f"ls_batteries_left: {ls_batteries_left}")
            print(f"New length: {num_digits_left}")

        if debug:
            print(f"Remaining list is: {ls_batteries_left}")
            print(f"remining digits is: {num_digits_left}")

    return int("".join(ls_return_digits))


# check to make sure we get the second 8 since its the one after the 9
text_line = "8987654321111111"
max_joltage = get_max_joltage(text_line, debug=True)
print(f"Max joltage of {text_line} is {max_joltage}")
assert max_joltage == 98

# test built in tests
text_line = "987654321111111"
max_joltage = get_max_joltage(text_line, debug=True)
print(f"Max joltage of {text_line} is {max_joltage}")
assert max_joltage == 98

text_line = "811111111111119"
max_joltage = get_max_joltage(text_line, debug=True)
print(f"Max joltage of {text_line} is {max_joltage}")
assert max_joltage == 89

text_line = "234234234234278"
max_joltage = get_max_joltage(text_line, debug=True)
print(f"Max joltage of {text_line} is {max_joltage}")
assert max_joltage == 78

text_line = "818181911112111"
max_joltage = get_max_joltage(text_line, debug=True)
print(f"Max joltage of {text_line} is {max_joltage}")
assert max_joltage == 92


# %%


def get_total_joltage_from_list_lines(text_lines):
    sum_lines = 0

    for text_line in text_lines:
        max_joltage = get_max_joltage(text_line)
        sum_lines += max_joltage

    return sum_lines


text_lines = get_text_input_lists("day_03_part_01_input_test.txt")
print(text_lines)
sum_lines = get_total_joltage_from_list_lines(text_lines)
print(sum_lines)
assert sum_lines == 357


# %%
# Part 01 #


text_lines = get_text_input_lists("day_03_part_01_input.txt")
print(text_lines)
sum_lines = get_total_joltage_from_list_lines(text_lines)
print(sum_lines)
assert sum_lines == 17694


# %%
