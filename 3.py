#Функция для подсчета суммы цифр в числе
def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

# Функция для подсчета гласных и согласных в слове
def count_vowels_and_consonants(word):
    vowels = 0
    consonants = 0
    vowel_characters = 'aeiouAEIOU'
    for char in word:
        if char.isalpha():
            if char.lower() in vowel_characters:
                vowels += 1
            else:
                consonants += 1
    return vowels, consonants

my_list = [1612, 49, 'hello', 6, 19, 'world']

# Обходим список и выполняем необходимые действия
for i in range(len(my_list)):
    if isinstance(my_list[i], int):  # Проверяем, является ли элемент числом
        if my_list[i] % 2 == 0:  # Если число четное
            my_list[i] = sum_of_digits(my_list[i])
        else:  # Если число нечетное
            my_list[i] = sum_of_digits(my_list[i])
    elif isinstance(my_list[i], str):  # Проверяем, является ли элемент строкой
        counts = count_vowels_and_consonants(my_list[i])
        my_list[i] = f"'{my_list[i]}' - Гласных: {counts[0]}, Согласных: {counts[1]}"

# Выводим результаты на экран
for item in my_list:
    print(item)

