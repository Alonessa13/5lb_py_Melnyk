import tkinter as tk
import random
# Список кольорів
colors = {
    "червоний": "теплий",
    "жовтий": "теплий",
    "синій": "холодний",
    "зелений": "холодний",
    "фіолетовий": "холодний"
}
# Випадковий  загаданй колір
secret_color = random.choice(list(colors.keys()))
attempts = 3  # Кількість спроб
# Функція для перевірки відповіді
def check_guess():
    global attempts
    guess = entry.get().strip().lower()
    if guess == secret_color:
        result_label.config(text="Вітаю! Ти вгадав колір!", fg="green")
        button_check.config(state=tk.DISABLED)
    else:
        attempts -= 1
        if attempts > 0:
            result_label.config(text=f"Невірно! Це {colors[secret_color]} колір.\nЗалишилось спроб: {attempts}",
                                fg="red")
        else:
            result_label.config(text=f"Гра закінчена! Загаданий колір був: {secret_color}.", fg="black")
            button_check.config(state=tk.DISABLED)
# Створення вікна інтерфейсу
root = tk.Tk()
root.title("Гра: Вгадай колір")
root.geometry("400x300")
# Заголовок
label = tk.Label(root, text="Вгадай колір: червоний, жовтий, синій, зелений, фіолетовий", font=("Arial", 12))
label.pack(pady=10)
# Поле вводу
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=5)
# Кнопка "Перевірити"
button_check = tk.Button(root, text="Перевірити", font=("Arial", 12), command=check_guess)
button_check.pack(pady=5)
# Поле для виводу результату
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)
# Запуск
root.mainloop()
