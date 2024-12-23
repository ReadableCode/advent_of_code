# %%
# Imports #

import copy
import os
from time import sleep

from tqdm import tqdm

# %%
# Vars #


def get_text_input_lists(file_path):
    with open(file_path, "r") as file:
        text_lines = file.readlines()

    text_lines = [list(line.strip()) for line in text_lines]

    return text_lines


dict_states = {
    "#": "obstacle",
    "O": "placed_obstacle",
    ".": "untraversed",
    "^": "traversed_north",
    "v": "traversed_south",
    "<": "traversed_west",
    ">": "traversed_east",
}

dict_character_sprites = {
    "^": "north",
    "v": "south",
    "<": "west",
    ">": "east",
}

dict_direction_to_sprite = {v: k for k, v in dict_character_sprites.items()}


# %%
# Funcs #


def pprint_ls(
    ls,
):
    for item in ls:
        print(item)


def get_state_at_cords(curr_map, coords_tup):

    coords_x, coords_y = coords_tup[0], coords_tup[1]

    if (
        coords_x > len(curr_map) - 1
        or coords_x < 0
        or coords_y > len(curr_map[0]) - 1
        or coords_y < 0
    ):
        return "off_map"

    char_at_coords = curr_map[coords_x][coords_y]

    return dict_states[char_at_coords]


def find_init_of_player(curr_map):
    for i, row in enumerate(curr_map):
        if "^" in row:
            return (i, curr_map[i].index("^")), "north"


def get_coords_in_direction(coords_tup, direction):
    return_coords = coords_tup

    if direction == "north":
        return_coords = (return_coords[0] - 1, return_coords[1])
    if direction == "south":
        return_coords = (return_coords[0] + 1, return_coords[1])
    if direction == "west":
        return_coords = (return_coords[0], return_coords[1] - 1)
    if direction == "east":
        return_coords = (return_coords[0], return_coords[1] + 1)

    return return_coords


def get_rotated_direction(input_direction, rotation_direction="right"):
    order_of_directions = ["north", "east", "south", "west"]
    index_of_input_direction = order_of_directions.index(input_direction)
    if rotation_direction == "right":
        if ((index_of_input_direction + 1)) > len(order_of_directions) - 1:
            return order_of_directions[0]
        return order_of_directions[index_of_input_direction + 1]
    else:
        if ((index_of_input_direction - 1)) < 0:
            return order_of_directions[-1]
        return order_of_directions[index_of_input_direction - 1]


def take_step(curr_map, coords_tup_person, direction_facing):
    while True:
        facing_coords = get_coords_in_direction(coords_tup_person, direction_facing)
        facing_coords_state = get_state_at_cords(curr_map, facing_coords)
        if facing_coords_state in ["obstacle", "placed_obstacle"]:
            direction_facing = get_rotated_direction(input_direction=direction_facing)
        elif facing_coords_state in ["off_map"]:
            raise Exception("cant move off map")
        else:
            break

    curr_map[facing_coords[0]][facing_coords[1]] = dict_direction_to_sprite[
        direction_facing
    ]
    coords_tup_person = facing_coords

    return curr_map, coords_tup_person, direction_facing


def count_traversed_spaces(input_map):
    traversed_spaces = 0
    for row in input_map:
        for col in row:
            if (
                "traversed" in dict_states[col]
                and "untraversed" not in dict_states[col]
            ):
                traversed_spaces += 1

    return traversed_spaces


def play_out_map(
    input_map,
    init_coords_of_player,
    init_player_facing_direction,
    animate,
    sleep_time,
    max_steps,
):
    coords_of_person = init_coords_of_player
    finished_map = copy.deepcopy(input_map)
    player_facing_direction = init_player_facing_direction
    running_count_steps = 0
    while True:
        try:
            finished_map, coords_of_person, player_facing_direction = take_step(
                finished_map, coords_of_person, player_facing_direction
            )
            running_count_steps += 1
            if running_count_steps >= max_steps:
                break
            if animate:
                # clear the screen
                os.system("cls" if os.name == "nt" else "clear")
                pprint_ls(finished_map)
                sleep(sleep_time)
        except Exception as e:
            break

    was_hung = running_count_steps >= max_steps

    return finished_map, was_hung


def find_possible_obstacle_placements_coords(played_map):
    ls_coords = []
    for r, row in enumerate(played_map):
        for c, col in enumerate(row):
            if (
                "traversed" in dict_states[col]
                and "untraversed" not in dict_states[col]
            ):
                ls_coords.append((r, c))

    return ls_coords


def get_map_with_added_obstacle(input_map, obstacle_coords):
    return_map = copy.deepcopy(input_map)
    return_map[obstacle_coords[0]][obstacle_coords[1]] = "O"
    return return_map


# %%
# Main #

SLEEP_TIME = 0.06
ANIMATE = False
TEST_MODE = False
if TEST_MODE:
    input_map = get_text_input_lists("day_06_input_text.txt")
else:
    input_map = get_text_input_lists("day_06_input.txt")

print("-" * 100)
print("input_map")
pprint_ls(input_map)


# %%
# Main Part One #

init_coords_of_player, facing_direction = find_init_of_player(input_map)
finished_map, was_hung = play_out_map(
    input_map,
    init_coords_of_player,
    facing_direction,
    animate=ANIMATE,
    sleep_time=SLEEP_TIME,
    max_steps=100000,
)
print("Finished map")
pprint_ls(finished_map)
traversed_spaces = count_traversed_spaces(finished_map)
print(f"Traversed spaces: {traversed_spaces}")


# %%
# Main Part Two #

init_coords_of_player, facing_direction = find_init_of_player(input_map)
finished_map, was_hung = play_out_map(
    input_map,
    init_coords_of_player,
    facing_direction,
    animate=ANIMATE,
    sleep_time=SLEEP_TIME,
    max_steps=100000,
)
print("Finished map")
pprint_ls(finished_map)
traversed_spaces = count_traversed_spaces(finished_map)
print(f"Traversed spaces: {traversed_spaces}")

ls_possible_obstacle_coords = find_possible_obstacle_placements_coords(finished_map)
print(ls_possible_obstacle_coords)

ls_hung_coords = []
# Wrap the loop with tqdm for progress tracking
for possible_obstacle_coords in tqdm(
    ls_possible_obstacle_coords, desc="Testing obstacles", unit="obstacle"
):
    input_map_with_added_obstacle = get_map_with_added_obstacle(
        input_map, possible_obstacle_coords
    )
    finished_map_with_obstacle, was_hung = play_out_map(
        input_map_with_added_obstacle,
        init_coords_of_player,
        facing_direction,
        animate=ANIMATE,
        sleep_time=SLEEP_TIME,
        max_steps=100000,
    )

    if was_hung:
        ls_hung_coords.append(possible_obstacle_coords)

print(f"Hung Locations: {ls_hung_coords}")
print(f"Total locations that obstacle hangs map: {len(ls_hung_coords)}")

# wrong Total locations that obstacle hangs map: 283


# %%
