class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums_set = set(nums)

        hash_map = {}

        for num in nums_set:
            if num-1 not in nums_set:
                current_sequence = [num]
                
                i = 1
                while num+i in nums_set:
                    current_sequence.append(num+i)
                    i+= 1
                
                hash_map[num] = current_sequence
        
        return len(max(hash_map.values(), key=len))