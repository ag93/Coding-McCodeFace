def pair_with_targetsum(arr, target_sum):
  # TODO: Write your code here
 
 start = 0
 end = len(arr) - 1

 while(start < end):
  if(arr[start] + arr[end] == target_sum):
     return [start, end]
  elif(arr[start] + arr[end] < target_sum):
    start += 1
  else:
    end -= 1