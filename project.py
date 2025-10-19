from naive import count_smaller_naive
from divideandconquer import count_smaller

def test_correctness():
   tests = [
   [5, 2, 6, 1],
   [3, 4, 9, 6, 1],
   [1, 2, 3, 4],
   [4, 3, 2, 1],
   [2, 2, 2, 2]
   ]
   for arr in tests:
       print("Array:", arr)
       print("Naive:", count_smaller_naive(arr))
       print("Efficient:", count_smaller(arr))
       print("-" *30)

test_correctness()

import random, time

def measure_runtime():
    sizes = [500, 700, 1000, 1300, 1600, 2000]
    for n in sizes:
       arr = [random.randint(0, n) for _ in range(n)]
       start = time.time()
       count_smaller(arr)
       fast_time =time.time() -start

       if n <= 1500:
          start = time.time()
          count_smaller_naive(arr)
          slow_time =time.time() -start
       else:
          slow_time ="Too slow"
       print(f"n={n} | Efficient={fast_time:.4f}s | Naive={slow_time}")


measure_runtime()