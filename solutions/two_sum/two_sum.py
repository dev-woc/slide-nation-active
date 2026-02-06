def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = round(target - num, 2)
        if complement in seen:
            return seen[complement], i
        seen[round(num, 2)] = i
    return None
