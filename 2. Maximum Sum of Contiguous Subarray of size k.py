def max_sub_array_of_size_k(k, arr):
  # TODO: Write your code here
  sums = []
  currentSum = 0.0
  currentStart = 0
  for end in range(len(arr)):
    currentSum += arr[end]

    if(end >= k-1):
      sums.append(currentSum)
      currentSum -= arr[currentStart]
      currentStart += 1

  return max(sums)