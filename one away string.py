# Implement your function below.
def is_one_away(s1, s2):
    i=0
    j=0
    count=0
    if len(s1)==len(s2) or len(s1)+1==len(s2) or len(s1)== len(s2)+1:    
        while i !=len(s1) and j!=len(s2):
            if s1[i]!=s2[j] or (i==len(s1) and j!=len(s2)) or (i!=len(s1) and j==len(s2)):
                if len(s1)+1==len(s2):
                    i+=1
                if len(s1)== len(s2)+1:
                    j+=1
                count+=1
                if count==2:
                    return False
            i+=1
            j+=1

        return True
    else:
        return False
# NOTE: The following input values will be used for testing your solution.
print(is_one_away("abcde", "abcd"))  # should return True
print(is_one_away("abde", "abcde"))  # should return True
print(is_one_away("a", "a"))  # should return True
print(is_one_away("abcdef", "abqdef"))  # should return True
print(is_one_away("abcdef", "abccef"))  # should return True
print(is_one_away("abcdef", "abcde"))  # should return True
print(is_one_away("aaa", "abc"))  # should return False
print(is_one_away("abcde", "abc"))  # should return False
print(is_one_away("abc", "abcde"))  # should return False
print(is_one_away("abc", "bcc"))  # should return False
