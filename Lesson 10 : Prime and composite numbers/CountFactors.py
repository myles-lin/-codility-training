def solution(N):
    factors = set()
    i = 1
    while i**2 <= N:
        if N % i == 0:
            factors.add(i)
            factors.add(N // i)
        i += 1
            
    result = len(factors)
    return result
  
# Analysis
# Detected time complexity: O(sqrt(N))
