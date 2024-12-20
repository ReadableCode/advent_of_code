# %%
# Imports

import re

# %%
# Functions


def get_text_input_lists(file_path):
    with open(file_path, "r") as file:
        text_lines = file.readlines()

    return text_lines


def check_list_is_one_direction(ls_to_check):
    print(f"\nRunning directional check on list: {ls_to_check}")
    ls_sorted = sorted(ls_to_check)
    ls_inverted = sorted(ls_to_check, reverse=True)

    if ls_to_check == ls_sorted:
        print(f"{ls_to_check} is all increasing")
        return True
    else:
        print(f"List is not increasing bc: {ls_to_check} != {ls_sorted}")
    if ls_to_check == ls_inverted:
        print(f"{ls_to_check} is all decreasing")
        return True
    else:
        print(f"List is not decreasing bc: {ls_to_check} != {ls_inverted}")

    return False


def check_list_doesnt_jump_too_much(ls_to_check):
    print(f"\nRunning jump check on list: {ls_to_check}")

    min_jump = 1
    max_jump = 3

    prev_item = None
    is_still_valid = True

    for item in ls_to_check:
        if not prev_item:
            prev_item = item
            continue
        difference = abs(item - prev_item)
        if difference < min_jump:
            print(f"difference between {prev_item} and {item} is too low")
            is_still_valid = False
        if difference > max_jump:
            print(f"difference between {prev_item} and {item} is too high")
            is_still_valid = False
        prev_item = item

    if is_still_valid:
        return True

    return False


def process_line_list(
    ls_to_check, check_single_removal=False, is_already_dropped=False
):

    print(f"\n\n\nProcessing line with items: {ls_to_check}")

    list_is_directional = check_list_is_one_direction(ls_to_check)

    list_doesnt_jump_wrong = check_list_doesnt_jump_too_much(ls_to_check)

    if not list_is_directional:
        print(f"List is not directional: {ls_to_check}")
    if not list_doesnt_jump_wrong:
        print(f"List jumps wrong: {ls_to_check}")

    if list_is_directional and list_doesnt_jump_wrong:
        return True

    if not check_single_removal:
        print("List invalid and check_single_removal turned off")
        return False

    if is_already_dropped:
        print("List invalid and we have already tried dropping one item")
        return False

    # Iterate using indices to remove specific occurrences
    for idx in range(len(ls_to_check)):
        ls_to_check_with_item_removed = ls_to_check.copy()
        removed_item = ls_to_check_with_item_removed.pop(idx)  # Remove by index
        print(
            f"Trying while removing {removed_item} from index: {idx}, check list is {ls_to_check_with_item_removed}"
        )

        if process_line_list(
            ls_to_check_with_item_removed, check_single_removal, is_already_dropped=True
        ):
            return True

    return False


# %%
# Main #


list_lines = get_text_input_lists("day_02_input.txt")
num_safe_lines = 0
for line_item in list_lines:
    print("-" * 100)
    ls_line_parts = re.split(r"\s+", line_item)
    if "" in ls_line_parts:
        ls_line_parts.remove("")
    ls_line_parts = [int(x) for x in ls_line_parts]

    result = process_line_list(ls_line_parts, check_single_removal=True)
    print(f"Result is: {result}")
    if result:
        num_safe_lines = num_safe_lines + 1

print(num_safe_lines)


# %%
