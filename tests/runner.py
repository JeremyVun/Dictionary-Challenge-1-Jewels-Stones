from timeit import Timer
from statistics import mean
from .tests import build_tests

# Run a single test
def run_test(f, test):
  jewels = test.data["jewels"]
  stones = test.data["stones"]
  
  actual = f(jewels, stones)
  expected = test.answer

  if (actual != expected):
    raise Exception(f" expected={expected}, actual={actual}")
  

# Run all the tests
def run_tests(f, runs=1000):
  testNum = 0
  test_times = []

  try:
    for test in build_tests():
      testNum += 1
      print(f"[RUNNING] Test {testNum}...", end="\r")

      timer = Timer(lambda: run_test(f, test))
      ms = timer.timeit(runs) * 1000 / runs
      
      test_times.append(ms)
      print(f"[PASS] Test {testNum}: {ms:.5f}ms")

    print(f"Average time: {mean(test_times):.5f}ms")

  except Exception as e:
    print(f"[FAIL] Test {testNum}: {e}")