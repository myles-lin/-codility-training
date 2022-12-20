from collections import defaultdict

def solution(nums):
    nums_len = len(nums)
    if nums_len == 0:
        return -1

    value_cnt = defaultdict(int)

    for value in nums:
        value_cnt[value] += 1

    max_value_sort = sorted(value_cnt, key=lambda x:value_cnt[x])
    max_cnt_value = max_value_sort[-1] #排序後出現最多次的 value 

    if value_cnt[max_cnt_value] > nums_len//2:
        return nums.index(max_cnt_value)
    
    return -1
  
# Analysis
# Detected time complexity: O(N*log(N)) or O(N)
