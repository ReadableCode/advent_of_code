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


def get_max_joltage(text_line, debug=False):
    ls_batteries = list(text_line)
    if debug:
        print(ls_batteries)

    # dont included last value because we deff want two digits
    max_value = max(ls_batteries[:-1])

    # get the first instance of this number so
    # we have the best chances for a high second num
    max_value_index = ls_batteries.index(max_value)

    max_second_value = max(ls_batteries[max_value_index + 1 :])
    max_second_value_index = (
        ls_batteries[max_value_index + 1 :].index(max_second_value)
        + max_value_index
        + 1
    )

    if debug:
        print(f"Max battery is: {max_value} @ {max_value_index}")
        print(f"Max second battery is: {max_second_value} @ {max_second_value_index}")

    return int(f"{max_value}{max_second_value}")


# check to make sure we get the second 8 since its the one after the 9
text_line = "8987654321111111"
max_joltage = get_max_joltage(text_line, debug=True)
print(f"Max holtage of {text_line} is {max_joltage}")
assert max_joltage == 98

# test built in tests
text_line = "987654321111111"
max_joltage = get_max_joltage(text_line, debug=True)
print(f"Max holtage of {text_line} is {max_joltage}")
assert max_joltage == 98

text_line = "811111111111119"
max_joltage = get_max_joltage(text_line, debug=True)
print(f"Max holtage of {text_line} is {max_joltage}")
assert max_joltage == 89

text_line = "234234234234278"
max_joltage = get_max_joltage(text_line, debug=True)
print(f"Max holtage of {text_line} is {max_joltage}")
assert max_joltage == 78

text_line = "818181911112111"
max_joltage = get_max_joltage(text_line, debug=True)
print(f"Max holtage of {text_line} is {max_joltage}")
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
