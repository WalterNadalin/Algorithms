def insertion_sort(array, begin, end):
    n = len(array)

    for i in range(begin, end + 1):
        k = i

        while k > begin and array[k] < array[k - 1]:
            array[k], array[k - 1] = array[k - 1], array[k]
            k -= 1
