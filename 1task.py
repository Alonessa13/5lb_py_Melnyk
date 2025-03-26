import random
secret_number = random.randint(1, 10)
print("Я загадав число від 1 до 10. Спробуй вгадати!")
while True:
    guess = int(input("Введи число: "))
    if guess < secret_number:
        print("Більше!")
    elif guess > secret_number:
        print("Менше!")
    else:
        print("Вітаю! Ти вгадав!")
        break
