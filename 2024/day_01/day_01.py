# %%
# Imports

import re

# %%
# Functions


def get_text_input_lists(file_path):
    list_a = []
    list_b = []
    with open(file_path, "r") as file:
        text_lines = file.readlines()

    for line in text_lines:
        # Strip the line to remove leading/trailing whitespace
        line = line.strip()
        # Use re.split to split on one or more spaces or tabs
        parts = re.split(r"\s+", line)
        if len(parts) >= 2:  # Ensure there are at least two items
            item_a = parts[0]
            item_b = parts[1]
            list_a.append(item_a)
            list_b.append(item_b)

    return list_a, list_b


# Example usage
list_a, list_b = get_text_input_lists("input.txt")
print("List A:", list_a)
print("List B:", list_b)

# sort both lists
list_a.sort()
list_b.sort()

print("Sorted List A:", list_a)
print("Sorted List B:", list_b)

list_distances = []
# calculate distances between lists
for i in range(len(list_a)):
    print(
        "Distance between",
        list_a[i],
        "and",
        list_b[i],
        "is",
        abs(int(list_a[i]) - int(list_b[i])),
    )
    list_distances.append(abs(int(list_a[i]) - int(list_b[i])))

print("List of distances:", list_distances)
print("Sum of distances:", sum(list_distances))


# %%
