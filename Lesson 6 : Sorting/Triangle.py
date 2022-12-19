def solution(A):
    A_len = len(A)
    if A_len < 3:
        return 0

    A.sort()
    for i in range(0, A_len - 2):
        if A[i] + A[i + 1] > A[i + 2]:
            return 1

    return 0
