class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)-1
        s = float('inf')
        i = 0
        while(s != target):
            s = numbers[i] + numbers[n]
            if s > target:
                n -= 1
            else:
                i += 1
        return [i,n+1]



        