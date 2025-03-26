import random
secret_number = random.randint(1, 20)
attempts = 3  # Кількість спроб
print("Я загадав число від 1 до 20. У тебе 3 спроби!")
while attempts > 0:
    guess = int(input("Введи число: "))
    if guess == secret_number:
        print("Вітаю! Ти вгадав!")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Неправильно! У тебе залишилося {attempts} спроб.")
        else:
            print(f"Гра закінчена! Загадане число було {secret_number}.")
