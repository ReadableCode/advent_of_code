# %%
# Imports #

import json

from tqdm import tqdm

# %%
# Vars #


def pprint_dict(data, indent=0):
    try:
        print(json.dumps(data, indent=indent + 2))
        return
    except Exception as e:
        if e:
            pass

    if isinstance(data, dict):
        for key, value in data.items():
            print(" " * indent + str(key) + ": ", end="")
            if isinstance(value, dict):
                print("DICTIONARY {")
                pprint_dict(value, indent + 8)
                print(" " * indent + "}")
            elif isinstance(value, list):
                print("LIST [")
                for item in value:
                    if isinstance(item, dict):
                        pprint_dict(item, indent + 8)
                        print("," + " " * (indent + 8))
                    else:
                        print(" " * (indent + 8) + str(item) + ",")
                print(" " * indent + "]")
            else:
                print(str(value))
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, dict):
                pprint_dict(item, indent)
                print("," + " " * indent)
            else:
                print(" " * indent + str(item) + ",")
    else:
        print(" " * indent + str(data))


def pprint_ls(
    ls,
):
    for item in ls:
        print(item)


def get_text_input_list(file_path):
    with open(file_path, "r") as file:
        text_lines = file.readlines()

    text_input = text_lines[0].split(" ")
    text_input = [int(x) for x in text_input]

    return text_input


"""
As you observe them for a while, you find that the stones have a consistent behavior. Every time you blink, the stones each simultaneously change according to the first applicable rule in this list:

If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
"""


def apply_rules_to_list(ls_text_input):
    ls_text_input_copy = ls_text_input.copy()
    ls_text_input_return = []
    num_items = len(ls_text_input_copy)
    i = 0
    while i < (num_items):
        item = ls_text_input_copy[i]
        print("-" * 20)
        print(f"Starting list:\n{ls_text_input_return}")
        print(f"Applying rule to item {i} which is: {item}")
        if item == 0:
            print("Apply rule 1 bc numer is 0")
            ls_text_input_return.append(1)
        elif len(str(item)) % 2 == 0:
            print("Applying rule 2 bc even numbers")
            len_of_item = len(str(item))
            half_item = int(len_of_item / 2)
            print(f"item: {item} has half num digits: {half_item}")
            ls_text_input_return.append(int(str(item)[:half_item]))
            ls_text_input_return.append(int(str(item)[half_item:]))
            # skip the newly added item
            # i = i + 1
        else:
            print("Applying rule 3 bc nothing else applied")
            ls_text_input_return.append(ls_text_input_copy[i] * 2024)
        i = i + 1
        print(ls_text_input_return)

    return ls_text_input_return


def apply_iterations_of_rules(ls_text_input, num_iterations):
    ls_text_input_return = ls_text_input.copy()
    for i in range(num_iterations):
        print(f"Running Iteration number: {i}")
        ls_text_input_return = apply_rules_to_list(ls_text_input_return)

    return ls_text_input_return


# %%
# Main #


TEST_MODE = False
if TEST_MODE:
    input_file = "day_11_input_test.txt"
else:
    input_file = "day_11_input.txt"

ls_text_input = get_text_input_list(input_file)

print("-" * 100)
print(ls_text_input)


print("-" * 100)


# %%


ls_text_input_return = apply_iterations_of_rules(ls_text_input, 25)
print("Results")
print(ls_text_input_return)
print(f"Length of list is now: {len(ls_text_input_return)}")


# %%
print("-" * 100)


# %%
