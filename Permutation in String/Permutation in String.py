# Solution Roval T:O(26*l) S:O(1) l - length of s2
# 05-09-2022

from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1C = Counter(s1)
        s2C = Counter(s2[0:len(s1)])
        
        def checker(c1,c2):
            for i in c1:
                if c1[i]!=c2[i]:
                    return False
            return True
        if checker(s1C,s2C):
            return True
        for i in range(len(s1),len(s2)):
            s2C[s2[i-len(s1)]]-=1
            if s2[i] not in s2C:
                s2C[s2[i]] = 1
            else:
                s2C[s2[i]]+=1
            if checker(s1C,s2C):
                return True
        return False

#T:O(S2) S:O(1)
def checker(arr1,arr2):
    for i in range(0,26):
        if arr1[i]!=arr2[i]:
            return False
    return True
def permutationInString(string1,string2):
    arrStr1 = [0]*26
    arrStr2 = [0]*26
    if len(string1)>len(string2):
            return False
    for i in range(0,len(string1)):
        arrStr1[ord(string1[i])-ord('a')]+=1
        arrStr2[ord(string2[i])-ord('a')]+=1
    if checker(arrStr1,arrStr2):
        return True
    for i in range(len(string1),len(string2)):
        index = ord(string2[i-len(string1)])-ord('a')
        arrStr2[index] = 0 if arrStr2[index]==0 else arrStr2[index]-1
        arrStr2[ord(string2[i])-ord('a')]+=1
        if checker(arrStr1,arrStr2):
            return True
    return False

def main():
    string1 = "abo"
    string2 = "eidbaooo"
    print(permutationInString(string1,string2))
####
main()



