import math
def smallest_subarray_with_given_sum(s, arr):
  
  currentSum = 0
  currentStart = 0
  minLength = math.inf

  for i in range(len(arr)):
    currentSum += arr[i]

    while currentSum >= s:
      minLength = min(minLength, len(arr[currentStart : i])+1)
      currentSum -= arr[currentStart]
      currentStart += 1

  if minLength == math.inf:
    return 0
  return minLength
