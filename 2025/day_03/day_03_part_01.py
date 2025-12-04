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


text_lines = get_text_input_lists("day_03_part_01_input_test.txt")
print(text_lines)


# %%


def get_max_joltage(text_line, debug=False):
    ls_batteries = list(text_line)
    if debug:
        print(ls_batteries)

    max_value = max(ls_batteries)
    max_value_index = ls_batteries.index(max_value)
    if debug:
        print(f"Max battery is: {max_value} @ {max_value_index}")


text_line = "987654321111111"
max_joltage = get_max_joltage(text_line, debug=True)
print(f"Max holtage of {text_line} is {max_joltage}")

# %%
