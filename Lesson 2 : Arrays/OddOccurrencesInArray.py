from collections import defaultdict

def solution(A):
    value_dict = defaultdict(int)
    for value in A:
        value_dict[value] += 1
    
    for key in value_dict:
        if value_dict[key] % 2 == 1:
            return key
