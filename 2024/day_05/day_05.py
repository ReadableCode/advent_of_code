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


ls_rules, ls_safety_manuals = get_text_input("day_05_input.txt")

# %%

pprint_ls(ls_rules, "ls_rules")


# %%


pprint_ls(ls_safety_manuals, "ls_safety_manuals")


# %%


def validate_safety_manual(safety_manual_page_order, ls_rules):
    print(f"Safety manual page order: {safety_manual_page_order}")
    for rule in ls_rules:
        first_page, second_page = rule.split("|")
        print(f"first_page: {first_page}, second_page: {second_page}")

        if (
            first_page not in safety_manual_page_order
            or second_page not in safety_manual_page_order
        ):
            print(f"Both pages not found")
            continue

        first_page_loc = safety_manual_page_order.index(first_page)
        second_page_loc = safety_manual_page_order.index(second_page)
        print(f"First page loc: {first_page_loc}")
        print(f"Second page loc: {second_page_loc}")

        if first_page_loc > second_page_loc:
            print(
                f"first_page: {first_page}@{first_page_loc} is not before second_page: {second_page}@{second_page_loc}"
            )
            return False

    return True


def get_pages_and_sum_valid_safety_manuals(ls_rules, ls_safety_manuals):
    ls_passing_middle_pages = []
    total_sum_of_added_middle_pages = 0
    for safety_manual in ls_safety_manuals:
        safety_manual_page_order = safety_manual.split(",")
        result = validate_safety_manual(safety_manual_page_order, ls_rules)
        if result:
            middle_index_of_manual = int((len(safety_manual_page_order) - 1) / 2)
            middle_page_of_manual = safety_manual_page_order[middle_index_of_manual]
            ls_passing_middle_pages.append(middle_page_of_manual)
            total_sum_of_added_middle_pages += int(middle_page_of_manual)

    return ls_passing_middle_pages, total_sum_of_added_middle_pages


ls_test_safety_manuals = ["75,47,61,53,29", "75,97,47,61,53"]
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

ls_passing_middle_pages, total_sum_of_added_middle_pages = (
    get_pages_and_sum_valid_safety_manuals(ls_test_rules, ls_test_safety_manuals)
)

print(ls_passing_middle_pages)
print(total_sum_of_added_middle_pages)


# %%


ls_passing_middle_pages, total_sum_of_added_middle_pages = (
    get_pages_and_sum_valid_safety_manuals(ls_rules, ls_safety_manuals)
)

print(ls_passing_middle_pages)
print(total_sum_of_added_middle_pages)


# %%
