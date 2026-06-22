#Arrays vs Python Lists (Memory & Performance Benchmark)
my_list = [42, 'hello', 3.14, True, [1,2,3]]

import sys
numbers = [1, 2, 3, 4, 5]
print(sys.getsizeof(numbers))

import numpy as np
np_arr = np.array([1, 2, 3, 4, 5], dtype=np.int32)
print(np_arr.nbytes)

import time

SIZE = 1_000_000

py_list = list(range(SIZE))
start = time.time()
result = [x * 2 for x in py_list]
print(f'Python list: {time.time() - start:.4f}s')

np_arr = np.arange(SIZE)
start = time.time()
result = np_arr * 2
print(f'NumPy array: {time.time() - start:.4f}s')