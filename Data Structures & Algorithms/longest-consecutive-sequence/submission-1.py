class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in nums: #iterate thru nums
            
            if (num - 1) in numSet:
                continue
            length = 0
            while(num + length) in numSet: 
                length += 1
            longest = max(length, longest)
        return longest