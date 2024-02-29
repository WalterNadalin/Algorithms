# Set the `__all__` variable, which defines `import *`
__all__ = ['test', 'quick_sort', 'bubble_sort', 'selection_sort', 'insertion_sort',  'counting_sort']

# Uncomment the following to `import` the package
from .quick_sort import quick_sort
from .bubble_sort import bubble_sort
from .selection_sort import selection_sort
from .insertion_sort import insertion_sort
from .counting_sort import counting_sort
from .test import check_sort
