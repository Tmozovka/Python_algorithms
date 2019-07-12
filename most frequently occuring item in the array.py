

def frequency(array):
    max_item = None
    max_count = -1 
    d= dict()
    for item in array:
        if item in d.keys():
            d[item]+=1
        else:
            d[item]=1
        if d[item]>max_count:
            max_count=d[item]
            max_item = item
    
    return max_item
    

array = [1,2,3,4,1,2,5,6,1,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
print(frequency(array))

array = []
print(frequency(array))

array = [1]
print(frequency(array))
        