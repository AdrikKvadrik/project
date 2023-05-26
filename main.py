import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (username TEXT PRIMARY KEY, password TEXT)''')

def register():
    username = input("Введіть своє ім'я: ")

    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    existing_user = cursor.fetchone()
    if existing_user:
        print("Користувач з таким ім'ям вже існує. Спробуйте інше ім'я.")
        return

    while True:
        password = input("Ваш пароль: ")
        confirm_password = input("Підтвердіть ваш пароль: ")
        if password == confirm_password:
            cursor.execute("INSERT INTO users VALUES (?, ?)", (username, password))
            conn.commit()
            print("Ви успішно зареєструвалися!")
            return username, password
        else:
            print("Пароль неправильний. Повторіть спробу.")

def login():
    username = input("Введіть своє ім'я: ")
    password = input("Введіть ваш пароль: ")
    cursor.execute("SELECT password FROM users WHERE username=?", (username,))
    result = cursor.fetchone()
    if result and result[0] == password:
        print("Все добре! Ви увійшли в обліковий запис.")
        change_password = input("Бажаєте змінити пароль? (Так/Ні): ")
        if change_password.lower() == "так":
            old_password = input("Введіть ваш поточний пароль: ")
            if old_password == password:
                new_password = input("Введіть новий пароль: ")
                cursor.execute("UPDATE users SET password=? WHERE username=?", (new_password, username))
                conn.commit()
                print("Пароль успішно змінено.")
            else:
                print("Неправильний поточний пароль.")
    else:
        print("Неправильне ім'я користувача або пароль.")

while True:
    print("1. Зареєструватися")
    print("2. Увійти")
    print("3. Вийти")
    choice = input("Виберіть пункт: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        break
    else:
        print("Неправильний вибір!")

conn.close()
