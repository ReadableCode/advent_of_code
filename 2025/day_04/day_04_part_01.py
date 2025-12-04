# %%
# Imports #


# %%
# Vars #


def get_text_input_lists(file_path):
    with open(file_path, "r") as file:
        text_lines = file.readlines()

    text_lines = [line.strip() for line in text_lines]

    return text_lines


def get_grid(file_path):
    text_lines = get_text_input_lists(file_path)

    text_arrays = []
    for line in text_lines:
        text_arrays.append(list(line))

    for row in text_arrays:
        print(row)

    return text_arrays


# %%


def get_list_ad_locations(location_tup):
    row_num, col_num = location_tup
    ls_rows = [row_num - 1, row_num, row_num + 1]
    ls_cols = [col_num - 1, col_num, col_num + 1]

    list_ad_locations = []

    for row_num in ls_rows:
        for col_num in ls_cols:
            list_ad_locations.append((row_num, col_num))

    return list_ad_locations


location_tup = (1, 3)
list_ad_locations = get_list_ad_locations(location_tup)
print(list_ad_locations)


# %%


def get_grid_values(text_arrays, list_ad_locations, debug=False):
    ls_grid_values = []

    for ad_loc in list_ad_locations:
        row_num, col_num = ad_loc
        if row_num >= len(text_arrays) or row_num < 0:
            continue
        if col_num >= len(text_arrays[0]) or col_num < 0:
            continue

        if debug:
            print(f"ad_loc: {ad_loc} is in range")

        value = text_arrays[row_num][col_num]
        ls_grid_values.append(value)

    return ls_grid_values


text_arrays = get_grid("day_04_part_01_input_test.txt")
location_tup = (0, 9)
list_ad_locations = get_list_ad_locations(location_tup)
ls_grid_values = get_grid_values(text_arrays, list_ad_locations, debug=True)
print(ls_grid_values)


# %%


def count_ad_rolls(text_arrays, location_tup, debug=False):
    if debug:
        print("-" * 200)
    row_num, col_num = location_tup

    if debug:
        print(f"row_num: {row_num}")
        print(f"col_num: {col_num}")

    list_ad_locations = get_list_ad_locations(location_tup)
    if debug:
        print(list_ad_locations)

    # remove current location
    list_ad_locations.remove(location_tup)

    if debug:
        print(list_ad_locations)

    ls_grid_values = get_grid_values(text_arrays, list_ad_locations)

    if debug:
        print(ls_grid_values)

    num_rolls = 0
    for grid_value in ls_grid_values:
        if grid_value == "@":
            num_rolls += 1

    return num_rolls


text_arrays = get_grid("day_04_part_01_input_test.txt")
location_tup = (0, 0)
num_ad_rolls = count_ad_rolls(text_arrays, location_tup, debug=True)
print(num_ad_rolls)
assert num_ad_rolls == 2

text_arrays = get_grid("day_04_part_01_input_test.txt")
location_tup = (1, 3)
num_ad_rolls = count_ad_rolls(text_arrays, location_tup, debug=True)
print(num_ad_rolls)
assert num_ad_rolls == 7


# %%


def count_moveable_rolls(text_arrays, debug=False):
    if debug:
        print("-" * 200)

    list_all_locations = []

    for row_num in range(len(text_arrays)):
        for col_num in range(len(text_arrays[0])):
            list_all_locations.append((row_num, col_num))

    if debug:
        print("list_all_locations")
        print(list_all_locations)

    num_moveable_rolls = 0
    for location_tup in list_all_locations:
        if debug:
            print(f"----- Processing location:{location_tup} -----")
        grid_value = get_grid_values(text_arrays, [location_tup])[0]
        if debug:
            print(f"Grid value is: {grid_value}")
        if grid_value != "@":
            continue
        num_ad_rolls = count_ad_rolls(text_arrays, location_tup)
        if num_ad_rolls < 4:
            if debug:
                print(f"location:{location_tup} is moveable")
            num_moveable_rolls += 1
        else:
            if debug:
                print(f"location:{location_tup} is not moveable")

    return num_moveable_rolls


text_arrays = get_grid("day_04_part_01_input_test.txt")
num_moveable_rolls = count_moveable_rolls(text_arrays, debug=True)
print(num_moveable_rolls)
assert num_moveable_rolls == 13

text_arrays = get_grid("day_04_part_01_input.txt")
num_moveable_rolls = count_moveable_rolls(text_arrays, debug=False)
print(num_moveable_rolls)
assert num_moveable_rolls == 1435

# %%
