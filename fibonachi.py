def fib(n):
    l = dict()
    l[0]=0
    l[1]=1

    for i in range (2,n):
        l[i]=l[i-1]+l[i-2]
    
    return l[n-1]

print(fib(2))
print(fib(10))

def get_fib(position):
    if position == 0 or position == 1:
        return position
    return get_fib(position - 1) + get_fib(position - 2)