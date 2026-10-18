class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        k = len(nums) - 1
        while(i <= k):
            n = i + (k - i) // 2
            if nums[n] == target:
                return n
            elif nums[n] > target:
                k = n - 1
            else:
                i = n + 1
        return -1


        
        