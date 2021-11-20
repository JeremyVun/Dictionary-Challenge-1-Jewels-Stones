import json

# Build the test cases
def build_tests():
  result = []

  tests = read_tests()
  for test in tests:
    result.append(build_test(test))

  return result

def build_test(test):
  return Test(test["data"], test["answer"])

# Read the tests from file
def read_tests():
  with open('tests/tests.json', 'r') as f:
    result = json.load(f)
    return result["tests"]


# Class to hold our test data
class Test:
  def __init__(self, data, answer):
    self.data = data
    self.answer = answer