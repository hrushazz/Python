my_dict = {'a': 3, 'b': 1, 'c': 2}

# Сортировка по значению в порядке возрастания
sorted_dict_ascending = dict(sorted(my_dict.items(), key=lambda item: item[1]))

print(sorted_dict_ascending)



my_dict = {'a': 3, 'b': 1, 'c': 2}

# Сортировка по значению в порядке убывания
sorted_dict_descending = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

print(sorted_dict_descending)