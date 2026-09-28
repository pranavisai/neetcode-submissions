class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)-1
        i = 0
        while(i < n):
            s = numbers[i] + numbers[n]
            if s == target:
                return [i+1, n+1]
            elif s > target:
                n -= 1
            else:
                i += 1



        