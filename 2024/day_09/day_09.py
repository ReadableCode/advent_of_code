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


def get_text_input_lists(file_path):
    with open(file_path, "r") as file:
        text_lines = file.readlines()

    text_lines = list(text_lines[0].strip())

    return text_lines


def get_files_on_disk(disk_input):
    disk_input = disk_input.copy()
    ls_dict_files = {}
    file_id = 0
    while len(disk_input) > 0:
        num_blocks = disk_input[0]
        if len(disk_input) > 1:
            space_after = disk_input[1]
        else:
            space_after = 0

        dict_this_item = {"num_blocks": num_blocks, "space_after": space_after}
        ls_dict_files[file_id] = dict_this_item

        file_id += 1
        disk_input = disk_input[2:]

    return ls_dict_files


def save_to_disk(ls_dict_files):
    str_disk_data = ""
    for id, file_data in ls_dict_files.items():
        num_blocks = int(file_data["num_blocks"])
        space_after = int(file_data["space_after"])

        str_disk_data = str_disk_data + (str(id) * num_blocks)
        str_disk_data = str_disk_data + (space_after * ".")

    return str_disk_data


def compact_disc(disk_input):
    ls_disk_input = list(disk_input)

    for idx in tqdm(range(len(ls_disk_input) - 1, 0, -1), desc="Compacting Disc"):
        if ls_disk_input[idx] == ".":
            continue
        if ls_disk_input.index(".") < idx:
            # Move the bit to the nearest empty space
            ls_disk_input[ls_disk_input.index(".")] = ls_disk_input[idx]
            ls_disk_input[idx] = "."

    return "".join(ls_disk_input)


def calculate_checksum(str_disk_data):
    checksum = 0
    for pos in range(len(str_disk_data) - 1):
        file_id = str_disk_data[pos]
        if file_id == ".":
            continue
        checksum = checksum + (pos * int(file_id))

    return checksum


# %%
# Main #

TEST_MODE = False
if TEST_MODE:
    ls_disk_input = get_text_input_lists("day_09_input_test.txt")
else:
    ls_disk_input = get_text_input_lists("day_09_input.txt")

print("-" * 100)
print("".join(ls_disk_input))

ls_dict_files = get_files_on_disk(ls_disk_input)

str_disk_data_uncompacted = save_to_disk(ls_dict_files)

print(f"str_disk_data_uncompacted:\n{str_disk_data_uncompacted}")

str_disk_data_compacted = compact_disc(str_disk_data_uncompacted)

print(f"str_disk_data_compacted:\n{str_disk_data_compacted}")

checksum = calculate_checksum(str_disk_data_compacted)

print(f"checksum:\n{checksum}")

print("-" * 100)


# %%
