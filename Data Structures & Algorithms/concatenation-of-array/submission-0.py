class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        result = len(nums)

        for i in range(0,result):
            nums.append(nums[i])
        return nums
        