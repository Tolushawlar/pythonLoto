def contains_007_in_order(checkList):
    pattern = [0, 0, 7]
    pattern_idx = 0

    for num in checkList:
        if num == pattern[pattern_idx]:
            pattern_idx += 1
            if pattern_idx == len(pattern):
                return True
    return False


# # Example usage:
# my_list = [1, 2, 0, 3, 0, 7, 4, 5]
# result = contains_007_in_order(my_list)
# print(result)  # Output: True

# my_list = [1, 0, 0, 7, 2, 3, 4, 5]
# result = contains_007_in_order(my_list)
# print(result)  # Output: False
