# %%
# Imports #


# %%
# Vars #

dial_locations = [i for i in range(0, 100)]
print(f"List created from {dial_locations[0]} to {dial_locations[-1]}")
# for i, dial_item in enumerate(dial_locations):
#     print(f"i: {i}, dial_item: {dial_item}")


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

    times_passed_zero = 0
    curr_location = starting_dial_index
    for i in range(number_moves):
        print(i) if debug else None
        if direction == "L":
            if curr_location == 0:
                curr_location = len(dial_locations) - 1
                times_passed_zero += 1
            else:
                curr_location -= 1
        elif direction == "R":
            if curr_location == len(dial_locations) - 1:
                curr_location = 0
                times_passed_zero += 1
            else:
                curr_location += 1
        print(f"    curr_location: {curr_location}") if debug else None

    return dial_locations[curr_location], times_passed_zero


# ending_loc, times_passed_zero = move_dial(10, "R", 112, debug=True)
# print(f"ending_loc: {ending_loc}, times_passed_zero: {times_passed_zero}")

# ending_loc, times_passed_zero = move_dial(90, "R", 10, debug=True)
# print(f"ending_loc: {ending_loc}, times_passed_zero: {times_passed_zero}")

# ending_loc, times_passed_zero = move_dial(0, "L", 1, debug=True)
# print(f"ending_loc: {ending_loc}, times_passed_zero: {times_passed_zero}")

# ending_loc, times_passed_zero = move_dial(50, "L", 68, debug=True)
# print(f"ending_loc: {ending_loc}, times_passed_zero: {times_passed_zero}")

# ending_loc, times_passed_zero = move_dial(82, "L", 30, debug=True)
# print(f"ending_loc: {ending_loc}, times_passed_zero: {times_passed_zero}")

# ending_loc, times_passed_zero = move_dial(52, "R", 48, debug=True)
# print(f"ending_loc: {ending_loc}, times_passed_zero: {times_passed_zero}")

# ending_loc, times_passed_zero = move_dial(2, "L", 2, debug=True)
# print(f"ending_loc: {ending_loc}, times_passed_zero: {times_passed_zero}")

# Be careful: if the dial were pointing at 50, a single rotation like R1000 would cause the dial
# to point at 0 ten times before returning back to 50!
# ending_loc, times_passed_zero = move_dial(50, "R", 1000, debug=True)
# print(f"ending_loc: {ending_loc}, times_passed_zero: {times_passed_zero}")

# ending_loc, times_passed_zero = move_dial(0, "R", 1000, debug=True)
# print(f"ending_loc: {ending_loc}, times_passed_zero: {times_passed_zero}")

# ending_loc, times_passed_zero = move_dial(52, "R", 48, debug=True)
# print(f"ending_loc: {ending_loc}, times_passed_zero: {times_passed_zero}")

# ending_loc, times_passed_zero = move_dial(0, "R", 100, debug=True)
# print(f"ending_loc: {ending_loc}, times_passed_zero: {times_passed_zero}")


# %%
# Vars #


def perform_moves(starting_location, ls_moves, debug=False):
    curr_location = starting_location
    times_zero_hit = 0
    times_zero_passed = 0

    for move_item in ls_moves:
        direction = move_item[0]
        number_moves = int(move_item[1:])
        (
            print(
                f"--------------- Processing Move from {curr_location}, Move: {move_item} ---------------"
            )
            if debug
            else None
        )
        curr_location, times_passed_zero_this_move = move_dial(
            curr_location, direction, number_moves, debug=debug
        )
        (
            print(
                f"        Ended on {curr_location}, passed 0: {times_passed_zero_this_move} times"
            )
            if debug
            else None
        )
        times_zero_passed += times_passed_zero_this_move
        if curr_location == 0:
            times_zero_hit += 1
            print(f"Ending on 0, adding 1 resulting in: {times_zero_hit}")

    return curr_location, times_zero_hit, times_zero_passed


# example test 2
# ls_input = ["R1000"]
# starting_location = 50
# debug = True

# example test 3
# ls_input = ["R1000", "R1000"]
# starting_location = 50
# debug = True

# %%
# Sample #

# example test 3
ls_input = ["R100"]
starting_location = 0
debug = True
ending_location, times_zero_hit, times_zero_passed = perform_moves(
    starting_location, ls_input, debug=debug
)
print(
    f"Ending location: {ending_location}, times_zero_hit: {times_zero_hit}, times_zero_passed: {times_zero_passed}"
)
assert times_zero_passed == 1


# %%
# Sample #

ls_input = get_text_input_lists("day_01_part_01_input_test.txt")
starting_location = 50
debug = True
ending_location, times_zero_hit, times_zero_passed = perform_moves(
    starting_location, ls_input, debug=debug
)
print(
    f"Ending location: {ending_location}, times_zero_hit: {times_zero_hit}, times_zero_passed: {times_zero_passed}"
)
assert times_zero_hit == 3


# %%
# Sample Part 2 #

ls_input = get_text_input_lists("day_01_part_01_input_test.txt")
starting_location = 50
debug = True
ending_location, times_zero_hit, times_zero_passed = perform_moves(
    starting_location, ls_input, debug=debug
)
print(
    f"Ending location: {ending_location}, times_zero_hit: {times_zero_hit}, times_zero_passed: {times_zero_passed}"
)
assert times_zero_passed == 6


# %%
# Part 1 #

# part 01
ls_input = get_text_input_lists("day_01_part_01_input.txt")
starting_location = 50
debug = False
ending_location, times_zero_hit, times_zero_passed = perform_moves(
    starting_location, ls_input, debug=debug
)
print(
    f"Ending location: {ending_location}, times_zero_hit: {times_zero_hit}, times_zero_passed: {times_zero_passed}"
)
assert times_zero_hit == 969


# %%
# Part 2 #

# part 02
ls_input = get_text_input_lists("day_01_part_01_input.txt")
starting_location = 50
debug = False
ending_location, times_zero_hit, times_zero_passed = perform_moves(
    starting_location, ls_input, debug=debug
)
print(
    f"Ending location: {ending_location}, times_zero_hit: {times_zero_hit}, times_zero_passed: {times_zero_passed}"
)
# assert times_zero_passed ==


# %%
