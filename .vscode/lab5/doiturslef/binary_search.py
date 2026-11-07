nums = list(map(int,input().split()))
target = int(input("Введите чилсо для поиска"))
lt = 0
rt = len(nums) - 1
found = -1
while lt <= rt:
    mid = (lt+rt)//2
    if nums [mid] == target:
        found = mid
        break
    elif nums[mid]<target:
        lt = mid+1
    else:
        rt = mid-1
if found == -1:
    print("ничегр не найдено ")
else:
    print(f"найдено, индекс {found}")