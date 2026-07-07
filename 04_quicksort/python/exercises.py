# Функция sum (через рекурсию)
def sum(arr):
	if not arr:
		return 0
	else:
		return arr[0] + sum(arr[1:])

# print(sum([1, 2, 11, 13]))

# Функция count (через рекурсию)
def count(arr):
	if not arr:
		return 0
	else:
		return 1 + count(arr[1:])
	
# print(count([1, 2, 3]))

# Функция поиска НАИБОЛЬШЕГО числа (через рекурсию)
def max(arr):
	if not arr:
		return None
	elif len(arr) == 1:
		return arr[0]
	else:
		rest_max = max(arr[1:])
		return arr[0] if arr[0] > rest_max else rest_max

"""
ИЛИ... (вариант из книги)
def max(arr):
	if len(arr) == 2:
		return arr[0] if arr[0] > arr[1] else arr[1]
	else:
		rest_max = max(arr[1:])
		return arr[0] if arr[0] > rest_max else rest_max
"""
# print(max([1, 2, 3, -1, 0, 1]))