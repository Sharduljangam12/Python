#1. Remove duplicates from a list using a set
#nums = [1, 2, 2, 3, 4, 4, 5]
# Expected Output: [1, 2, 3, 4, 5]
nums = [1, 2, 2, 3, 4, 4, 5]
unique_nums = list(set(nums))
print(unique_nums)