def positive_sum(arr):
    pos_sum = 0
    if len(arr) < 1:
        return 0
    for element in arr:
        if element > 0:
            pos_sum += element
    return pos_sum
