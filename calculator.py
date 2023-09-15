class Calculator:
    def __init__(self):
        pass

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Помилка: Ділення на нуль неможливе")
        return a / b

    @staticmethod
    def power(a, exponent):
        return a ** exponent

    @staticmethod
    def square_root(a):
        return a ** 0.5

    @staticmethod
    def cubic_root(a):
        return a ** (1/3)

    def run(self):
        while True:
            print("Меню операцій:")
            print("1. Додавання")
            print("2. Віднімання")
            print("3. Множення")
            print("4. Ділення")
            print("5. Зведення в ступінь")
            print("6. Квадратний корінь")
            print("7. Кубічний корінь")
            print("8. Вихід")

            choice = input("Виберіть операцію (введіть номер): ")

            if choice == "8":
                print("До побачення!")
                break

            try:
                num1 = float(input("Введіть перше число: "))
                if choice != "5" and choice != "6" and choice != "7":
                    num2 = float(input("Введіть друге число: "))
            except ValueError:
                print("Будь ласка, введіть коректні числа.")
                continue

            if choice == "1":
                print(f"Результат: {self.add(num1, num2)}")
            elif choice == "2":
                print(f"Результат: {self.subtract(num1, num2)}")
            elif choice == "3":
                print(f"Результат: {self.multiply(num1, num2)}")
            elif choice == "4":
                try:
                    print(f"Результат: {self.divide(num1, num2)}")
                except ValueError as e:
                    print(e)
            elif choice == "5":
                exponent = int(input("Введіть показник ступеня: "))
                print(f"Результат: {self.power(num1, exponent)}")
            elif choice == "6":
                print(f"Результат: {self.square_root(num1)}")
            elif choice == "7":
                print(f"Результат: {self.cubic_root(num1)}")
            else:
                print("Некоректний вибір. Введіть номер операції з меню.")

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
