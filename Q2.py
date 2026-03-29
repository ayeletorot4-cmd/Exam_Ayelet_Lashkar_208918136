import statistics
def find_median(numbers: list) -> float:
    """

    :param numbers: unsorted list f numbers
    :return: median
    """
    sorted_numbers = sorted(numbers)
    print(sorted_numbers)
    if len(sorted_numbers) % 2 == 1:
        return float(sorted_numbers[len(sorted_numbers) // 2])
    else:

        return float(statistics.mean([sorted_numbers[len(sorted_numbers) // 2 ] , sorted_numbers[len(sorted_numbers) // 2 -1]]))
print(find_median([3,1,4,1,5]))
print(find_median([7,2,10,9]))
print(find_median([42]))