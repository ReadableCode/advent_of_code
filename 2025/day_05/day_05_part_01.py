# %%
# Imports #

import sys

from tqdm import tqdm  # type: ignore

# %%
# Vars #


def get_text_input_lines(file_path, debug=False):
    with open(file_path, "r") as file:
        text_lines = file.readlines()

    text_lines = [line.strip() for line in text_lines]

    if debug:
        print("-------- text file contents --------")
        for text_line in text_lines:
            print(text_line)
        print("------------------------------------")

    return text_lines


def get_fresh_ranges(file_path):
    text_lines = get_text_input_lines(file_path)

    fresh_ranges = []
    for text_line in text_lines:
        if text_line == "":
            break

        start_of_range, end_of_range = text_line.split("-")
        fresh_ranges.append((int(start_of_range), int(end_of_range)))

    return fresh_ranges


def get_available_ids_from_file(file_path):
    text_lines = get_text_input_lines(file_path)

    found_break = False
    available_ids = []
    for text_line in text_lines:
        if text_line == "":
            found_break = True
            continue

        if found_break:
            available_ids.append(int(text_line))

    return available_ids


def check_if_id_fresh(ls_fresh_ranges, available_id):
    for fresh_range in ls_fresh_ranges:
        if (available_id >= fresh_range[0]) and (available_id <= fresh_range[1]):
            return True

    return False


ls_fresh_ranges = [(3, 5), (10, 14), (16, 20), (12, 18)]
available_id = 3
is_fresh = check_if_id_fresh(ls_fresh_ranges, available_id)
assert is_fresh

available_id = 1
is_fresh = check_if_id_fresh(ls_fresh_ranges, available_id)
assert not is_fresh

available_id = 32
is_fresh = check_if_id_fresh(ls_fresh_ranges, available_id)
assert not is_fresh

# %%


def get_list_fresh_ids_from_available_ids(ls_fresh_ranges, available_ids):
    ls_fresh_ids_available = []
    for available_id in available_ids:
        if check_if_id_fresh(ls_fresh_ranges, available_id):
            ls_fresh_ids_available.append(available_id)

    return ls_fresh_ids_available


def get_max_fresh_id(ls_fresh_ranges):
    max_fresh_id = 0
    for fresh_range in ls_fresh_ranges:
        max_fresh_id = max(max_fresh_id, fresh_range[1])

    return max_fresh_id


def count_all_possible_fresh_ids(ls_fresh_ranges):
    num_fresh_ids = 0
    use_tqdm = "ipykernel" not in sys.argv[0]
    max_fresh_id = get_max_fresh_id(ls_fresh_ranges)

    iterator = range(0, max_fresh_id + 1)
    if use_tqdm:
        iterator = tqdm(
            iterator,
            total=max_fresh_id + 1,
            desc="Counting fresh IDs",
            unit="id",
        )

    for available_id in iterator:
        if check_if_id_fresh(ls_fresh_ranges, available_id):
            num_fresh_ids += 1

    return num_fresh_ids


# %%


file_path = "day_05_part_01_input_test.txt"

ls_fresh_ranges = get_fresh_ranges(file_path)
print("ls_fresh_ranges")
print(ls_fresh_ranges)

available_ids = get_available_ids_from_file(file_path)
print("available_ids")
print(available_ids)

ls_fresh_ids_available = get_list_fresh_ids_from_available_ids(
    ls_fresh_ranges, available_ids
)
print("fresh_avaiable_ids")
print(ls_fresh_ids_available)

num_fresh_ids = len(ls_fresh_ids_available)
print(f"{num_fresh_ids} ids are fresh")
assert num_fresh_ids == 3

# %%

file_path = "day_05_part_01_input.txt"

ls_fresh_ranges = get_fresh_ranges(file_path)
print("ls_fresh_ranges")
print(ls_fresh_ranges)

available_ids = get_available_ids_from_file(file_path)
print("available_ids")
print(available_ids)

ls_fresh_ids_available = get_list_fresh_ids_from_available_ids(
    ls_fresh_ranges, available_ids
)
print("fresh_avaiable_ids")
print(ls_fresh_ids_available)

num_fresh_ids = len(ls_fresh_ids_available)
print(f"{num_fresh_ids} ids are fresh")
assert num_fresh_ids == 525


# %%

file_path = "day_05_part_01_input_test.txt"

ls_fresh_ranges = get_fresh_ranges(file_path)
print("ls_fresh_ranges")
print(ls_fresh_ranges)

num_fresh_ids = count_all_possible_fresh_ids(ls_fresh_ranges)
print(f"Num fresh ids: {num_fresh_ids}")
assert num_fresh_ids == 14

# %%

file_path = "day_05_part_01_input.txt"

ls_fresh_ranges = get_fresh_ranges(file_path)
print("ls_fresh_ranges")
print(ls_fresh_ranges)

num_fresh_ids = count_all_possible_fresh_ids(ls_fresh_ranges)
print(f"Num fresh ids: {num_fresh_ids}")
# assert num_fresh_ids == 14

# %%
