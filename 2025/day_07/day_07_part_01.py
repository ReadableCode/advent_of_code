# %%
# Imports #


# %%
# Vars #


def get_text_input_lines(file_path, debug=False):
    with open(file_path, "r") as file:
        text_lines = file.readlines()

    text_lines = [line.strip() for line in text_lines]

    if debug:
        print("-------- text file contents --------")
        for text_line in text_lines:
            print(text_line)
        print("------------------------------------")

    ls_cleaned_row_lists = []
    for row in text_lines:
        ls_cleaned_row_lists.append(list(row))

    return ls_cleaned_row_lists


file_path = "day_07_part_01_input_test.txt"
ls_cleaned_row_lists = get_text_input_lines(file_path, debug=False)

print("Output")
for row in ls_cleaned_row_lists:
    print(row)


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
ls_cleaned_row_lists = get_text_input_lines(file_path, debug=False)
s_loc = find_s(ls_cleaned_row_lists, debug=True)
print(s_loc)


# %%


def cast_rays(ls_cleaned_row_lists, debug=False):
    s_loc = find_s(ls_cleaned_row_lists)
    print(f"s_loc: {s_loc}")


file_path = "day_07_part_01_input_test.txt"
ls_cleaned_row_lists = get_text_input_lines(file_path, debug=False)
ls_cleaned_row_lists_w_rays = cast_rays(ls_cleaned_row_lists, debug=True)
print(s_loc)

# %%
