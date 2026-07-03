# При сортировке выбором:
# ПО ВОЗРАСТАНИЮ => искать НАИМЕНЬШИЙ
def findSmallest(arr):
  # Stores the smallest value
  smallest = arr[0]
  # Stores the index of the smallest value
  smallest_index = 0
  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest_index = i
      smallest = arr[i]      
  return smallest_index

# ПО УБЫВАНИЮ => искать НАИБОЛЬШИЙ
def findLargest(arr):
  largest = arr[0]
  largest_idx = 0
  for i in range (1, len(arr)):
    if arr[i] > largest:
      largest_idx = i
      largest = arr[i]
  return largest_idx

# Sort array
def selectionSort(arr):
  newArr = []
  for i in range(len(arr)):
      # Finds the smallest element in the array and adds it to the new array
      smallest = findSmallest(arr)
      newArr.append(arr.pop(smallest))    # pop - удаляет эл-т по позиции + возвращает его
  return newArr

print(selectionSort([5, 3, 6, 2, 10]))

# === КЛАССИЧЕСКИЙ (ЦЕЛЫЙ) алг. СОРТИРОВКИ ВЫБОРОМ ===
def selection_sort(arr):
  n = len(arr)    # Получить длину массива
  # Внешний цикл (по всем эл-там): сдвигаем границу i
  for i in range(n):
    min_idx = i   # Считать текущий эл-т по индексу i "минимумом"
    # Внутренний цикл (по всем эл-там ПРАВЕЕ границы): выбор НАИМЕНЬШЕГО/НАИБОЛЬШЕГО...
    for j in range (i + 1, n):
      # ...поиск НАИМЕНЬШЕГО (для примера)
      if arr[j] < arr[min_idx]:   # Если найден эл-т меньше "минимума"
        min_idx = j     # Запомнить его индекс
    # После проверки всей правой части: поменять местами эл-т на [i] и найденный "минимум" [min_idx]
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
  # Вернуть отсортированный список
  return arr

print("===== Упражнения =====")
print(selection_sort([5, 3, 6, 2, 10]))
print(selection_sort([1, 2, 3, 4, 5]))
print(selection_sort([5, 4, 3, 2, 1]))
