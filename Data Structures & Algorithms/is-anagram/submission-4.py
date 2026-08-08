class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1 = {}
        str2 = {}

        if len(s) != len(t):
            return False

        for val1, val2 in zip(s, t):
            if val1 in str1:
                str1[val1] += 1
            else:
                str1[val1] = 1
            
            if val2 in str2:
                str2[val2] += 1
            else:
                str2[val2] = 1
        
        if str1 == str2:
            return True
        
        return False