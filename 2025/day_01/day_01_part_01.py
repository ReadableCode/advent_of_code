# %%
# Imports #


# %%
# Vars #

dial_locations = [i for i in range(0, 100)]
print(f"List created from {dial_locations[0]} to {dial_locations[-1]}")


# %%
# Vars #


def move_dial(starting_location, direction, number_moves, debug=False):

    starting_dial_index = dial_locations.index(int(starting_location))
    print(f"starting_index: {starting_dial_index}") if debug else None

    if direction == "L":
        number_moves = number_moves * -1

    print(f"number_moves: {number_moves}") if debug else None

    while True:
        if (starting_dial_index + number_moves) < 0:
            print("Wrapping leftward") if debug else None
            number_moves += len(dial_locations)
            print(f"Moving {number_moves} instead") if debug else None
        elif (starting_dial_index + number_moves) > len(dial_locations) - 1:
            print("wrapping rightward") if debug else None
            number_moves -= len(dial_locations)
            print(f"Moving {number_moves} instead") if debug else None
        else:
            (
                print(f"Returning dial_locations[{starting_dial_index + number_moves}]")
                if debug
                else None
            )
            return dial_locations[starting_dial_index + number_moves]


# print(move_dial(10, "R", 112, debug=True))

# print(move_dial(90, "R", 10, debug=True))

# print(move_dial(0, "L", 1, debug=True))

# print(move_dial(50, "L", 68, debug=True))

# print(move_dial(82, "L", 30, debug=True))

# print(move_dial(52, "R", 48, debug=True))


# %%
# Vars #


def perform_moves(starting_location, ls_moves):
    curr_location = starting_location
    times_zero_hit = 0
    for move_item in ls_moves:
        direction = move_item[0]
        number_moves = int(move_item[1:])
        print(
            f"Processing Move from {curr_location} with direction: {direction}, number_moves: {number_moves}"
        )
        curr_location = move_dial(curr_location, direction, number_moves)
        print(f"        Ended on {curr_location}")
        if curr_location == 0:
            times_zero_hit += 1

    return curr_location, times_zero_hit


def get_text_input_lists(file_path):
    with open(file_path, "r") as file:
        text_lines = file.readlines()

    text_lines = [line.strip() for line in text_lines]

    return text_lines


# example test
# ls_input = get_text_input_lists("day_01_part_01_input_test.txt")
# starting_location = 50

# part 01
ls_input = get_text_input_lists("day_01_part_01_input.txt")
starting_location = 50

print(ls_input)

ending_location, times_zero_hit = perform_moves(starting_location, ls_input)
print(f"Ending location: {ending_location}, times_zero_hit: {times_zero_hit}")


# %%
# Vars #
