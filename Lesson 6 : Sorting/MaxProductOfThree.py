def solution(A):
    A.sort()    
    case_1 = A[-1] * A[-2] * A[-3]
    case_2 = A[0] * A[1] * A[-1]
    answer = max(case_1, case_2)
    
    return answer
