class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = dict(Counter(nums))
        a = []
        sorted_desc = dict(sorted(nums_dict.items(), key=lambda item: item[1], reverse=True))
        a_list = list(sorted_desc)
        return a_list[:k]

        