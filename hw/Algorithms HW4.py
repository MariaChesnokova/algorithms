# 1. Even First. Your input is a list of integers, and you have to reorder its entries so that the even entries
# appear first. You are required to solve it without allocating additional storage (operate with the input list).
from typing import List


def even_first(nums):
    even = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            nums[even], nums[i] = nums[i], nums[even]
            even += 1
    return nums


example = [7, 3, 5, 6, 4, 10, 3, 2]
print(even_first(example))


# 2. Increment a Number. Write a program that takes as input a list of digits encoding a nonnegative decimal integer D
# and updates the list to represent the integer D + 1.

def increment_number(nums):
    n = len(nums)
    d = 1

    for i in range(n - 1, -1, -1):
        total = nums[i] + d
        nums[i] = total % 10
        d = total // 10

    if d == 1:
        nums.insert(0, 1)

    return nums


example = [1, 2, 9]
print(increment_number(example))
