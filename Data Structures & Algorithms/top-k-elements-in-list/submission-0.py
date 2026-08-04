class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        res = {}
        for elem in nums:
            if elem in res:
                res[elem] += 1
            else:
                res[elem] = 1
        # print(res)
        max = float('-inf')
        for _ in range(k):
            for k, v in res.items():
                if v > max:
                    max = k
            del res[max]
            result.append(max)
            max = float('-inf')
        
        return result
