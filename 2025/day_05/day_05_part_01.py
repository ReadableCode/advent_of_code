# %%
# Imports #


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
        fresh_ranges.append((start_of_range, end_of_range))

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
        if (available_id >= int(fresh_range[0])) and (
            available_id <= int(fresh_range[1])
        ):
            return True

    return False


ls_fresh_ranges = [("3", "5"), ("10", "14"), ("16", "20"), ("12", "18")]
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


# def get_fresh_ids(file_path, debug=False):
#     fresh_ranges = get_fresh_ranges(file_path)

#     fresh_ids = []
#     for fresh_range in fresh_ranges:
#         start_of_range, end_of_range = fresh_range.split("-")

#         start_of_range = int(start_of_range)
#         end_of_range = int(end_of_range) + 1

#         if debug:
#             print(f"start_of_range: {start_of_range}, end_of_range: {end_of_range}")

#         fresh_ids_this_range = range(start_of_range, end_of_range)
#         fresh_ids.extend(fresh_ids_this_range)

#     fresh_ids = list(set(fresh_ids))
#     fresh_ids.sort()

#     return fresh_ids


# def get_list_fresh_ids_from_available_ids(fresh_ids, available_ids):
#     return [
#         available_id for available_id in available_ids if int(available_id) in fresh_ids
#     ]


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
