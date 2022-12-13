##Determine if a string has all Unique Characters
##
##Difficulty Level : Easy
##Last Updated : 25 Apr, 2022
##Given a string, determine if the string has all unique characters.
##
##Examples :  
##
##Input : abcd10jk
##Output : true
##
##Input : hutg9mnd!nk9
##Output : false

import math

# T:O(logn) S:O(1)

def uniqueCharacterSort(s):
    s = sorted(s)
    for i in range(1,len(s)):
        if s[i]== s[i-1]:
            return False
    return True

def uniqueCharacterWithoutExtraSpace(s):
    checker = 0
    for i in s:
        ascii = ord(i) - ord('a')
        if ascii<0:
            continue
        if (checker & (1<<ascii))>0:
            return False
        checker = checker | (1<<ascii)
    return True

def main():
    s = "rovaal"
    print(uniqueCharacterWithoutExtraSpace(s))
main()
