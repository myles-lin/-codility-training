def solution(nums):
    firstSection , backSection = sum(nums[:1]), sum(nums[1:])
    min_value = abs(firstSection - backSection)
    for P in range(1, len(nums) - 1):
        firstSection += nums[P]
        backSection -= nums[P]
        current_answer = abs(firstSection - backSection)
        if min_value > current_answer: # 如果後續的答案比目前 min_value 小，min_value 更新目前的值
            min_value = current_answer
    
    return min_value
