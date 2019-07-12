# Implement your function below.
def non_repeating(given_string):
    d = {}

    for char in given_string:
        if char not in d.keys():
            d[char]=1
        else:
            d[char]+=1

    for char in given_string:
        if given_string[char]==1:
            return char

    return None

# NOTE: The following input values will be used for testing your solution.
print(non_repeating("abcab")) # should return 'c'
print(non_repeating("abab")) # should return None
print(non_repeating("aabbbc")) # should return 'c'
print(non_repeating("aabbdbc")) # should return 'd'