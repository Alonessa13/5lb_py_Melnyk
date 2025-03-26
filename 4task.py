import random
secret_pin = str(random.randint(1000, 9999))
attempts = 5  # Кількість спроб
print("Я загадав 4-значний PIN-код. Спробуй вгадати!")
while attempts > 0:
    guess = input("Введи PIN-код: ")
    if guess == secret_pin:
        print("Вітаю! Ти правильно відгадав PIN-код!")
        break
    else:
        correct_positions = sum(1 for i in range(4) if guess[i] == secret_pin[i])
        print(f"Невірно! {correct_positions} цифри на правильних місцях.")
        attempts -= 1
    if attempts == 0:
        print(f"Спроби закінчились! Правильний PIN-код: {secret_pin}.")
