def sum():
    while True:

        input_str = input("Введите число (или 'exit' для завершения): ")
        if input_str.lower() == 'exit':
            print("Завершение программы.")
            break
        if input_str.isdigit():
            number = int(input_str)
            even_count = 0
            odd_count = 0
            for digit in str(number):
                digit = int(digit)
                if digit % 2 != 0:
                    even_count += digit
            if even_count == 0:
                print("В числе нет нечетных цифр(")
            else:
                print(f"Cумма нечетных цифр: {even_count}")
        else:
            print("Это не число. Пожалуйста, введите число.")
sum()