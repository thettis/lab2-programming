numbers = list(map(int, input("ваш список через пробел: ").split()))
print(f"До сортировки: {numbers}")
n = len(numbers)
for i in range(n-1):
    for j in range(n-1-i):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1],numbers[j]

print(f"После сортировки: {numbers}")