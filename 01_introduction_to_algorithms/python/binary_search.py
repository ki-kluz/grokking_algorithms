class BinarySearch():

  def search_iterative(self, list, item):
    # Границы части списка, в которой выполняется поиск
    low = 0                 # Начальная граница
    high = len(list) - 1    # Конечная (длина - 1)

    # Пока исследуемая часть списка не сократится до одного элемента...
    while low <= high:
      # ...проверяем средний элемент (с округлением в меньшую сторону <=> взятием целой части)
      mid = (low + high) // 2
      guess = list[mid]
      # Совпадение
      if guess == item:
        return mid
      # Предполагаемое больше искомого => сдвигаем поиск в левую часть
      if guess > item:
        high = mid - 1
      # Предполагаемое меньше искомого => сдвигаем поиск в правую часть
      else:
        low = mid + 1

    return None

  def search_recursive(self, list, low, high, item):
    # Check base case 
    if high >= low: 
  
        mid = (high + low) // 2
        guess = list[mid]
  
        # If element is present at the middle itself 
        if guess == item:
            return mid 
  
        # If element is smaller than mid, then it can only 
        # be present in left subarray 
        elif guess > item: 
            return self.search_recursive(list, low, mid - 1, item) 
  
        # Else the element can only be present in right subarray 
        else: 
            return self.search_recursive(list, mid + 1, high, item) 
  
    else: 
        # Element is not present in the array 
        return None

if __name__ == "__main__":
  # We must initialize the class to use the methods of this class
  bs = BinarySearch()
  my_list = [1, 3, 5, 7, 9]
  print(bs.search_iterative(my_list, 3)) # => 1
  # 'None' means nil in Python. We use to indicate that the item wasn't found.
  print(bs.search_iterative(my_list, -1)) # => None

  print("===== Упражнения 1.1 1.2 =====")
  # Список из 8 НЕОТСОРТИРОВАННЫХ имён
  names_8_unsorted = ["Алексей", "Елена", "Иван", "Ольга", "Дмитрий", "Анна", "Сергей", "Мария"]
  # Список из 8 ОТСОРТИРОВАННЫХ имён
  names_8_sorted = ["Алексей", "Анна", "Дмитрий", "Елена", "Иван", "Мария", "Ольга", "Сергей"]
  print(bs.search_iterative(names_8_unsorted, "Анна"))    # => None
  print(bs.search_iterative(names_8_sorted, "Анна"))      # => 1

  # Список из 16 НЕОТСОРТИРОВАННЫХ имён (увеличиваем в два раза)
  names_16_unsorted = [
      "Александр", "Татьяна", "Михаил", "Наталья", "Андрей", "Ирина", "Николай", "Евгения",
      "Владимир", "Светлана", "Антон", "Екатерина", "Денис", "Юлия", "Роман", "Дарья"
  ]
  # Список из 16 ОТСОРТИРОВАННЫХ имён
  names_16_sorted = [
      "Александр", "Андрей", "Антон", "Владимир", "Дарья", "Денис", "Евгения", "Екатерина", 
      "Ирина", "Михаил", "Наталья", "Николай", "Роман", "Светлана", "Татьяна", "Юлия"
  ]
  print(bs.search_iterative(names_16_unsorted, "Антон"))    # => None
  print(bs.search_iterative(names_16_sorted, "Антон"))      # => 2