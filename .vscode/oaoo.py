# s = input("Введите строку: ")

# letters = 0
# digits = 0
# spaces = 0
# punct = 0

# for ch in s:
#     if ch.isalpha():
#         letters += 1
#     elif ch.isdigit():
#         digits += 1
#     elif ch == " ":
#         spaces += 1
#     elif ch in ".,!?;:-—()\"'«»":
#         punct += 1

# print(f"Букв: {letters}")
# print(f"Цифр: {digits}")
# print(f"Пробелов: {spaces}")
# print(f"Знаков препинания: {punct}")


from datetime import date

day = int(input("Введите день: "))
month = int(input("Введите месяц: "))
year = int(input("Введите год: "))

today = date.today()

age = today.year - year

if (today.month, today.day) < (month, day):
    age -= 1
print(f"Вам {age} лет")