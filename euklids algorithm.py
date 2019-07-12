def eukl(a,b):
    if b ==0:
        return a

    return eukl(b,a%b)

print (eukl(10,4))
print(eukl(4,10))
        