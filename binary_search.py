def binary_search(list, target):
    """
    Break down a list into smaller sets untiltarget value is found.
    """

    first = 0
    last = list[-1]

    while first <= last:
        midpoint = (first + last) // 2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        elif list[midpoint] > target:
            last = midpoint - 1
    
    return None

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")


numbers = list(range(1, 11))

result = binary_search(numbers, 6)
verify(result)