def countdown(i):
  print(i)
  # base case
  if i <= 0:
    return 0
  # recursive case
  else:
    return countdown(i-1)

countdown(5)