def pair_with_targetsum(arr, target_sum):
  # TODO: Write your code here
  for i in range (len(arr)):
    if target_sum - arr[i] in arr:
      return([i, arr.index(target_sum - arr[i])])
  return [-1, -1]