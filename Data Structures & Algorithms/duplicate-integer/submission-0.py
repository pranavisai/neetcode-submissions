class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num = set(nums)
        print(num)
        if len(nums) == len(num):
            return False
        return True