##1. check two words are anagram or not means all the letters are common also handle space and caps
# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.

def anagram(str1,str2):
    if len(str1) != len(str2): # # Quick length check (optional optimization)
        return False
    group_letters={} # hash dictionary
    for i in str1:
        if i in group_letters:
            group_letters[i]+=1
        else:
            group_letters[i]=1
        print(group_letters)

    for i in str2:
        if i in  group_letters:
            group_letters[i]-=1
            if group_letters[i] < 0:  # More occurrences in str2 than str1
                return False
        else:
            return False  # # Character in str2 not in str1
        print(group_letters)
        
    # Check if all counts are zero
    for count in group_letters.values():
        if count != 0:
            return False
        
    return True


string1 = "abcde"
string2 = "edcbb"
# string1=input("Enter first string : ")
string1 = string1.replace(" ","").lower()
# string2=input("Enter the first string :")
string2=string2.replace(" ","").lower()
var = anagram(string1,string2)
if var:
    print("anagram")
else:
    print("not a anagram")

    
# print(sorted('study')) ## letters are splitted as char in ascending order based on ascii value

# Time Complexity
# Building group_letters: O(n) where n = len(str1).
# Subtracting counts: O(m) where m = len(str2).
# Final check: O(k) where k is the number of unique characters in str1.
# Total: O(n + m), typically simplified to O(n) if n ≈ m.

# Space Complexity
# O(k) where k is the number of unique characters in str1 (size of the dictionary).

# {'a': 1}
# {'a': 1, 'b': 1}
# {'a': 1, 'b': 1, 'c': 1}
# {'a': 1, 'b': 1, 'c': 1, 'd': 1}
# {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1}
# {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 0}
# {'a': 1, 'b': 1, 'c': 1, 'd': 0, 'e': 0}
# {'a': 1, 'b': 1, 'c': 0, 'd': 0, 'e': 0}
# {'a': 1, 'b': 0, 'c': 0, 'd': 0, 'e': 0}
# {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}