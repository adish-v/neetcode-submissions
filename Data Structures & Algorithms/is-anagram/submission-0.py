class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1, str2 = {}, {}
        for val in s:
            if val in str1:
                str1[val] += 1
            else:
                str1[val] = 1
        
        for val in t:
            if val in str2:
                str2[val] += 1
            else:
                str2[val] = 1
        
        if str1 == str2:
            return True
        
        return False