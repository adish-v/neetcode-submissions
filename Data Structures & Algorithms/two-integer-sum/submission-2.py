class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, index_val in enumerate(nums):
            jndex_val = target - index_val
            if jndex_val in nums[index+1:]:
                jndex = nums.index(jndex_val, index + 1)
                return [index, jndex]