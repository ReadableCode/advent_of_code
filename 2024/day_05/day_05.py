# %%
# Imports

import re

# %%
# Functions


def pprint_ls(ls, ls_title="List"):
    """
    Pretty prints a list with a title.

    Args:
        ls (list): The list to print.
        ls_title (str): The title of the list.

    Returns:
        None
    """

    # if list is empty return
    if len(ls) == 0:
        item_max_len = 0
    else:
        item_max_len = 0
        for item in ls:
            try:
                this_length = len(str(item))
            except Exception:
                this_length = 0
            if this_length > item_max_len:
                item_max_len = this_length

    # get the longest item in the list
    max_len = max(item_max_len, len(ls_title)) + 8

    # print the top of the box
    print(f"{'-' * (max_len + 4)}")

    # print the title with padding
    print(f"| {ls_title.center(max_len)} |")

    # print the bottom of the title box
    print(f"{'-' * (max_len + 4)}")

    # print each item in the list
    for item in ls:
        if isinstance(item, str):
            print(f"| {item.ljust(max_len)} |")
        else:
            print(f"| {str(item).ljust(max_len)} |")

    # print the bottom of the list box
    print(f"{'-' * (max_len + 4)}")


def get_text_input(file_path):
    with open(file_path, "r") as file:
        text_lines = file.readlines()

    ls_rules = []
    ls_safety_manuals = []

    for text_line in text_lines:
        if "|" in text_line:
            ls_rules.append(text_line.strip())
        elif "," in text_line:
            ls_safety_manuals.append(text_line.strip())

    return ls_rules, ls_safety_manuals


def validate_safety_manual(safety_manual_page_order, ls_rules):
    print(
        f"Validate Safety Manual: Safety manual page order: {safety_manual_page_order}"
    )
    for rule in ls_rules:
        first_page, second_page = rule.split("|")

        if (
            first_page not in safety_manual_page_order
            or second_page not in safety_manual_page_order
        ):
            continue

        first_page_loc = safety_manual_page_order.index(first_page)
        second_page_loc = safety_manual_page_order.index(second_page)

        if first_page_loc > second_page_loc:
            return False

    return True


