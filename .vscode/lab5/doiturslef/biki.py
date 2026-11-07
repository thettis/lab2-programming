
import random

digits = random.sample("0123456789", 4)
secret = "".join(digits)

print("Угадайте четырехзначное число.")

while True:
    guess = input("Введите число: ")

    if len(guess) != 4 or not guess.isdigit():
        print("Введите именно четырехзначное число!")
        continue

    if len(set(guess)) != 4:
        print("Цифры не должны повторяться!")
        continue

    bulls = 0
    cows = 0

    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1

    print("Быки:", bulls)
    print("Коровы:", cows)

    if bulls == 4:
        print("Поздравляем! Вы угадали число!")
        break
