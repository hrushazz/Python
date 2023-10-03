# Исходный кортеж
my_tuple = (5, 2, 9, 1, 7)

# Сортировка кортежа в порядке убывания
sorted_tuple = tuple(sorted(my_tuple, reverse=True))

# Вывод первого и последнего элементов кортежа
first_element = sorted_tuple[0]
last_element = sorted_tuple[-1]

print("Сортированный кортеж:", sorted_tuple)
print("Первый элемент:", first_element)
print("Последний элемент:", last_element)
