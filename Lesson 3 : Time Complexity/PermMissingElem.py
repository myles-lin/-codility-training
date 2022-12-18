def solution(nums):
    n = len(nums) + 1 # 缺少一個元素，總共長度為 len(nums) + 1。
    total_sum = ((n + 1) * n) // 2 # 沒有缺少元素，完整的總和。
    return total_sum - sum(nums)
