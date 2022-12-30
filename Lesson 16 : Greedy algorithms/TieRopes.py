def solution(K, A):
    count = 0
    length = 0
    for i in A:
        length += i
        if length >= K:
            count += 1
            length = 0
            
    return count

# Analysis
# Detected time complexity: O(N)