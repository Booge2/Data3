class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.capacity

    def enqueue(self, item):
        if self.is_full():
            print("Черга повна. Неможливо додати елемент.")
        else:
            self.items.append(item)
            print(f"Елемент '{item}' додано до черги.")

    def dequeue(self):
        if self.is_empty():
            print("Черга порожня. Неможливо видалити елемент.")
        else:
            item = self.items.pop(0)
            print(f"Елемент '{item}' видалено з черги.")

    def show(self):
        if self.is_empty():
            print("Черга порожня.")
        else:
            print("Елементи черги:")
            for item in self.items:
                print(item)


def main():
    capacity = int(input("Введіть максимальну ємність черги: "))
    queue = Queue(capacity)

    while True:
        print("\nМеню:")
        print("1. Перевірити, чи черга порожня")
        print("2. Перевірити, чи черга повна")
        print("3. Додати елемент до черги")
        print("4. Видалити елемент з черги")
        print("5. Показати елементи черги")
        print("0. Вихід")

        choice = input("Виберіть операцію: ")

        if choice == "1":
            if queue.is_empty():
                print("Черга порожня.")
            else:
                print("Черга не порожня.")
        elif choice == "2":
            if queue.is_full():
                print("Черга повна.")
            else:
                print("Черга не повна.")
        elif choice == "3":
            item = input("Введіть елемент для додавання: ")
            queue.enqueue(item)
        elif choice == "4":
            queue.dequeue()
        elif choice == "5":
            queue.show()
        elif choice == "0":
            print("Програма завершена.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()


# Завдання 2
class PriorityQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.capacity

    def insert_with_priority(self, item, priority):
        if self.is_full():
            print("Черга повна. Неможливо додати елемент з пріоритетом.")
        else:
            self.items.append((item, priority))
            self.items.sort(key=lambda x: x[1])
            print(f"Елемент '{item}' з пріоритетом {priority} додано до черги.")

    def pull_highest_priority_element(self):
        if self.is_empty():
            print("Черга порожня. Неможливо видалити елемент.")
        else:
            item, priority = self.items.pop(0)
            print(f"Елемент '{item}' з пріоритетом {priority} видалено з черги.")

    def peek(self):
        if self.is_empty():
            print("Черга порожня.")
        else:
            item, priority = self.items[0]
            print(f"Найвищий пріоритет: {priority}. Елемент: {item}")

    def show(self):
        if self.is_empty():
            print("Черга порожня.")
        else:
            print("Елементи черги:")
            for item, priority in self.items:
                print(f"Елемент: {item}, Пріоритет: {priority}")


def main():
    capacity = int(input("Введіть максимальну ємність черги: "))
    queue = PriorityQueue(capacity)

    while True:
        print("\nМеню:")
        print("1. Перевірити, чи черга порожня")
        print("2. Перевірити, чи черга повна")
        print("3. Додати елемент з пріоритетом до черги")
        print("4. Видалити елемент з найвищим пріоритетом з черги")
        print("5. Переглянути найвищий пріоритет елемента")
        print("6. Показати елементи черги")
        print("0. Вихід")

        choice = input("Виберіть операцію: ")

        if choice == "1":
            if queue.is_empty():
                print("Черга порожня.")
            else:
                print("Черга не порожня.")
        elif choice == "2":
            if queue.is_full():
                print("Черга повна.")
            else:
                print("Черга не повна.")
        elif choice == "3":
            item = input("Введіть елемент для додавання: ")
            priority = int(input("Введіть пріоритет елемента: "))
            queue.insert_with_priority(item, priority)
        elif choice == "4":
            queue.pull_highest_priority_element()
        elif choice == "5":
            queue.peek()
        elif choice == "6":
            queue.show()
        elif choice == "0":
            print("Програма завершена.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()


# Завдання 3
class UserDatabase:
    def __init__(self):
        self.users = {}

    def add_user(self, username, password):
        if username not in self.users:
            self.users[username] = password
            print(f"Користувач {username} успішно доданий.")
        else:
            print(f"Користувач з логіном {username} вже існує.")

    def remove_user(self, username):
        if username in self.users:
            del self.users[username]
            print(f"Користувач {username} успішно видалений.")
        else:
            print(f"Користувача з логіном {username} не існує.")

    def check_user(self, username):
        if username in self.users:
            print(f"Користувач {username} існує.")
        else:
            print(f"Користувача з логіном {username} не знайдено.")

    def change_username(self, old_username, new_username):
        if old_username in self.users:
            self.users[new_username] = self.users.pop(old_username)
            print(f"Логін користувача змінено з {old_username} на {new_username}.")
        else:
            print(f"Користувача з логіном {old_username} не знайдено.")

    def change_password(self, username, new_password):
        if username in self.users:
            self.users[username] = new_password
            print(f"Пароль користувача {username} змінено.")
        else:
            print(f"Користувача з логіном {username} не знайдено.")

    def display_users(self):
        print("Список користувачів:")
        for username, password in self.users.items():
            print(f"Логін: {username}, Пароль: {password}")


def main():
    db = UserDatabase()

    while True:
        print("\nМеню:")
        print("1. Додати нового користувача")
        print("2. Видалити існуючого користувача")
        print("3. Перевірити, чи існує користувач")
        print("4. Змінити логін існуючого користувача")
        print("5. Змінити пароль існуючого користувача")
        print("6. Показати всіх користувачів")
        print("0. Вихід")

        choice = input("Виберіть операцію: ")

        if choice == "1":
            username = input("Введіть логін нового користувача: ")
            password = input("Введіть пароль нового користувача: ")
            db.add_user(username, password)
        elif choice == "2":
            username = input("Введіть логін користувача для видалення: ")
            db.remove_user(username)
        elif choice == "3":
            username = input("Введіть логін користувача для перевірки: ")
            db.check_user(username)
        elif choice == "4":
            old_username = input("Введіть поточний логін користувача: ")
            new_username = input("Введіть новий логін користувача: ")
            db.change_username(old_username, new_username)
        elif choice == "5":
            username = input("Введіть логін користувача: ")
            new_password = input("Введіть новий пароль: ")
            db.change_password(username, new_password)
        elif choice == "6":
            db.display_users()
        elif choice == "0":
            print("Програма завершена.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()


# Завдання 4
class OrderQueue:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)
        print(f"Замовлення {order} додано до черги.")

    def process_order(self):
        if self.orders:
            processed_order = self.orders.pop(0)
            print(f"Оброблено замовлення {processed_order}.")
            return processed_order
        else:
            print("Черга замовлень порожня.")

    def show_orders(self):
        if self.orders:
            print("Замовлення у черзі:")
            for order in self.orders:
                print(order)
        else:
            print("Черга замовлень порожня.")


def main():
    order_queue = OrderQueue()

    while True:
        print("\nМеню:")
        print("1. Додати нове замовлення")
        print("2. Обробити наступне замовлення")
        print("3. Показати замовлення у черзі")
        print("0. Вихід")

        choice = input("Виберіть операцію: ")

        if choice == "1":
            new_order = input("Введіть нове замовлення: ")
            order_queue.add_order(new_order)
        elif choice == "2":
            order_queue.process_order()
        elif choice == "3":
            order_queue.show_orders()
        elif choice == "0":
            print("Програма завершена.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
