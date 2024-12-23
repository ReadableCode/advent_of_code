# %%
# Imports #


# %%
# Vars #


test_input_map = get_text_input_lists("day_06_input_text.txt")
input_map = get_text_input_lists("day_06_input.txt")


# %%
# Funcs #


def pprint_ls(
    ls,
):
    for item in ls:
        print(item)


def get_text_input_lists(file_path):
    with open(file_path, "r") as file:
        text_lines = file.readlines()

    text_lines = [list(line.strip()) for line in text_lines]

    return text_lines


def get_state_at_cords(curr_map, coords_tup):
    char_at_coords = curr_map[coords_tup[0]][coords_tup[1]]
    dict_states = {
        "#": "obstacle",
        ".": "untraversed",
        "^": "traversed_north",
        "v": "traversed_south",
        "<": "traversed_west",
        ">": "traversed_east",
    }

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


def take_step(curr_map, coords_tup_person, direction_facing):
    pass


print("-" * 100)
print("test_input_map")
pprint_ls(test_input_map)
state_at_coords = get_state_at_cords(test_input_map, (0, 4))
print(f"state_at_coords: {state_at_coords}")
init_coords_of_player, facing_direction = find_init_of_player(test_input_map)
print(f"init_coords_of_player: {init_coords_of_player}, facing: {facing_direction}")
next_coords = get_coords_in_direction(init_coords_of_player, "north")
print(f"next_coords: {next_coords}")


# %%
# Imports #


# %%
# Imports #


# %%
# Vars #


print("-" * 100)
print("test_input_map")
pprint_ls(test_input_map)


# %%
# Vars #

print("-" * 100)
print("input_map")
pprint_ls(input_map)


# %%
# Main #


state_at_coords = get_state_at_cords(test_input_map, (0, 4))
print(f"state_at_coords: {state_at_coords}")
init_coords_of_player, facing_direction = find_init_of_player(test_input_map)
print(f"init_coords_of_player: {init_coords_of_player}")


# %%
