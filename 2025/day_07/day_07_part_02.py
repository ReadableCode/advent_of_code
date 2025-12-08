# %%
# Imports #


# %%
# Vars #


def print_text_lines(text_lines):
    print("-------- text file contents --------")
    for text_line in text_lines:
        print(text_line)
    print("------------------------------------")


def get_text_input_lines(file_path, debug=False):
    with open(file_path, "r") as file:
        text_lines = file.readlines()

    text_lines = [line.strip() for line in text_lines]

    if debug:
        print_text_lines(text_lines)

    ls_cleaned_row_lists = []
    for row in text_lines:
        ls_cleaned_row_lists.append(list(row))

    return ls_cleaned_row_lists


file_path = "day_07_part_01_input_test.txt"
ls_cleaned_row_lists_w_rays = get_text_input_lines(file_path, debug=False)

print("Output")
print_text_lines(ls_cleaned_row_lists_w_rays)


# %%


def find_s(ls_cleaned_row_lists, debug=False):
    for row_num in range(0, len(ls_cleaned_row_lists)):
        for col_num in range(0, len(ls_cleaned_row_lists[0])):
            if debug:
                print(f"row_num: {row_num}, col_num: {col_num}")
            if ls_cleaned_row_lists[row_num][col_num] == "S":
                s_loc = (row_num, col_num)
                return s_loc

    raise Exception("Couldnt find s")


file_path = "day_07_part_01_input_test.txt"
ls_cleaned_row_lists_w_rays = get_text_input_lines(file_path, debug=False)
s_loc = find_s(ls_cleaned_row_lists_w_rays, debug=True)
print(s_loc)


# %%


def cast_rays(ls_cleaned_row_lists, debug=False):
    s_loc = find_s(ls_cleaned_row_lists)
    print(f"s_loc: {s_loc}")

    # put ray below S
    ls_cleaned_row_lists[s_loc[0] + 1][s_loc[1]] = "|"
    print_text_lines(ls_cleaned_row_lists)

    for row_num in range(0, len(ls_cleaned_row_lists)):
        for col_num in range(0, len(ls_cleaned_row_lists[0])):
            cell_value_above = ls_cleaned_row_lists[row_num - 1][col_num]
            cell_value = ls_cleaned_row_lists[row_num][col_num]

            if (cell_value == "^") and (cell_value_above == "|"):
                ls_cleaned_row_lists[row_num][col_num - 1] = "|"
                ls_cleaned_row_lists[row_num][col_num + 1] = "|"
            elif cell_value_above == "|":
                ls_cleaned_row_lists[row_num][col_num] = "|"

    print_text_lines(ls_cleaned_row_lists)
    return ls_cleaned_row_lists


def count_splits(ls_cleaned_row_lists_w_rays):
    count = 0
    for row_num in range(0, len(ls_cleaned_row_lists_w_rays)):
        for col_num in range(0, len(ls_cleaned_row_lists_w_rays[0])):
            cell_value_above = ls_cleaned_row_lists_w_rays[row_num - 1][col_num]
            cell_value = ls_cleaned_row_lists_w_rays[row_num][col_num]
            if (cell_value == "^") and (cell_value_above == "|"):
                count += 1

    return count


file_path = "day_07_part_01_input_test.txt"
ls_cleaned_row_lists_w_rays = get_text_input_lines(file_path, debug=False)
ls_cleaned_row_lists_w_rays = cast_rays(ls_cleaned_row_lists_w_rays, debug=True)
print(s_loc)
count = count_splits(ls_cleaned_row_lists_w_rays)
print(count)
assert count == 21


# %%

file_path = "day_07_part_01_input.txt"
ls_cleaned_row_lists_w_rays = get_text_input_lines(file_path, debug=False)
ls_cleaned_row_lists_w_rays = cast_rays(ls_cleaned_row_lists_w_rays, debug=True)
print(s_loc)
count = count_splits(ls_cleaned_row_lists_w_rays)
print(count)

# %%
