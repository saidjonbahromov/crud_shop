import categories, products_api, cart

while True:
    print('Добро пожаловать на наш магазин.')
    categories_ = categories.get_all_categories()
    print(f'Наши категории: {" | ".join(categories_)}')
    print('#####################################')
    print("Выберите действие:")
    print("1. Получить продукты выбранной категории.")
    print("2. Получить список всех товаров.")
    print("3. Получить список всех корзин.")
    print("4. Выход")
        
    choise = int(input('Выберите действие: '))

    if choise == 1:
        categorie_name = input('Введите котегория: ')
        products = categories.get_products_of_categorie(categorie_name)
        for product in products:
            print(f'{product["id"]}. {product["title"]} Price {product["price"]}')
    elif choise == 2:
        products = products_api.get_all_products()
        for product in products:
            print(f'{product["id"]}. {product["title"]} Price {product["price"]}')
    elif choise == 3:
        carts = cart.get_all_cart()
        for cart in carts:
            print(f'{cart["id"]}. UserId: {cart["userId"]}. Date: {cart["date"]}')
    elif choise == 4:
        break

    print('---------------------------------------')
    print('---------------------------------------')
    print('---------------------------------------')
