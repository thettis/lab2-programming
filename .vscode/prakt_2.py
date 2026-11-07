def task1 (nums):
    done = {}
    for i, base in nums.items():
        dv = int(i, base)
        done[f'{i}(base: {base})'] = dv
    for key, val in done.items():
        print(f'{key} = {val}(10)')
    s_nums = sorted(done.items(), key= lambda item: item[1])
    print(s_nums)
    print(f'min:{s_nums[0][0]} ({s_nums[0][1]})')
    print(f'max:{s_nums[-1][0]} ({s_nums[-1][1]})')
    print('ascending:','>'.join([f"{k}" for k,v in s_nums]))
    print('decreasing:','>'.join([f"{k}" for k,v in reversed(s_nums)]))
nums = {
    '1000000':2,
    '62':8,
    '39':16,
    '52':10
}
task1(nums)

def task2(num):        
    if num[0] == '0':
        res = int(num, 2)
    else:
        inverted = "".join('1' if bit == '0' else '0' for bit in num)
        print(inverted)
        res = -int(inverted, 2)
    print(f"{num} 2 = {res} 10")
    return res
task2('00000101')

def task3(num): 
    if num>=0:
        bn = format(num, '08b')
        inv = ''.join('1' if i == '0' else '0' for i in bn)
        res = int(inv,2)

    else:
        bn = format(abs(num), '08b')
        inv = ''.join('1' if i == '0' else '0' for i in bn)
        res = format(int(inv,2)+1,'08b')
    return res
print(task3(-5))

def task4(num1,num2):
    for base in range(2,37):
        try:
            if int(str(num2),base) == num1:
                res = base
                break
        except ValueError:
            continue
    return res
print(task4(14,16))
        