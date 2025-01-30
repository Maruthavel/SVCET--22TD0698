def find_unique_number(nums):
    unique_number = 0
    for num in nums:
        unique_number ^= num
    return unique_number
nums = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 7]
print("The unique number is:", find_unique_number(nums))
