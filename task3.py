import random

number_to_guess = random.randint(1, 10)
attempts = 3

print("Вгадай число від 1 до 10!")

for attempt in range(attempts):
    guess = int(input(f"Спроба {attempt + 1}: Введіть ваше число: "))

    if guess > number_to_guess:
        print("Менше")
    elif guess < number_to_guess:
        print("Більше")
    else:
        print("Ви вгадали число")
        break
else:
    print(f"На жаль, ви не вгадали. Загадане число було {number_to_guess}.")
