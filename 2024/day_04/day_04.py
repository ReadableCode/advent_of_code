# %%
# Imports

import re

# %%
# Functions


def pprint_ls(ls, ls_title="List"):
    """
    Pretty prints a list with a title.

    Args:
        ls (list): The list to print.
        ls_title (str): The title of the list.

    Returns:
        None
    """

    # if list is empty return
    if len(ls) == 0:
        item_max_len = 0
    else:
        item_max_len = 0
        for item in ls:
            try:
                this_length = len(str(item))
            except Exception:
                this_length = 0
            if this_length > item_max_len:
                item_max_len = this_length

    # get the longest item in the list
    max_len = max(item_max_len, len(ls_title)) + 8

    # print the top of the box
    print(f"{'-' * (max_len + 4)}")

    # print the title with padding
    print(f"| {ls_title.center(max_len)} |")

    # print the bottom of the title box
    print(f"{'-' * (max_len + 4)}")

    # print each item in the list
    for item in ls:
        if isinstance(item, str):
            print(f"| {item.ljust(max_len)} |")
        else:
            print(f"| {str(item).ljust(max_len)} |")

    # print the bottom of the list box
    print(f"{'-' * (max_len + 4)}")


def get_text_input_list_of_lists(file_path):
    with open(file_path, "r") as file:
        text_lines = file.readlines()

    ls_all_lines = []
    for text_line in text_lines:
        print(text_line)
        ls_chars = list(text_line)
        ls_all_lines.append(ls_chars)

    return ls_all_lines


def get_text_from_ls_coords(ls_ls_text, ls_coords):
    ls_text = []

    for coords in ls_coords:
        ls_text.append(ls_ls_text[coords[0]][coords[1]])

    return ls_text


def get_ls_cords(ls_ls_text, start_row, start_col, direction, num_chars=4):
    ls_coords = [[start_row, start_col]]
    prev_coords = [start_row, start_col]
    for char_idx in range(num_chars - 1):
        if direction == "up_right":
            new_coords = [prev_coords[0] - 1, prev_coords[1] + 1]
        elif direction == "up_left":
            new_coords = [prev_coords[0] - 1, prev_coords[1] - 1]
        elif direction == "down_right":
            new_coords = [prev_coords[0] + 1, prev_coords[1] + 1]
        elif direction == "down_left":
            new_coords = [prev_coords[0] + 1, prev_coords[1] - 1]
        elif direction == "right":
            new_coords = [prev_coords[0] - 0, prev_coords[1] + 1]
        elif direction == "left":
            new_coords = [prev_coords[0] - 0, prev_coords[1] - 1]
        elif direction == "up":
            new_coords = [prev_coords[0] - 1, prev_coords[1] + 0]
        elif direction == "down":
            new_coords = [prev_coords[0] + 1, prev_coords[1] + 0]
        else:
            return None

        prev_coords = new_coords

        # if out of bounds, skip
        if new_coords[0] < 0 or new_coords[0] > ((len(ls_ls_text) - 1)):
            continue
        if new_coords[1] < 0 or new_coords[1] > (len(ls_ls_text[0]) - 1):
            continue

        ls_coords.append(new_coords)

    return ls_coords


def get_all_matches_xmas(ls_ls_text):
    ls_directions = [
        "up_right",
        "up_left",
        "down_right",
        "down_left",
        "right",
        "left",
        "up",
        "down",
    ]
    search_text = "XMAS"
    ls_search_text = list(search_text)

    count_occurances = 0
    ls_coords_matches = []
    for start_row in range(len(ls_ls_text)):
        for start_col in range(len(ls_ls_text[0])):
            for direction in ls_directions:
                ls_coords = get_ls_cords(
                    ls_ls_text, start_row, start_col, direction=direction, num_chars=4
                )

                ls_text = get_text_from_ls_coords(ls_ls_text, ls_coords)
                is_match = ls_text == ls_search_text
                if is_match:
                    count_occurances += 1
                    coord_match_data = {"ls_coords": ls_coords, "direction": direction}
                    ls_coords_matches.append(coord_match_data)

    return count_occurances, ls_coords_matches


ls_ls_text = get_text_input_list_of_lists("day_04_input.txt")
pprint_ls(ls_ls_text)

count_occurances, ls_coords_matches = get_all_matches_xmas(ls_ls_text)
print(f"There are {count_occurances} of XMAS in all directions")


# %%


def get_all_matches_mas_diag(ls_ls_text):
    ls_directions = [
        "up_right",
        "up_left",
        "down_right",
        "down_left",
    ]
    search_text = "MAS"
    ls_search_text = list(search_text)

    count_occurances = 0
    ls_coords_matches = []
    for start_row in range(len(ls_ls_text)):
        for start_col in range(len(ls_ls_text[0])):
            for direction in ls_directions:
                ls_coords = get_ls_cords(
                    ls_ls_text, start_row, start_col, direction=direction, num_chars=3
                )

                ls_text = get_text_from_ls_coords(ls_ls_text, ls_coords)
                is_match = ls_text == ls_search_text
                if is_match:
                    count_occurances += 1
                    coord_match_data = {"ls_coords": ls_coords, "direction": direction}
                    ls_coords_matches.append(coord_match_data)

    return count_occurances, ls_coords_matches


ls_ls_text = get_text_input_list_of_lists("day_04_input.txt")
pprint_ls(ls_ls_text)

count_occurances, ls_coords_matches = get_all_matches_mas_diag(ls_ls_text)
print(f"There are {count_occurances} of MAS in diag directions")
pprint_ls(ls_coords_matches)

# %%


def find_intersections_of_coords(ls_coords_matches):
    ls_mid_coords = []
    for dict_data in ls_coords_matches:
        mid_coords = dict_data["ls_coords"][1]
        ls_mid_coords.append(mid_coords)

    ls_mid_coords = list((tuple(item) for item in ls_mid_coords))
    print(f"ls_mid_coords: {ls_mid_coords}")
    ls_set_mid_coords = list(set(ls_mid_coords))
    print(f"ls_set_mid_coords: {ls_set_mid_coords}")

    count_intersections = 0
    ls_intersections = []
    for unique_mid_coords in ls_set_mid_coords:
        if ls_mid_coords.count(unique_mid_coords) > 1:
            count_intersections += 1
            ls_intersections.append(unique_mid_coords)

    return count_intersections, ls_intersections


pprint_ls(ls_coords_matches)
count_intersections, ls_intersections = find_intersections_of_coords(ls_coords_matches)

pprint_ls(ls_intersections, ls_title="Ls Intersections")
print(count_intersections)


# %%
