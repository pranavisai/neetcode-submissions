class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = re.sub(r'[^a-zA-Z0-9]', '', s)
        res1 = res.lower()
        res2 = res1[::-1]
        if res1 == res2:
            return True
        return False
        
        