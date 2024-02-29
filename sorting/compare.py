from numpy.random import randint
from copy import copy
from time import time
from math import log2
from matplotlib.pyplot import legend, show, xlabel, ylabel, loglog, title, style
from algorithms import check_sort, quick_sort, bubble_sort, insertion_sort, selection_sort, counting_sort
from data_structures import heap

style.use('dark_background')

def heap_sort(array, begin, end):
	heap_array = heap(*array[begin:end + 1], max_heap = True)

	for i in range(end, begin + 1, -1):
		array[i] = heap_array.pop_minimum()

	array[begin], array[begin + 1] = heap_array.array[begin + 1], heap_array.array[begin]
	
def binary_search(array, value):
    lower, upper = 0, len(array) - 1
    i = 0
    while lower <= upper:
        mid = (upper + lower) // 2

        if array[mid] == value:
            return mid
        elif array[mid] > value:
            upper = mid - 1
        else:
            lower = mid + 1

        i += 1
    print(i)

    return None

def complexity(func, args, nmax = 8):
    times = []
    sizes = [2 ** x for x in range(1, nmax)]

    for n in sizes:
        start = time()
        func(args(n), 0, n - 1)
        end = time()

        times += [end - start]

    return sizes, times

def check(algorithm, array):
	array = copy(array)
	algorithm(array, 0, n - 1)
	check_sort(array)
	print(f'{array}\n')

if __name__ == "__main__":
	n = 1 + randint(23, size = 1)[0]
	example = randint(100, size = n).tolist()
	print(f'Array considered: {example}\n')

	print('Insertion sort:')
	check(insertion_sort, example)

	print('Quick sort:')
	check(quick_sort, example)

	print('Bubble sort:')
	check(bubble_sort, example)

	print('Selection sort:')
	check(selection_sort, example)

	print('Heap sort:')
	check(heap_sort, example)

	print('Counting sort:')
	check(counting_sort, example)

	args = lambda n : randint(100, size = n).tolist()
	size = 13
	x = [2 ** x for x in range(1, size)] 
	square = [y ** 2 * 5e-8 for y in x]
	log = [y * log2(y) * 1e-7 for y in x]
	y = [y * 1e-7 for y in x]


	loglog(x, y, 'c--', label = '$n$')
	loglog(x, square, 'y--', label = '$n^2$')
	loglog(x, log, 'w--', label = '$n\log_2(n)$')
	loglog(*complexity(insertion_sort, args, size), ':.', label = 'Insertion sort') 
	loglog(*complexity(quick_sort, args, size), ':.', label = 'Quick sort') 
	loglog(*complexity(bubble_sort, args, size), ':.', label = 'Bubble sort') 
	loglog(*complexity(selection_sort, args, size), ':.', label = 'Selection sort') 
	loglog(*complexity(heap_sort, args, size), ':.', label = 'Heap sort') 
	loglog(*complexity(counting_sort, args, size), ':.', label = 'Counting sort') 

	title('Time required with respect to the size of the input')
	xlabel('$n$')
	ylabel('$t$')
	legend()
	show()