def get_perfect_order(rules):
    # Extract all unique pages
    pages = set()
    for rule in rules:
        left, right = rule.split("|")
        pages.add(left)
        pages.add(right)

    # Build adjacency list and in-degree dictionary
    adjacency_list = {page: [] for page in pages}
    in_degree = {page: 0 for page in pages}

    for rule in rules:
        left, right = rule.split("|")
        adjacency_list[left].append(right)
        in_degree[right] += 1

    # Initialize order and find pages with no dependencies
    order = []
    no_dependencies = [page for page in pages if in_degree[page] == 0]

    # Perform topological sort
    while no_dependencies:
        current = no_dependencies.pop()
        order.append(current)

        for neighbor in adjacency_list[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                no_dependencies.append(neighbor)

    # Check for cycles (if not all pages are in order)
    if len(order) != len(pages):
        raise ValueError("Invalid rules: cyclic dependency detected!")

    return order


def correct_invalid_safety_manual(safety_manual_page_order, ls_rules):
    starting_order = safety_manual_page_order.copy()

    perfect_order = get_perfect_order(ls_test_rules)
    fixed_safety_manual_order = [
        perf_item
        for perf_item in perfect_order
        if perf_item in safety_manual_page_order
    ]
    for non_ruled_item in safety_manual_page_order:
        if non_ruled_item not in perfect_order:
            fixed_safety_manual_order.append(non_ruled_item)
    print(
        f"Fixed Invalid Safety Mnaual: Starting Order was: {starting_order} > Fixed List is: {fixed_safety_manual_order}"
    )
    return fixed_safety_manual_order


def get_pages_and_sum_valid_safety_manuals(ls_rules, ls_safety_manuals):
    ls_passing_middle_pages = []
    total_sum_of_already_passing_middle_pages = 0
    ls_fixed_middle_pages = []
    total_sum_of_fixed_middle_pages = 0
    for safety_manual in ls_safety_manuals:
        print("-" * 100)
        safety_manual_page_order = safety_manual.split(",")
        result = validate_safety_manual(safety_manual_page_order, ls_rules)
        if result:
            middle_index_of_manual = int((len(safety_manual_page_order) - 1) / 2)
            middle_page_of_manual = safety_manual_page_order[middle_index_of_manual]
            ls_passing_middle_pages.append(middle_page_of_manual)
            total_sum_of_already_passing_middle_pages += int(middle_page_of_manual)
        else:
            safety_manual_page_order = correct_invalid_safety_manual(
                safety_manual_page_order, ls_rules
            )
            middle_index_of_manual = int((len(safety_manual_page_order) - 1) / 2)
            print(middle_index_of_manual)
            print(safety_manual_page_order)
            print(len((safety_manual_page_order)))
            middle_page_of_manual = safety_manual_page_order[middle_index_of_manual]
            ls_fixed_middle_pages.append(middle_page_of_manual)
            total_sum_of_fixed_middle_pages += int(middle_page_of_manual)

    return (
        ls_passing_middle_pages,
        total_sum_of_already_passing_middle_pages,
        ls_fixed_middle_pages,
        total_sum_of_fixed_middle_pages,
    )


# %%
# Test 1: Corrections #

ls_test_safety_manuals = [
    "75,47,61,53,29",
    "97,61,53,29,13",
    "75,29,13",
    "75,97,47,61,53",
    "61,13,29",
    "97,13,75,29,47",
]
ls_test_rules = [
    "47|53",
    "97|13",
    "97|61",
    "97|47",
    "75|29",
    "61|13",
    "75|53",
    "29|13",
    "97|29",
    "53|29",
    "61|53",
    "97|53",
    "61|29",
    "47|13",
    "75|47",
    "97|75",
    "47|61",
    "75|61",
    "47|29",
    "75|13",
    "53|13",
]

for safety_manual_page_order in ls_test_safety_manuals:
    print("-" * 100)
    safety_manual_page_order = correct_invalid_safety_manual(
        safety_manual_page_order.split(","), ls_test_rules
    )
    print(safety_manual_page_order)


# %%
# Test 2: All Functions#


ls_test_safety_manuals = [
    "75,47,61,53,29",
    "97,61,53,29,13",
    "75,29,13",
    "75,97,47,61,53",
    "61,13,29",
    "97,13,75,29,47",
]
ls_test_rules = [
    "47|53",
    "97|13",
    "97|61",
    "97|47",
    "75|29",
    "61|13",
    "75|53",
    "29|13",
    "97|29",
    "53|29",
    "61|53",
    "97|53",
    "61|29",
    "47|13",
    "75|47",
    "97|75",
    "47|61",
    "75|61",
    "47|29",
    "75|13",
    "53|13",
]

(
    ls_passing_middle_pages,
    total_sum_of_already_passing_middle_pages,
    ls_fixed_middle_pages,
    total_sum_of_fixed_middle_pages,
) = get_pages_and_sum_valid_safety_manuals(ls_test_rules, ls_test_safety_manuals)

print("########## Test ###########")
print(f"ls_passing_middle_pages: {ls_passing_middle_pages}")
print(
    f"total_sum_of_already_passing_middle_pages: {total_sum_of_already_passing_middle_pages}"
)
print(f"ls_fixed_middle_pages: {ls_fixed_middle_pages}")
print(f"total_sum_of_fixed_middle_pages: {total_sum_of_fixed_middle_pages}")


# %%
# Real #

ls_rules, ls_safety_manuals = get_text_input("day_05_input.txt")

pprint_ls(ls_rules, "ls_rules")
pprint_ls(ls_safety_manuals, "ls_safety_manuals")

(
    ls_passing_middle_pages,
    total_sum_of_already_passing_middle_pages,
    ls_fixed_middle_pages,
    total_sum_of_fixed_middle_pages,
) = get_pages_and_sum_valid_safety_manuals(ls_rules, ls_safety_manuals)

print("########## Real ###########")
print(f"ls_passing_middle_pages: {ls_passing_middle_pages}")
print(
    f"total_sum_of_already_passing_middle_pages: {total_sum_of_already_passing_middle_pages}"
)
print(f"ls_fixed_middle_pages: {ls_fixed_middle_pages}")
print(f"total_sum_of_fixed_middle_pages: {total_sum_of_fixed_middle_pages}")
print(
    f"Sum of all correct page numbers: {total_sum_of_already_passing_middle_pages + total_sum_of_fixed_middle_pages}"
)


# %%
