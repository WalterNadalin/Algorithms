def bubble_sort(array, begin, end):
    for upper in range(end, -1, -1):
        for lower in range(begin, upper):
            if array[lower] > array[lower + 1]:
                array[lower], array[lower + 1] = array[lower + 1], array[lower]
