def solution(S):
    rights = [')', ']', '}']
    lefts = ['(', '[', '{']
    
    op_stack = list()
    for char in S:
        if char in lefts:
            op_stack.append(char)
        elif char in rights:
            if len(op_stack) != 0 and op_stack[-1] == lefts[rights.index(char)]: # To fix, when S = '())(()'
                op_stack.pop()
            else:
                return 0
        else:
            op_stack.append(char)
            
    if len(op_stack) == 0:    
        return 1
    else:
        return 0
      
# Analysis
# Detected time complexity: O(N)
