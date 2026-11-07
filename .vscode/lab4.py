import random

def guess():
    n = random.randint(1, 100)
    
    print("угадайте число")
    
    while True:
        try:
            t = int(input("ввкедите попытку"))
            if t < n:
                print("Больше")
            elif guess > n:
                print("Меньше")
            else:
                print(f"Поздравляю! Вы угадали число {n}!")
                break
        except ValueError:
            print("нет")

guess()