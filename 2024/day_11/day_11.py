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


def apply_rules_to_list(ls_text_input):
    ls_text_input_copy = ls_text_input.copy()
    ls_text_input_return = []
    num_items = len(ls_text_input_copy)
    i = 0
    while i < (num_items):
        item = ls_text_input_copy[i]
        if item == 0:
            ls_text_input_return.append(1)
        elif len(str(item)) % 2 == 0:
            len_of_item = len(str(item))
            half_item = int(len_of_item / 2)
            ls_text_input_return.append(int(str(item)[:half_item]))
            ls_text_input_return.append(int(str(item)[half_item:]))
            # skip the newly added item
            # i = i + 1
        else:
            ls_text_input_return.append(ls_text_input_copy[i] * 2024)
        i = i + 1

    return ls_text_input_return


def apply_iterations_of_rules(ls_text_input, num_iterations):
    ls_text_input_return = ls_text_input.copy()
    for i in tqdm(range(num_iterations), desc="Iterations"):
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


ls_text_input_return = apply_iterations_of_rules(ls_text_input, 75)
print("Results")
# print(ls_text_input_return)
print(f"Length of list is now: {len(ls_text_input_return)}")


# %%
print("-" * 100)


# %%
