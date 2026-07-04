def sum_array(arr):
    if not arr:     # Эквивалентно: len(arr) == 0
        return 0
    return arr[0] + sum_array(arr[1:])

print(sum_array([]))
print(sum_array([1, 2, 3, 2, 1]))