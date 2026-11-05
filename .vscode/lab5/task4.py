# def f(n):
#     dels = []
#     for d in range(1,int(n**0.5)+1):
#         if n%d==0:
#             dels.append(d)
#             dels.append(n//d)
#     return sorted(dels)
# print(f(15))

n = int(input('Enter your number: '))
n_o = n
d = 2
res = []
while d*d<=n:
    while n%d==0:
        res+=[d]
        n//=d
    d+=1
if n>1:
    res.append(n)
print(f"{n_o} = {'x'.join(map(str,res))}")