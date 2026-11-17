class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}

        for num in nums:
            res[num] = res.get(num, 0) + 1
        
        return sorted(res.keys(), key=lambda x: res[x], reverse=True)[:k]