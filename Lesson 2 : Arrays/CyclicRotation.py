def solution(A, K):
    if len(A) == 0 or K % len(A) == 0:
        return A
      
    B = [None] * len(A)
    for i in range(len(A)):
        K %= len(A)
        B[i] = A[i-K]

    return B
