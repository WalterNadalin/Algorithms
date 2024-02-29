def heap_sort(array, begin, end):
    heap_array = data_structures.heap(*array, max_heap = True)

    for i in range(end, begin + 1, - 1):
        array[i] = heap_array.pop_minimum()

    array[0], array[1] = heap_array[1], heap_array[0]
