

def count_case_pairs_and_consonants():
    word = input("Введите слово: ")
    # Инициализируем счетчики пар верхнего и нижнего регистра
    upper_lower_pairs = 0
    lower_upper_pairs = 0
    # Инициализируем счетчик согласных букв
    consonant_count = 0

    # Проходим по каждой букве в слове
    for i in range(len(word) - 1):
        current_char = word[i]
        next_char = word[i + 1]

        # Проверяем, является ли текущая буква верхнего и следующая нижнего регистра, и наоборот
        if current_char.isupper() and next_char.islower():
            upper_lower_pairs += 1
        elif current_char.islower() and next_char.isupper():
            lower_upper_pairs += 1

        # Проверяем, является ли текущая буква согласной
        if current_char.isalpha() and current_char.lower() not in "aeiouаеиёояюэуы":
            consonant_count += 1

    print(f"Пар верхнего и нижнего регистра: {upper_lower_pairs + lower_upper_pairs}")
    print(f"Согласных букв: {consonant_count}")
    # Возвращаем результаты
    return upper_lower_pairs, lower_upper_pairs, consonant_count

# Вызываем функцию
count_case_pairs_and_consonants()
