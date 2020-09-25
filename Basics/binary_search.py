def binary_search(numbers, Target, low, high):
    """[summary]

    Args:
        numbers ([list]): [List of numbers in which we want to search]
        Target ([int]): [Number we want to find]
        low ([int]): [smallest index on the list]
        high ([int]): [biggets index on the list]

    Returns:
        [boolean]: [True if we find it, False if we do not find it]
        [recursion]: [If the number is higher than the target then we need to call 
                       the function again but with the middle-1 as the new low value
                      If the number is lower than the target then we need to call 
                        the function but  with the middle+1 as the new high value]
    """
    if low > high:
        return False

    mid = (low + high) // 2

    if numbers[mid] == Target:
        return True
    elif numbers[mid] > Target:
        return binary_search(numbers, Target, low, mid - 1)
    else:
        return binary_search(numbers, Target, mid + 1, high)



if __name__ == '__main__':
    numbers = [100, 24, 44, 5, 61, 9, 100, 11, 25, 270, 28, 1, 36, 49, 11,4,66,21,70,56,7,2,45,90,28,29]
    numbers.sort()
   
    print(numbers)

    Target = int(input('Enter a number: '))

    result = binary_search(numbers, Target, 0, len(numbers) - 1)

    if result is True:
        print('The number is on the list.')
    else:
        print('The number IS NOT on the list.')