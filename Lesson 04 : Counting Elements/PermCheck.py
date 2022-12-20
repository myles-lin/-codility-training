def solution(nums):
    n = len(nums)
    if n != len(set(nums)): # 避免 array 有重複值
        return 0
    expected_sum = ((n + 1) * n) // 2
    actual_sum = sum(nums)
    if expected_sum == actual_sum:
        return 1
      
    return 0
