# Вывод таблицы значений функции y = x² − 2x + 1 для x от −5 до 5
# 3
# print(f"{"x":>10}{"y":>10}")
# for x in range(-5,6):
#     y = x**2-2*x+1
#     print(f"{x:10.0f}{y:10.0f}")

# 6 
# Перевод числа из десятичной системы в двоичную и обратно
# n_bin = bin(n)[2:]
def d_to_b():
    n = int(input("num (decimal): "))
    binary = ''
    while n>0:
        binary+=str(n%2)
        n//=2
    return int(binary[::-1])
print(d_to_b())

def b_to_d():
    n = int(input("num (binary): "))
    dec = 0
    for x in range(len(str(n))):
        cur = str(n)[x]
        if cur !='0':dec+=2**(len(str(n))-x-1)
    return dec
print(b_to_d())