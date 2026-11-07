

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