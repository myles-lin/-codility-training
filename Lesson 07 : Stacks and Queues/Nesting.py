def solution(S):
    count = 0
    for char in S:
        if char == '(':
            count += 1  # like as .append
        elif char == '/':
            return 0
        else:
            count -= 1 # like as .pop()
        
        if count < 0:
            return 0
    
    if count > 0: # To fix, S = '()(()()(((()())(()()))' 
        return 0
    else:
        return 1
      
# Analysis
# Detected time complexity: O(N)
