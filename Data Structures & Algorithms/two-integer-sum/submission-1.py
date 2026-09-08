class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map_nums = {}
        for i, n in enumerate(nums):
            j = target - n
            if j in hash_map_nums:
                return [hash_map_nums[j], i]
            hash_map_nums[n] = i
        