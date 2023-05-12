class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, age, salary, position, num_of_subordinates):
        super().__init__(name, age, salary, position)
        self.num_of_subordinates = num_of_subordinates

    def say_hello(self):
        print(f"Привіт, мене звати {self.name}. Мені {self.age} років. Я заробляю {self.position}. І я маю {self.num_of_subordinates} підлеглих.")

    def add_subordinates(self, subordinate):
        self.num_of_subordinates += subordinate
        print(f"У мене тепер {self.num_of_subordinates} підлеглих.")

    def remove_subordinates(self, subordinate):
        self.num_of_subordinates -= subordinate
        print(f"У мене тепер {self.num_of_subordinates} підлеглих.")


class Developer(Employee):
    def __init__(self, name, age, salary, position):
        super().__init__(name, age, salary, position)
        self.IT_languages = []

    def say_hello(self):
        print(f"Привіт, мене звати {self.name}. Мені {self.age} років. Я заробляю {self.position}. І я знаю наступні мови програмування: {', '.join(self.IT_languages)}.")

    def set_languages(self):
        num_of_languages = int(input("Скільки мов програмування ви знаєте? "))
        for i in range(num_of_languages):
            language = input(f"Введіть назву мови програмування #{i+1}: ")
            self.IT_languages.append(language)

manager = Manager("Adrian", 40, 80000, "Manager", 10)
developer = Developer("Mark", 25, 60000, "Developer")


manager.say_hello()
print("Додамо 5 підлеглих")
manager.add_subordinates(5)
print("Заберемо 7 підлеглих")
manager.remove_subordinates(7)

developer.set_languages()
developer.say_hello()

