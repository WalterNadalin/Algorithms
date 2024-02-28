def selection_sort(array, begin, end):
    for upper in range(end, -1, -1):
        maximum, index = array[begin], begin

        for lower in range(begin + 1, upper + 1):
            if array[lower] > maximum:
                maximum, index  = array[lower], lower

        array[index], array[upper] = array[upper], array[index]
