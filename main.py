import sqlite3

conn = sqlite3.connect('products.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Products (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price REAL, quantity INTEGER)''')
conn.commit()


def add_product():
    name = input("Введіть назву товару: ")
    price = float(input("Введіть ціну товару: "))
    quantity = int(input("Введіть кількість товару: "))

    cursor.execute("INSERT INTO Products (name, price, quantity) VALUES (?, ?, ?)", (name, price, quantity))
    conn.commit()
    print("Товар успішно додано!")


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
            print("Товар '{}' успішно видалено!".format(product_name))
        else:
            print("Видалення товару скасовано.")


def edit_product():
    product_id = int(input("Введіть ідентифікатор товару, який потрібно редагувати: "))
    new_price = float(input("Введіть нову ціну товару: "))
    new_quantity = int(input("Введіть нову кількість товару: "))

    cursor.execute("UPDATE Products SET price=?, quantity=? WHERE id=?", (new_price, new_quantity, product_id))
    conn.commit()
    print("Інформацію про товар успішно оновлено!")


def view_products():
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()

    if len(products) == 0:
        print("Немає жодного товару у базі даних.")
    else:
        for product in products:
            print("Id:{}, Назва:{}, ціна{}, кількість{}".format(product[0], product[1], product[2], product[3] ))


while True:
    print("\nМеню:")
    print("1. Добавити товар")
    print("2. Видалити товар")
    print("3. Редагувати товар")
    print("4. Переглянути список товарів")
    print("5. Вийти")

    choice = input("Виберіть дію: ")

    if choice == "1":
        add_product()
    elif choice == "2":
        delete_product()
    elif choice == "3":
        edit_product()
    elif choice == "4":
        view_products()
    elif choice == "5":
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")

conn.close()