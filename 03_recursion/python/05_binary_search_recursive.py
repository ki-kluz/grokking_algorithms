def binary_search(arr, target):
    if len(arr) == 0:
        return None

    mid = len(arr) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr[:mid], target)
    else:
        recursive_response = binary_search(arr[(mid + 1):], target)
        return (
            (mid + 1) + recursive_response
            if recursive_response is not None
            else recursive_response
        )

print(binary_search([6, 7, 8, 9, 10], 8))
print(binary_search([6, 7, 8, 9, 10], 6))
print(binary_search([6, 7, 8, 9, 10], 10))


# ИЛИ можно сразу передавать в ф-цию границы (указатели low и high)
def binary_search_idx(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low > high:
        return None
    
    mid = (low + high) // 2

    if arr[mid] == target:
        return mid      # Индекс найден => возвращаем его
    elif arr[mid] > target:
        return binary_search_idx(arr, target, low, mid - 1)     # Ищем в левой части
    else:
        return binary_search_idx(arr, target, mid + 1, high)    # Ищем в правой части
    
print(binary_search_idx([6, 7, 8, 9, 10], 8))
print(binary_search_idx([6, 7, 8, 9, 10], 6))
print(binary_search_idx([6, 7, 8, 9, 10], 10))