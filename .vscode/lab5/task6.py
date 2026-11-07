n = int(input('Введите число: '))
n_o = n
rev = 0
while n>0:
    i = n%10
    rev = rev*10+i
    n//=10
print(rev)
if n_o==rev:
    print(f"число {n_o} является палиндромом.")
else: 
    print(f"число {n_o} не является палиндромом.")