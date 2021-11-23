from random import randint
from solutions import fast

# Build the test cases
def build_tests(n):
  result = []

  for i in range(1, n, int(n/10)):
    print(f"Building tests... n={i}", end="\r")
    jewels = [j for j in range(i)]
    stones = [randint(0, i-1) for _ in range(i)]
    answer = fast(jewels, stones)
    result.append(build_test(jewels, stones, answer))

  print("\rTests Built!            ")
  return result

def build_test(jewels, stones, answer):
  data = {
    "jewels": jewels,
    "stones": stones
  }
  return Test(data, answer)


# Class to hold our test data
class Test:
  def __init__(self, data, answer):
    self.data = data
    self.answer = answer