def solution(distance, leaf):
    if len(leaf) < distance:
        return -1
    elif len(leaf) == 1 and distance == 1:
        return 0
    
    steps = set(range(1, distance + 1)) # set優於list，如果使用list型態，time complexity提高，Performance變差。
    for second, value in enumerate(leaf):
        if value in steps:
            steps.remove(value)
            if len(steps) == 0:
                return second
              
    return -1
