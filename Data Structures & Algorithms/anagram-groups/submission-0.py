class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def create_hash(string):
            hash_string = {}
            for val in string:
                if val in hash_string:
                    hash_string[val] += 1
                else:
                    hash_string[val] = 1
            return hash_string
        
        hash_strings = []
        for val in strs:
            hash_strings.append(create_hash(val))
        
        sub_result = []
        # visited_index = []
        visited_jndex = []
        for index, index_val in enumerate(hash_strings):
            temp = set([index])
            for jndex, jndex_val in enumerate(hash_strings):
                if index_val == jndex_val and jndex not in visited_jndex:
                    temp.add(jndex)
                    visited_jndex.append(jndex)
            if index not in [item for sublist in sub_result for item in sublist]:
                sub_result.append(temp)
                # visited_index.append(index)
        
        result = []
        for vals in sub_result:
            temp = []
            for val in vals:
                temp.append(strs[val])
            result.append(temp)
        
        return result