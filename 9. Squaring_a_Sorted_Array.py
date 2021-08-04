def make_squares(arr):
  #squares = [i**2 for i in arr]
  #return sorted(squares)
  # TODO: Write your code here
  left = 0
  right = len(arr) - 1

  squares = []

  while(left<=right):
    number_one = arr[left] ** 2
    number_two = arr[right] ** 2

    if(number_one > number_two):
      squares.insert(0, number_one)
      left+=1

    else:
      squares.insert(0, number_two)
      right-=1
  return squares