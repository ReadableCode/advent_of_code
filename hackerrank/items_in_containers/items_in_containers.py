def numberOfItems(s, startIndices, endIndices):
    result = []
    for start, end in zip(startIndices, endIndices):
        count = 0
        in_container = False
        item_count = 0
        for i in range(start - 1, end):
            if s[i] == "|":
                if in_container:
                    count += item_count
                in_container = True
                item_count = 0
            elif s[i] == "*" and in_container:
                item_count += 1
        result.append(count)
    return result
