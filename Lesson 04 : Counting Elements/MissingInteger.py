def solution(nums):
    nums_int = [i for i in set(nums) if i > 0]
    nums_int.sort() # 需要排序， 若沒有排序 nums = [1, 10000] 會出問題
    nums_int_len = len(nums_int)

    if nums_int_len == 0 or nums_int[0] != 1:
        return 1
    elif nums_int[-1] == nums_int_len:
        return nums_int_len + 1
    
    count = 1
    for i in range(0, len(nums_int)):
        if nums_int[i] == count:
            count += 1
        else:
            return count
