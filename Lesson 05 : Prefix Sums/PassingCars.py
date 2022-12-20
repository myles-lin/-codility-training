def solution(cars):
    remaining_one_cnt = cars.count(1)
    passing_cnt = 0
    for i in range(len(cars)):
        if cars[i] == 0:
          # passing_cnt += cars[i+1:].count(1)  # 若使用此方法, cars = [0, 1] * 100000, higher big O time complexity.
            passing_cnt += remaining_one_cnt
            if passing_cnt > 1000000000:
                return -1
        else:
            remaining_one_cnt -= 1
    
    return passing_cnt
  
# Analysis
# Detected time complexity: O(N)
