def recursive_binary_search(list, target):
    """
    Return boolean value if target value exists
    """

    if len(list) == 0:
        return False
    else: 
        midpoint = len(list) // 2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:], target)
            elif list[midpoint] > target:
                return recursive_binary_search(list[:midpoint], target)

def verify(result):
    print("Target found: ", result)


numbers = list(range(1, 11))

result = recursive_binary_search(numbers, 6)
verify(result)
        