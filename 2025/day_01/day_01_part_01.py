# %%
# Imports #


# %%
# Vars #

dial_locations = [i for i in range(0, 100)]
print(f"List created from {dial_locations[0]} to {dial_locations[-1]}")


# %%
# Vars #


def get_text_input_lists(file_path):
    with open(file_path, "r") as file:
        text_lines = file.readlines()

    text_lines = [line.strip() for line in text_lines]

    return text_lines


# %%
# Vars #


def move_dial(starting_location, direction, number_moves, debug=False):

    starting_dial_index = dial_locations.index(int(starting_location))
    print(f"starting_index: {starting_dial_index}") if debug else None

    if direction == "L":
        number_moves = number_moves * -1

    print(f"number_moves: {number_moves}") if debug else None

    times_passed_zero = 0
    while True:
        if (starting_dial_index + number_moves) < 0:
            print("Wrapping leftward") if debug else None
            number_moves += len(dial_locations)
            print(f"Moving {number_moves} instead") if debug else None
            times_passed_zero += 1
        elif (starting_dial_index + number_moves) > len(dial_locations) - 1:
            print("wrapping rightward") if debug else None
            number_moves -= len(dial_locations)
            print(f"Moving {number_moves} instead") if debug else None
            times_passed_zero += 1
        else:
            (
                print(f"Returning dial_locations[{starting_dial_index + number_moves}]")
                if debug
                else None
            )
            ending_loc = dial_locations[starting_dial_index + number_moves]
            if ending_loc == 0:
                times_passed_zero += 1
            print(
                f"Returning ending_loc: {ending_loc}, times_passed_zero: {times_passed_zero}"
            )
            return ending_loc, times_passed_zero


# print(move_dial(10, "R", 112, debug=True))

# print(move_dial(90, "R", 10, debug=True))

# print(move_dial(0, "L", 1, debug=True))

# print(move_dial(50, "L", 68, debug=True))

# print(move_dial(82, "L", 30, debug=True))

# print(move_dial(52, "R", 48, debug=True))

# print(move_dial(2, "L", 2, debug=True))

# Be careful: if the dial were pointing at 50, a single rotation like R1000 would cause the dial to point at 0 ten times before returning back to 50!
# print(move_dial(50, "R", 1000, debug=True))

# print(move_dial(0, "R", 1000, debug=True))

#  52, Move: R48
print(move_dial(52, "R", 48, debug=True))


# %%
# Vars #


def perform_moves(starting_location, ls_moves, debug=False):
    curr_location = starting_location
    times_zero_hit = 0
    times_zero_passed = 0
    for move_item in ls_moves:
        direction = move_item[0]
        number_moves = int(move_item[1:])
        print(
            f"--------------- Processing Move from {curr_location}, Move: {move_item} ---------------"
        )
        curr_location, times_passed_zero_this_move = move_dial(
            curr_location, direction, number_moves, debug=debug
        )
        print(
            f"        Ended on {curr_location}, passed 0: {times_passed_zero_this_move} times"
        )
        times_zero_passed += times_passed_zero_this_move
        if curr_location == 0:
            times_zero_hit += 1

    return curr_location, times_zero_hit, times_zero_passed


# example test
ls_input = get_text_input_lists("day_01_part_01_input_test.txt")
starting_location = 50
debug = True

# example test 2
# ls_input = ["R1000"]
# starting_location = 50
# debug = True

# example test 3
# ls_input = ["R1000", "R1000"]
# starting_location = 50
# debug = True

# example test 3
# ls_input = ["L50"]
# starting_location = 50
# debug = True

# part 01 and part 02
# ls_input = get_text_input_lists("day_01_part_01_input.txt")
# starting_location = 50
# debug = False

print(ls_input)

ending_location, times_zero_hit, times_zero_passed = perform_moves(
    starting_location, ls_input, debug=debug
)
print(
    f"Ending location: {ending_location}, times_zero_hit: {times_zero_hit}, times_zero_passed: {times_zero_passed}"
)


# %%
# Vars #
