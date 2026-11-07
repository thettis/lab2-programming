n = int(input("Введите точность: "))
e = 1
def factorial(n):
    if n<0:
        print('net')
    return 1 if n<=1 else n*factorial(n-1)

for x in range(1, n+1):
    
    e+=(1/factorial(x))
print(f"число е с точностью {n}: {e}")