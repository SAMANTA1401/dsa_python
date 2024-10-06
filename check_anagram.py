##1. check two words are anagram or not means all the letters are common also handle space and caps


def anagram(str1,str2):
    group_letters={}
    for i in str1:
        if i in group_letters:
            group_letters[i]+=1
        else:
            group_letters[i]=1
        print(group_letters)

    for i in str2:
        if i in  group_letters:
            group_letters[i]-=1
        else:
            group_letters[i]=1
            return False
        print(group_letters)
        
    return True

string1=input("Enter first string : ")
string1 = string1.replace(" ","").lower()
string2=input("Enter the first string :")
string2=string2.replace(" ","").lower()
var = anagram(string1,string2)
if var:
    print("anagram")
else:
    print("not a anagram")

    
# print(sorted('study')) ## letters are splitd as char in ascending order based on ascii value

