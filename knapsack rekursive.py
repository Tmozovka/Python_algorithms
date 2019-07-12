w = [1,2,4,2,5]
v = [5,3,5,3,2]
num = 4
compacity = 10
arr = [[None for _ in range(num + 1)] for _ in range(compacity + 1)]
def KS(n,c):
    if arr[c][n] is not None:
        result =  arr[c][n]
    if n == -1 or c == 0:
        result =  0
    elif w[n] > c:
        result = KS(n - 1, c)
    else:
        tmp1 = KS(n - 1, c)
        tmp2 = v[n] + KS(n - 1, c - w[n])
        result = max(tmp1, tmp2)
    arr[c][n] = result
    return result



print(KS(num,compacity))