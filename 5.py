# Создаем словарь с описанием продукции
menu = {
    'торт': ['Изысканный торт с разнообразными начинками', 500, 10],
    'пирожное': ['Нежное пирожное с шоколадной глазурью', 150, 20],
    'маффин': ['Ароматный маффин с ягодами', 200, 15],
    'печенье': ['Вкусное овсяное печенье', 100, 30],
    'эклер': ['Нежный эклер с заварным кремом', 180, 12],
    'пончик': ['Пышный пончик с сахарной посыпкой', 250, 8]
}
# Функция для просмотра описания продукции
def view_description(product):
    if product in menu:
        print(f"{product}: {menu[product][0]}")
    else:
        print("Такого продукта нет в меню.")


# Функция для просмотра цены продукции
def view_price(product):
    if product in menu:
        print(f"{product}: {menu[product][1]} рублей за 100 грамм")
    else:
        print("Такого продукта нет в меню.")


# Функция для просмотра количества продукции
def view_quantity(product):
    if product in menu:
        print(f"{product}: {menu[product][2]} грамм в наличии")
    else:
        print("Такого продукта нет в меню.")


# Функция для вывода всей информации о продукции
def view_all_info():
    for product, info in menu.items():
        print(f"{product}: {info[0]}, Цена: {info[1]} рублей за 100 грамм, Количество: {info[2]} грамм")


# Функция для совершения покупки
def buy_product(product, quantity):
    if product in menu and quantity > 0:
        if quantity <= menu[product][2]:
            cost = (menu[product][1] * quantity) / 100
            menu[product][2] -= quantity
            print(f"Вы купили {quantity} грамм(а) {product} за {cost} рублей.")
        else:
            print(f"Извините, недостаточно {product} в наличии.")
    else:
        print("Такого продукта нет в меню или введено некорректное количество.")


# Основной цикл программы
while True:
    print("\nМеню:")
    print("1. Просмотр описания продукции")
    print("2. Просмотр цены продукции")
    print("3. Просмотр количества продукции")
    print("4. Вся информация о продукции")
    print("5. Покупка продукции")
    print("6. Выход")

    choice = input("Выберите пункт меню: ")

    if choice == '1':
        product = input("Введите название продукции: ")
        view_description(product)
    elif choice == '2':
        product = input("Введите название продукции: ")
        view_price(product)
    elif choice == '3':
        product = input("Введите название продукции: ")
        view_quantity(product)
    elif choice == '4':
        view_all_info()
    elif choice == '5':
        product = input("Введите название продукции: ")
        quantity = int(input("Введите количество (в граммах): "))
        buy_product(product, quantity)
    elif choice == '6':
        print("До свидания!")
        break
    else:
        print("Некорректный выбор. Пожалуйста, выберите существующий пункт меню.")