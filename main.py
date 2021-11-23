"""
Dictionary Challenge 1 - Jewels and Stones

Description:
You're given a string "jewels" representing the types of stones that are jewels, and a string "stones" representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Example:
Input:
  jewels = "aA"
  stones = "aAAbbbb"
Correct Output:
  3
"""

from solutions import slow, fast
from tests import build_tests
from graph import plot_graph


# Entry point
def main():
  slow_times = []
  fast_times = []
  
  # n = 4 (size of our arrays)
  # jewels = [a, b, c, d]
  # stones = [a, a, e, e]
  tests = build_tests(n=5000)

  # Benchmark slow and fast solution
  for test in tests:
    print(f"Benchmarking n={len(test.data['jewels'])}")
    # O(n^2)
    slow_times.append(measure(slow, test))

    # O(n)
    fast_times.append(measure(fast, test))

  # graph the time complexity of our solutions
  plot_graph(slow_times)
  plot_graph(fast_times)
  print(f"[Max Times] fast: {max(fast_times):.2f}ms, slow: {max(slow_times):.2f}ms")



######
######
# Measure the performance of our solution against a test
from timeit import Timer
from statistics import mean
from concurrent.futures import ThreadPoolExecutor, as_completed
def measure(f, test, runs=50):
  futures = []
  with ThreadPoolExecutor(max_workers=runs) as executor:
    futures.append(executor.submit(measure_task, f, test))

  times = []
  for future in as_completed(futures):
    times.append(future.result())

  return mean(times)

def measure_task(f, test):
  data = test.data
  timer = Timer(lambda: f(data["jewels"], data["stones"]))
  return timer.timeit(1) * 1000



if __name__ == "__main__":
  main()