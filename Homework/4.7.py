def fibo_gen(n):
    res=1
    for i in range(1, n+1):
        res *= i
        yield res
i=0
for el in fibo_gen(20):
    print(el)
    i +=1
    if i > 14:
        break