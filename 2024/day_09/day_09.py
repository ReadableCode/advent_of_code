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
            space_after = "0"

        dict_this_item = {"num_blocks": num_blocks, "space_after": space_after}
        ls_dict_files[file_id] = dict_this_item

        file_id += 1
        disk_input = disk_input[2:]

    return ls_dict_files


def save_to_disk(ls_dict_files):
    ls_disk_data = []
    for id, file_data in ls_dict_files.items():
        num_blocks = int(file_data["num_blocks"])
        space_after = int(file_data["space_after"])

        ls_disk_data.extend((num_blocks * [str(id)]))

        ls_disk_data.extend((space_after * ["."]))

    return ls_disk_data


def compact_disc(ls_disk_data):
    for idx in tqdm(range(len(ls_disk_data) - 1, 0, -1), desc="Compacting Disc"):
        if ls_disk_data[idx] == ".":
            continue
        if ls_disk_data.index(".") < idx:
            # Move the bit to the nearest empty space
            ls_disk_data[ls_disk_data.index(".")] = ls_disk_data[idx]
            ls_disk_data[idx] = "."

    return ls_disk_data


def find_first_contiguous_space_of_size(ls_disk_data, num_blocks_needed, curr_index):
    spaces_empty = 0
    currently_counting_empty = False
    starting_loc = 0
    for i, item in enumerate(ls_disk_data):
        if i >= curr_index:
            return False, False
        if item == ".":
            if num_blocks_needed == 1:
                return i, i
            if currently_counting_empty:
                spaces_empty += 1
                if spaces_empty >= int(num_blocks_needed):
                    ending_loc = i
                    return starting_loc, ending_loc
            else:
                starting_loc = i
                spaces_empty = 1
                currently_counting_empty = True
        else:
            currently_counting_empty = False
            spaces_empty = 0

    return False, False


def compact_disc_with_defrag(ls_disk_data, ls_dict_files):
    ls_disk_data = ls_disk_data.copy()
    max_file_id = list(ls_dict_files.keys())[-1]

    for file_id in tqdm(range(max_file_id, 0, -1), desc="Compacting Disc"):
        size_of_file = ls_dict_files.get(file_id).get("num_blocks")
        indexes_of_file = list(
            range(
                ls_disk_data.index(str(file_id)),
                ls_disk_data.index(str(file_id)) + int(size_of_file),
            )
        )
        # find first place whole file fits
        starting_loc, ending_loc = find_first_contiguous_space_of_size(
            ls_disk_data, int(size_of_file), indexes_of_file[0]
        )
        if starting_loc and ending_loc:
            for change_loc in range(starting_loc, ending_loc + 1):
                ls_disk_data[change_loc] = str(file_id)
            for erase_loc in indexes_of_file:
                ls_disk_data[erase_loc] = "."
    return ls_disk_data


def calculate_checksum(str_disk_data):
    checksum = 0
    for pos, file_id in enumerate(str_disk_data):
        # Only skip dots; include all numeric IDs, including "0"
        if file_id != ".":
            checksum += pos * int(file_id)
    return checksum


# %%
# Main #

KEEP_DEFRAGGED = True
TEST_MODE = False
if TEST_MODE:
    input_file = "day_09_input_test.txt"
    ls_dict_file = "day_09_output_test_files.json"
    uncompacted_file = "day_09_output_test_uncompacted.txt"
    compacted_file = "day_09_output_test_compacted.txt"
    compacted_file_defragged = "day_09_output_test_compacted_defragged.txt"
else:
    input_file = "day_09_input.txt"
    ls_dict_file = "day_09_output_files.json"
    uncompacted_file = "day_09_output_uncompacted.txt"
    compacted_file = "day_09_output_compacted.txt"
    compacted_file_defragged = "day_09_output_compacted_defragged.txt"

ls_disk_data = get_text_input_lists(input_file)

print("-" * 100)
print("".join(ls_disk_data))

ls_dict_files = get_files_on_disk(ls_disk_data)

with open(ls_dict_file, "w") as file:
    json.dump(ls_dict_files, file)

ls_disk_data = save_to_disk(ls_dict_files)

# Write uncompacted data to a file
with open(uncompacted_file, "w") as file:
    file.write(str(ls_disk_data))

print(f"ls_disk_data:\n{ls_disk_data}")

if KEEP_DEFRAGGED:
    ls_disk_data_compacted = compact_disc_with_defrag(ls_disk_data, ls_dict_files)
    # Write compacted data to a file
    with open(compacted_file_defragged, "w") as file:
        file.write(str(ls_disk_data_compacted))
else:
    ls_disk_data_compacted = compact_disc(ls_disk_data)
    # Write compacted data to a file
    with open(compacted_file, "w") as file:
        file.write(str(ls_disk_data_compacted))

print("-" * 100)

print(f"str_disk_data_compacted:\n{ls_disk_data_compacted}")

checksum = calculate_checksum(ls_disk_data_compacted)

print(f"checksum:\n{checksum}")

print("-" * 100)


# %%
