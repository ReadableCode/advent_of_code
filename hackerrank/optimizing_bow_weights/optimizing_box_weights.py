def minimalHeaviestSetA(box_b):
    # Write your code here
    box_a = []
    box_b.sort()
    total_weight_a = 0
    total_weight_b = sum(box_b)

    # move items from b to a until A weighs more, this will be max weight with minimal size
    while total_weight_a <= total_weight_b:
        move_value = box_b[-1]
        box_a.append(box_b.pop(-1))
        total_weight_a += move_value
        total_weight_b -= move_value

    box_a.sort()
    return box_a
