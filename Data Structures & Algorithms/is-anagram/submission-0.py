class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count_s = dict(Counter(s))
        char_count_t = dict(Counter(t))
        if char_count_s == char_count_t:
            return True
        return False