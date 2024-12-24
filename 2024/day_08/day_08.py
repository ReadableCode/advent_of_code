# %%
# Imports #

import copy
from math import sqrt

from tqdm import tqdm

# %%
# Vars #


def get_text_input_lists(file_path):
    with open(file_path, "r") as file:
        text_lines = file.readlines()

    text_lines = [list(line.strip()) for line in text_lines]

    return text_lines


# %%
# Funcs #


def pprint_ls(
    ls,
):
    for item in ls:
        print(item)


def get_distance_between_coords(tup_coords_one, tup_coords_two):
    x_distance = tup_coords_one[0] - tup_coords_two[0]
    y_distance = tup_coords_one[1] - tup_coords_two[1]

    distance = sqrt((abs(x_distance) ** 2) + (abs(y_distance) ** 2))

    return distance


def get_unique_freqs(ls_ls_map):
    all_symbols = []
    for row in ls_ls_map:
        for cell in row:
            all_symbols.append(cell)

    all_symbols = list(set(all_symbols))

    if "." in all_symbols:
        all_symbols.remove(".")
    if "#" in all_symbols:
        all_symbols.remove("#")

    return all_symbols


def get_coords_of_all_symbol(ls_ls_map, symbol):
    all_coords = []
    for row_index, row in enumerate(ls_ls_map):
        for col_index, cell in enumerate(row):
            if symbol in cell:
                all_coords.append((row_index, col_index))  # Append coordinates

    return all_coords


def check_coord_is_antinode(coords_to_check, ls_coords_of_symbol):
    for coord_one in ls_coords_of_symbol:
        for coord_two in ls_coords_of_symbol:
            if coord_one == coord_two:
                continue

            distance_from_coord_one = get_distance_between_coords(
                coord_one, coords_to_check
            )
            distance_from_coord_two = get_distance_between_coords(
                coord_two, coords_to_check
            )

            if (distance_from_coord_one * 2 == distance_from_coord_two) or (
                distance_from_coord_two * 2 == distance_from_coord_one
            ):
                # Collinearity Check using determinant method
                x1, y1 = coord_one
                x2, y2 = coord_two
                x3, y3 = coords_to_check

                det = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
                is_collinear = abs(det) < 1e-9  # Handle floating-point errors

                if is_collinear and (
                    (distance_from_coord_one * 2 == distance_from_coord_two)
                    or (distance_from_coord_two * 2 == distance_from_coord_one)
                ):
                    # Point is an antinode and collinear
                    return True

    return False


def count_anitnodes(ls_ls_map):
    count_antinodes = 0
    for row_index, row in enumerate(ls_ls_map):
        for col_index, cell in enumerate(row):
            if "<" in cell:
                count_antinodes += 1

    return count_antinodes


def get_map_with_placed_antinode(ls_ls_map, coords_to_place_at, symbol_to_place):
    return_map = copy.deepcopy(ls_ls_map)
    return_map[coords_to_place_at[0]][coords_to_place_at[1]] = (
        str(return_map[coords_to_place_at[0]][coords_to_place_at[1]]) + symbol_to_place
    )
    return_map[coords_to_place_at[0]][coords_to_place_at[1]] = return_map[
        coords_to_place_at[0]
    ][coords_to_place_at[1]].replace(".", "")

    return return_map


def place_all_antinodes(ls_ls_map):
    return_map = copy.deepcopy(ls_ls_map)
    ls_symbols = get_unique_freqs(ls_ls_map)

    # Outer loop for symbols with tqdm
    for symbol in tqdm(ls_symbols, desc="Processing Symbols"):
        # Loop for rows with tqdm
        for row_index, row in enumerate(
            tqdm(ls_ls_map, desc=f"Rows for {symbol}", leave=False)
        ):
            for col_index, cell in enumerate(row):
                all_coords_this_symbol = get_coords_of_all_symbol(ls_ls_map, symbol)
                is_antinode_this_symbol = check_coord_is_antinode(
                    (row_index, col_index), all_coords_this_symbol
                )
                if is_antinode_this_symbol:
                    return_map = get_map_with_placed_antinode(
                        return_map, (row_index, col_index), f"<{symbol}>"
                    )

    return return_map


# %%
# Main #

TEST_MODE = False
if TEST_MODE:
    ls_ls_map = get_text_input_lists("day_08_input_test.txt")
else:
    ls_ls_map = get_text_input_lists("day_08_input.txt")

print("-" * 100)
print("input_map")
pprint_ls(ls_ls_map)

return_map = place_all_antinodes(ls_ls_map)
print("Filled Map")
pprint_ls(return_map)

num_anitnodes = count_anitnodes(return_map)
print(f"Num antinodes:{num_anitnodes}")

print("-" * 100)


# %%
# Main Part One #


# %%
# Main Part Two #


# %%
