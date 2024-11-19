def groups_of_3(numbers: list[int]) -> list[list[int]]:
    result = []
    group = []
    for num in numbers:
        group.append(num)
        if len(group) == 3:
            result.append(group)
            group = []
    if group:
        result.append(group)
    return result


