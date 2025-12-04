# %%
# Imports #


# %%
# Vars #


# %%
# Vars #


def get_text_input_lists(file_path):
    with open(file_path, "r") as file:
        test_input = file.read()

    return test_input


def get_input_data(file_path):
    test_input = get_text_input_lists(file_path)

    print("Test input:")
    print(test_input)

    ls_test_input = test_input.split(",")

    ls_test_input = [
        (ls_test_item.split("-")[0], ls_test_item.split("-")[1])
        for ls_test_item in ls_test_input
    ]

    return ls_test_input


# %%


def get_chunks(id_to_check, chunk_size, debug=False):
    if debug:
        print("-" * 50)

    ls_chunks = []

    if len(id_to_check) % chunk_size != 0:
        if debug:
            print(f"id cant be divided evenly into {chunk_size} sized chunks")
        return []

    num_chunks = int(len(id_to_check) / chunk_size)

    if debug:
        print(f"Num chunks: {num_chunks}")

    for i in range(num_chunks):
        start_index = chunk_size * i
        end_index = chunk_size * (i + 1)
        chunk = id_to_check[start_index:end_index]
        if debug:
            print(i)
            print(f"getting {start_index} - {end_index}")
        ls_chunks.append(chunk)

    return ls_chunks


id_to_check = "123123"
chunk_size = 5
ls_chunks = get_chunks(id_to_check, chunk_size, debug=True)
print(f"id_to_check: {id_to_check} = ls_chunks: {ls_chunks}")
assert not ls_chunks

id_to_check = "123123"
chunk_size = 3
ls_chunks = get_chunks(id_to_check, chunk_size, debug=True)
print(f"id_to_check: {id_to_check} = ls_chunks: {ls_chunks}")
assert len(ls_chunks) == 2

id_to_check = "123123"
chunk_size = 2
ls_chunks = get_chunks(id_to_check, chunk_size, debug=True)
print(f"id_to_check: {id_to_check} = ls_chunks: {ls_chunks}")
assert len(ls_chunks) == 3

# %%


def check_id_valid(id_to_check, debug=False):
    if debug:
        print("-" * 50)
    if id_to_check[0] == "0":
        return False
    # else:
    #     print(f"{id_to_check[0]} is not 0")

    # check for only 1 digit and repeating
    if len(set(id_to_check)) == 1 % len(id_to_check) > 1:
        return False

    # for all possible chunk sizes check if len(set(ls_chunks)) == 1
    for chunk_size in range(int(len(id_to_check) / 2), 0, -1):
        if debug:
            print(f"Checking chunk size {chunk_size}")
        ls_chunks = get_chunks(id_to_check, chunk_size)
        if len(set(ls_chunks)) == 1:
            return False

    return True


id_to_check = "12341234"
test_value = check_id_valid(id_to_check, debug=True)
print(f"Result of {id_to_check} = {test_value}")
assert not test_value


id_to_check = "1111111"
test_value = check_id_valid(id_to_check, debug=True)
print(f"Result of {id_to_check} = {test_value}")
assert not test_value

id_to_check = "123123123"
test_value = check_id_valid(id_to_check, debug=True)
print(f"Result of {id_to_check} = {test_value}")
assert not test_value

id_to_check = "2"
test_value = check_id_valid(id_to_check, debug=True)
print(f"Result of {id_to_check} = {test_value}")
assert test_value

# %%


id_to_check = "0101"
test_value = check_id_valid(id_to_check)
print(f"Result of {id_to_check} = {test_value}")
assert not test_value

id_to_check = "123"
test_value = check_id_valid(id_to_check)
print(f"Result of {id_to_check} = {test_value}")
assert test_value

id_to_check = "123456"
test_value = check_id_valid(id_to_check)
print(f"Result of {id_to_check} = {test_value}")
assert test_value

# %%


def check_range_of_ids(start_id, end_id, debug=False):
    num_invalid_ids = 0
    ls_invalid_ids = []

    for id_to_check in range(int(start_id), int(end_id) + 1):
        if debug:
            print(f"Checking id: {id_to_check}")
        if not check_id_valid(str(id_to_check)):
            if debug:
                print(f"id {id_to_check} is not valid")
            num_invalid_ids += 1
            ls_invalid_ids.append(id_to_check)

    return num_invalid_ids, ls_invalid_ids


id_range_to_test = ("11", "22")
num_invalid_ids, ls_invalid_ids = check_range_of_ids(
    id_range_to_test[0], id_range_to_test[1], debug=True
)
print(f"Result of range {id_range_to_test} = {num_invalid_ids}")
assert num_invalid_ids == 2

id_range_to_test = ("99", "115")
num_invalid_ids, ls_invalid_ids = check_range_of_ids(
    id_range_to_test[0], id_range_to_test[1], debug=True
)
print(f"Result of range {id_range_to_test} = {num_invalid_ids}")
assert num_invalid_ids == 2

# %%


def test_list_of_id_ranges(ls_id_ranges):
    num_invalid_ids = 0
    ls_invalid_ids = []

    for id_range_to_test in ls_id_ranges:
        num_invalid_ids_this_range, ls_invalid_ids_this_range = check_range_of_ids(
            id_range_to_test[0], id_range_to_test[1]
        )
        print(f"{id_range_to_test} has {num_invalid_ids_this_range} invalid ids")
        num_invalid_ids += num_invalid_ids_this_range
        ls_invalid_ids.extend(ls_invalid_ids_this_range)

    return num_invalid_ids, ls_invalid_ids


def get_sum_of_list(ls_values):
    sum_of_values = 0
    for value in ls_values:
        sum_of_values += value

    return sum_of_values


# %%


ls_test_input = get_input_data("day_02_part_01_input_test.txt")

print(ls_test_input)

num_invalid_ids, ls_invalid_ids = test_list_of_id_ranges(ls_test_input)
print(num_invalid_ids)
print(f"Sum of invalid IDs: {get_sum_of_list(ls_invalid_ids)}")

# %%


ls_test_input = get_input_data("day_02_part_01_input.txt")

print(ls_test_input)

num_invalid_ids, ls_invalid_ids = test_list_of_id_ranges(ls_test_input)
print(num_invalid_ids)
sum_of_invalid_ids = get_sum_of_list(ls_invalid_ids)
print(f"Sum of invalid IDs: {sum_of_invalid_ids}")
assert sum_of_invalid_ids == 11323661261


# %%
# Vars #
