def counting_sort(array, begin, end):
    maximum, index = array[begin], begin

    for index in range(begin + 1, end + 1):
        if array[index] > maximum:
            maximum, index  = array[index], index

    counting = [0 for _ in range(maximum)]

    for index in array:
        counting[index - 1] += 1

    for index in range(1, maximum):
        counting[index] += counting[index - 1]

    sorted_array = [0 for _ in range(end + 1)]

    for index in reversed(array):
        sorted_array[counting[index - 1] - 1] = index
        counting[index - 1] -= 1

    array.clear()
    array += sorted_array
