class colors:
    green = '\033[92m'
    fail = '\033[91m'
    endc = '\033[0m'
    bold = '\033[1m'

def check_partition(array, lower, upper, pivot):
    for element in array[:lower]:
        if element >= pivot:
            print(f"{colors.fail}Partition unsuccessful.{colors.endc}")
            return
    for element in array[lower:upper]:
        if element != pivot:
            print(f"{colors.fail}Partition unsuccessful.{colors.endc}")
            return
    for element in array[upper:]:
        if element < pivot:
            print(f"{colors.fail}Partition unsuccessful.{colors.endc}")
            return

    print(f"{colors.okgreen}Partition successful.{colors.endc}")

def check_sort(array):
    for current, following in zip(array[:-1], array[1:]):
        if current > following:
            print(f"{colors.fail}Sort {colors.bold}unsuccessful{colors.endc}.{colors.endc}")
            return

    print(f"{colors.green}Sort {colors.bold}successful{colors.endc}.{colors.endc}")
