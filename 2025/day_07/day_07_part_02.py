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


def count_timelines(grid):
    H = len(grid)
    W = len(grid[0])

    # --- find S ---
    start = None
    for r in range(H):
        for c in range(W):
            if grid[r][c] == "S":
                start = (r + 1, c)
                break
        if start:
            break

    memo = {}  # <-- the crucial addition

    def dfs(r, c, visited):
        # out of bounds → finished timeline
        if r < 0 or r >= H or c < 0 or c >= W:
            return 1

        state = (r, c)

        # cycle protection (rare here)
        if state in visited:
            return 0

        # memoized result?
        if state in memo:
            return memo[state]

        visited.add(state)
        cell = grid[r][c]

        # empty or S → continue downward
        if cell == "." or cell == "S":
            result = dfs(r + 1, c, visited)
            memo[state] = result
            return result

        # splitter → spawn left + right, both downward
        if cell == "^":
            left = dfs(r + 1, c - 1, visited.copy())
            right = dfs(r + 1, c + 1, visited.copy())
            result = left + right
            memo[state] = result
            return result

        memo[state] = 0
        return 0

    return dfs(start[0], start[1], set())


file_path = "day_07_part_01_input_test.txt"
grid = get_text_input_lines(
    file_path, debug=False
)  # list of strings or list of list of chars is fine

ans = count_timelines(grid)
print(ans)
assert ans == 40


# %%

file_path = "day_07_part_01_input.txt"
grid = get_text_input_lines(file_path, debug=False)
print(s_loc)

ans = count_timelines(grid)
print(ans)
assert ans == 135656430050438

# %%
