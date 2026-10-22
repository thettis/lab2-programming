# a = int(input('Введите число'))
# if a%2==0: print(f"{a} - четное число")
# if a%2!=0: print(f"{a} - нечетное число")

# a,b,c = map(int,input('введите 3 числа через пробел').split())
# if a>=b and a>=c: print(f"{a} - максимальное число")
# if b>= a and b>= c: print(f"{b}- максимальное число")
# if c>=a and c>=b: print(f"{c}- максимальное число")

# age = int(input('введите возраст: '))
# if age<0: print('Некорректный возраст')
# if age <= 12: print('Ребенок')
# if 12<age <=17: print('Подросток')
# if 17<age<=64: print('Взрослый')
# if age>=64: print('Пожилой')

# a, b, c = map(float,input("Введите коэффициенты a, b, c через запятую").split(','))
# if a == 0: 
#     print("это не квадратное уравнение")
# else:
#     D = b**2-4*a*c
#     if D<0: 
#         print('корней нет')
#     elif D==0: 
#         x = -b/(2*a)
#         print(f'существует только один корень: {x:.2f}')
#     else: 
#         x1 = (-b+D**0.5)/(2*a)
#         x2 = (-b-D**0.5)/(2*a)
#         print(f"1-й корень: {x1:.2f}; 2-й корень: {x2:.2f}")

# a,b = map(float, input('введите 2 числа через запятую').split(","))
# operation = str(input('Выберите операцию из предложенных: (+, -, *, /): '))
# match operation:
#     case "+":
#         print(f"Result: {a+b}")
#     case "-":
#         print(f"Result: {a-b}")
#     case "*":
#         print(f"Result: {a*b}")
#     case "/":
#         if b!=0:
#             print(f"Result: {a/b:.2f}")
#         else: 
#             print('Error!')
#     case _:
#         print("Error!")

# year = int(input("Введите год"))
# if (year%4==0 and year %100!=0) or( year % 400 == 0):
#     print(f"{year} - високосный год.")
# else:
#     print(f"{year} - не високосный год.")

# a,b,c = map(int, input('Введите сторороны треугольника через пробел').split())
# if a + b > c and a + c > b and b + c > a:
#     if a == b == c: 
#         print("Треугольник равносторонний.")
#     elif a==b or b==c or a==c:
#         print("Треугольник равнобедренный.")
#     else:
#         print("Треугольник разносторонний.")
# else: 
#     print(f"Tреугольника со сторонами {a}, {b}, {c} не существует.")

hour = int(input('который час? '))
if 5<=hour<=11: 
    print('Сейчас утро.')
elif 12<=hour<=17: 
    print("Сейчас день.")
elif 18<= hour<=21: 
    print("Сейчас вечер")
elif 22<= hour <= 23 or 0<=hour<=4: 
    print("Сейчас ночь.")
else:
    print("Вы некорректно ввели время.")

