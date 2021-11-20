# O(n^2)
def slow(jewels, stones):
  result = 0

  for s in stones:
    for j in jewels:
      if s == j:
        result += 1
        break

  return result

# O(n)
def fast(jewels, stones):
  dictionary = {}
  for j in jewels:
    dictionary[j] = True

  result = 0
  for s in stones:
    if s in dictionary:
      result += 1

  return result
