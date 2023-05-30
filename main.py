import sqlite3

conn = sqlite3.connect('products.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Products (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price REAL, quantity INTEGER)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)''')
conn.commit()

current_user = None

def add_product():
    product_name = input("Введіть назву товару: ")
    price = float(input("Введіть ціну товару: "))
    quantity = int(input("Введіть кількість товару: "))

    cursor.execute("INSERT INTO Products (name, price, quantity) VALUES (?, ?, ?)", (product_name, price, quantity))
    conn.commit()
    print("Товар {} успішно додано! (Користувач: {})".format(product_name, current_user))


def delete_product():
    product_id = int(input("Введіть ідентифікатор товару, який потрібно видалити: "))

    cursor.execute("SELECT name FROM Products WHERE id=?", (product_id,))
    product_name = cursor.fetchone()

    if product_name is None:
        print("Товар з введеним ідентифікатором не знайдено.")
    else:
        product_name = product_name[0]
        print("Ви збираєтесь видалити:{}".format(product_name))
        confirm = input("Ви впевнені, що хочете видалити цей товар? (Так/Ні): ")

        if confirm.lower() == "так":
            cursor.execute("DELETE FROM Products WHERE id=?", (product_id,))
            conn.commit()
            print("Товар {} успішно видалено! (Користувач: {})".format(product_name, current_user))
        else:
            print("Видалення товару скасовано.")


def edit_product():
    product_id = int(input("Введіть ідентифікатор товару, який потрібно редагувати: "))

    cursor.execute("SELECT * FROM Products WHERE id=?", (product_id,))
    products = cursor.fetchall()
    if len(products) == 0:
        print("Немає такого товару у базі даних.")
        raise
    else:
        for product in products:
            old_product_name = product[1]
            old_price = product[2]
            old_quantity = product[3]

    new_product_name = input("Введіть нову назву товару: ")
    new_price = float(input("Введіть нову ціну товару: "))
    new_quantity = int(input("Введіть нову кількість товару: "))

    cursor.execute("UPDATE Products SET name=?, price=?, quantity=? WHERE id=?", (new_product_name, new_price, new_quantity, product_id))
    conn.commit()
    print("Інформацію про {} товар успішно оновлено! Назву {} змінено на {}, ціну {} на {}, кількість {} на {} (Користувач: {})".format(old_product_name, new_product_name, old_price, new_price, old_quantity, new_quantity, current_user))


def view_products():
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()

    if len(products) == 0:
        print("Немає такого товару у базі даних.")
    else:
        for product in products:
            print("Id:{}, Назва:{}, ціна:{}, кількість:{}".format(product[0], product[1], product[2], product[3]))


def register():
    username = input("Введіть ім'я користувача: ")
    password = input("Введіть пароль: ")

    cursor.execute("SELECT username FROM Users WHERE username=?", (username,))
    existing_user = cursor.fetchone()

    if existing_user is not None:
        print("Користувач з введеним ім'ям вже існує.")
    else:
        cursor.execute("INSERT INTO Users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        print("Користувач {} успішно зареєстрований.".format(username))
        global current_user
        current_user = username
        choose_role()


def login():
    username = input("Введіть ім'я користувача: ")
    password = input("Введіть пароль: ")

    cursor.execute("SELECT username, password FROM Users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()

    if user is None:
        print("Неправильне ім'я користувача або пароль.")
    else:
        global current_user
        current_user = username
        print("Користувач {} успішно увійшов.".format(username))
        choose_role()


def choose_role():
    print("Виберіть роль:")
    print("1. Клієнт")
    print("2. Продавець")

    role_choice = input("Виберіть роль: ")

    if role_choice == "1":
        display_catalog()
    elif role_choice == "2":
        if current_user is None:
            print("Будь ласка, увійдіть або зареєструйтесь.")
        else:
            while True:
                print("\nМеню продавця:")
                print("1. Редагувати товар")
                print("2. Переглянути список товарів")
                print("3. Видалити товар")
                print("4. Додати товар")
                print("5. Вийти")

                seller_choice = input("Виберіть дію: ")

                if seller_choice == "1":
                    edit_product()
                elif seller_choice == "2":
                    view_products()
                elif seller_choice == "3":
                    delete_product()
                elif seller_choice == "4":
                    add_product()
                elif seller_choice == "5":
                    break
                else:
                    print("Невірний вибір. Спробуйте ще раз.")
    else:
        print("Невірний вибір. Спробуйте ще раз.")

def display_catalog():
    if current_user is None:
        print("Будь ласка, увійдіть або зареєструйтесь.")
    else:
        cursor.execute("SELECT * FROM Products")
        products = cursor.fetchall()

        if len(products) == 0:
            print("Каталог товарів порожній.")
        else:
            print("Каталог товарів:")
            for product in products:
                print("Id:{}, Назва:{}, ціна:{}, кількість:{}".format(product[0], product[1], product[2], product[3]))


while True:
    print("\nМеню:")
    print("1. Реєстрація")
    print("2. Вхід")
    print("3. Вийти")

    choice = input("Виберіть дію: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")

conn.close()
