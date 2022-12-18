def solution(N):
    bin_N = bin(N)
    tmp = 0
    seq_count = set()
    for index in range(3, len(bin_N)):
        if bin_N[index] == '0':
            tmp += 1
        else:
            seq_count.add(tmp)
            tmp = 0
            
    if len(seq_count) == 0:
        return 0
    else:
        return max(seq_count)
