class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for index, val in enumerate(nums):
            if val in nums[index+1:]:
                return True
        return False