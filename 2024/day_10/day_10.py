# %%
# Imports #

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


def get_text_input_lists(file_path):
    with open(file_path, "r") as file:
        text_lines = file.readlines()

    # Convert each line into a list of integers
    text_lines = [list(map(int, line.strip())) for line in text_lines]

    return text_lines


def get_adjacent_spots(ls_ls_map, coords):
    north = coords[0] + 1, coords[1]
    south = coords[0] - 1, coords[1]
    east = coords[0], coords[1] + 1
    west = coords[0], coords[1] - 1

    potential_adjacents = [north, south, east, west]
    # Filter out invalid coordinates
    ls_adjacents = [
        item
        for item in potential_adjacents
        if 0 <= item[0] < len(ls_ls_map) and 0 <= item[1] < len(ls_ls_map[0])
    ]

    return ls_adjacents


def pprint_path(ls_ls_map, path):
    for step in path:
        step_height = ls_ls_map[step[0]][step[1]]
        print(f"Moving to location: {step} @ height: {step_height}")


def find_all_paths(ls_ls_map, current_path, all_paths):
    current_coords = current_path[-1]
    current_height = int(ls_ls_map[current_coords[0]][current_coords[1]])
    ls_adjacents = get_adjacent_spots(ls_ls_map, current_coords)

    path_extended = False
    for adjacent_coords in ls_adjacents:
        adjacent_height = int(ls_ls_map[adjacent_coords[0]][adjacent_coords[1]])
        if (
            current_height + 1 == adjacent_height
            and adjacent_coords not in current_path
        ):
            # Add this adjacent step to the current path and continue exploring
            find_all_paths(ls_ls_map, current_path + [adjacent_coords], all_paths)
            path_extended = True

    # If no further steps can be made, save the current path
    if not path_extended:
        all_paths.append(current_path)


def get_all_paths(ls_ls_map, start_coords):
    all_paths = []
    find_all_paths(ls_ls_map, [start_coords], all_paths)

    return all_paths


def score_trailhead_paths(ls_ls_map, all_paths, allow_dupe_nines=True):
    ls_reachable_nines = []
    for path in all_paths:
        reachable_nine_coords = path[-1]
        nine_height = int(ls_ls_map[reachable_nine_coords[0]][reachable_nine_coords[1]])
        if nine_height != 9:
            continue
        reachable_nine = str(reachable_nine_coords)
        print(f"reachable_nine: {reachable_nine}")
        ls_reachable_nines.append(reachable_nine)

    if not allow_dupe_nines:
        ls_reachable_nines = list(set(ls_reachable_nines))

    return len(ls_reachable_nines)


def score_all_trailheads(ls_ls_map):
    dict_trailheads = {}
    running_score = 0
    for row_index, row in enumerate(ls_ls_map):
        for col_index, cell in enumerate(row):
            if cell == 0:
                trailhead_coords = (row_index, col_index)
                print(f"trailhead_coords: {trailhead_coords}")
                dict_trailheads[str(trailhead_coords)] = {}
                all_paths = get_all_paths(ls_ls_map, trailhead_coords)
                score = score_trailhead_paths(ls_ls_map, all_paths)
                dict_trailheads[str(trailhead_coords)]["score"] = score
                running_score += score

    return dict_trailheads, running_score


# %%
# Main #


TEST_MODE = False
if TEST_MODE:
    input_file = "day_10_input_test.txt"
else:
    input_file = "day_10_input.txt"

ls_ls_map = get_text_input_lists(input_file)

print("-" * 100)
pprint_ls(ls_ls_map)


# %%

print("-" * 100)


dict_trailheads, running_score = score_all_trailheads(ls_ls_map)
print("Results")
pprint_dict(dict_trailheads)
print(f"Score: {running_score}")

print("-" * 100)


# %%
