def quick_sort(array, begin, end):
    while begin < end:
        lower, upper = partition(array, begin, end, end)
        quick_sort(array, begin, lower - 1)
        begin = upper + 1

def partition(array, lower, upper, pivot):
    auxiliary, value = lower, array[pivot]

    for _ in range(upper - lower + 1):
        if array[auxiliary] < value:
            array[lower], array[auxiliary] = array[auxiliary], array[lower]
            lower += 1
            auxiliary += 1
        elif array[auxiliary] > value:
            array[auxiliary], array[upper] = array[upper], array[auxiliary]
            upper -= 1
        else:
            auxiliary += 1

    return lower, upper
