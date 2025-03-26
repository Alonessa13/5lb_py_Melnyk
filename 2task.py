import random
secret_number = random.randint(1, 50)
print("Я загадав число від 1 до 50. Спробуй вгадати!")
while True:
    guess = int(input("Введи число: "))
    difference = abs(secret_number – guess
        print("Вітаю! Ти вгадав!")
        break
    elif difference <= 3:
        print("Дуже близько!")
    elif difference <= 10:
        print("Близько!")
    else:
        print("Далеко!")
