def find_averages_of_subarrays(K, arr):
  result = []

  #Educative Code
  '''for i in range(len(arr)-K+1):
   find sum of next 'K' elements
   _sum = 0.0
   for j in range(i, i+K):
    _sum += arr[j]
  result.append(_sum/K)'''  # calculate average
  
  for i in range(len(arr) - K + 1):
    total = 0.0
    total = sum(arr[i:i+K])
    result.append(total/K)

  return result


def main():
  result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
  print("Averages of subarrays of size K: " + str(result))


main()