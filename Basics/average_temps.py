def average_temps(temps):
    """[Calculate average of n numbers of temperatures]

    Args:
        temps ([list]): [Meditions of temperatures defined by the developer]

    Returns:
        [average]: [Sum of all the temps divided by the number of meditions]
    """
    sum_of_temps = 0

    for temp in temps:
        sum_of_temps += float(temp)

    #sum_temps = sum(temps) #An easier way to implement the sum of n elements
                            #In a list is with the sum function

    return sum_temps / len(temps)


if __name__ == '__main__':
    temps = [21, 24, 24, 22, 20, 23, 24]

    average = average_temps(temps)

    print('La temperatura promedio es: {}'.format(average))