class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1 = {}
        str2 = {}

        for val1, val2 in zip(s, t):
            str1[val1] = ''
            str2[val2] = ''
        
        if str1 == str2:
            return True
        
        return False