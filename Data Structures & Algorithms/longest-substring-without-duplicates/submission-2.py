class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0
        l = 0
        this_set = set()
        for i in range(len(s)):
            while s[i] in this_set:
                this_set.remove(s[l])
                l += 1
            this_set.add(s[i])
            max_count = max(max_count, len(this_set))
        return max_count
            
        