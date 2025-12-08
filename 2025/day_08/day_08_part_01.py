# %%
# Imports #

from math import sqrt

import numpy as np

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

    return text_lines


file_path = "day_08_part_01_input_test.txt"
ls_cleaned_row_lists = get_text_input_lines(file_path, debug=True)
for text_line in ls_cleaned_row_lists:
    print(text_line)


def get_list_points(file_path):
    ls_cleaned_row_lists = get_text_input_lines(file_path)

    ls_points = []
    for text_line in ls_cleaned_row_lists:
        ls_point = text_line.split(",")
        ls_points.append((int(ls_point[0]), int(ls_point[1]), int(ls_point[2])))

    return ls_points


file_path = "day_08_part_01_input_test.txt"
ls_points = get_list_points(file_path)
for point in ls_points:
    print(point)

# %%


def distance_between_points(point_a, point_b):
    distance = sqrt(
        ((point_a[0] - point_b[0]) ** 2)
        + ((point_a[1] - point_b[1]) ** 2)
        + ((point_a[2] - point_b[2]) ** 2)
    )

    return distance


point_a = (10, 10, 10)
point_b = (20, 10, 10)
distance = distance_between_points(point_a, point_b)
print(distance)
assert distance == 10


# %%


def find_closest_unconnected(ls_points, ls_connections):
    min_distance = np.inf
    min_distance_points = None

    for start_point in ls_points:
        for end_point in ls_points:
            if [start_point, end_point] in ls_connections:
                print(f"already connected: {[start_point, end_point]}")
            distance_these_points = distance_between_points(start_point, end_point)
            if distance_these_points < min_distance:
                min_distance = distance_these_points
                min_distance_points = [start_point, end_point]

    return min_distance, min_distance_points


def make_connections(ls_points):
    ls_groups = []
    ls_connections = []

    min_distance, min_distance_points = find_closest_unconnected(
        ls_points, ls_connections
    )


file_path = "day_08_part_01_input_test.txt"
ls_points = get_list_points(file_path)
for point in ls_points:
    print(point)

dict_distances = make_connections(ls_points)


# %%
