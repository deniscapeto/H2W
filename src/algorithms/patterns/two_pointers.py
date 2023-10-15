def two_pointers(array):
    left = 0
    right = len(array) - 1
    while left <= right:
        left = left + 1
        right = right -1 
