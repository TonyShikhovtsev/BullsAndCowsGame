import random

class BullsAndCowsGame:
    def __init__(self):
        self.secret_number = self.generate_number()
        self.history = []

    @staticmethod
    def generate_number():
        """Генерация четырехзначного числа с разными цифрами."""
        while True:
            number = str(random.randint(1000, 9999))
            if len(set(number)) == 4:
                return number

    def check_guess(self, guess):
        """Проверка числа на быков и коров."""
        bulls = sum(s == g for s, g in zip(self.secret_number, guess))
        cows = sum(s in guess for s in self.secret_number) - bulls
        return bulls, cows

    def show_history(self):
        """Показать историю запросов и ответов."""
        print("\nИстория:")
        for turn, (guess, result) in enumerate(self.history, start=1):
            print(f"{turn}. Вы ввели: {guess}, Результат: {result}")

    def play(self):
        print("Добро пожаловать в игру 'Быки и коровы'!")

        while True:
            user_input = input("Введите вашу догадку (четырехзначное число): ")

            if not user_input.isdigit() or len(user_input) != 4 or len(set(user_input)) != 4:
                print("Некорректный ввод. Пожалуйста, введите четырехзначное число с разными цифрами.")
                continue

            bulls, cows = self.check_guess(user_input)
            self.history.append((user_input, f"{bulls} бык., {cows} кор."))

            if bulls == 4:
                print("Поздравляю! Вы угадали число!")
                break
            else:
                self.show_history()
