class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # dictionary where key is number and value is the index

        for i in range(len(nums)): #ITERATE THRU LIST
            test = target - nums[i] #CALCULATE COMPLEMENT OF CURRENT ELEMENT
            if (test in seen): #check if that complement is in the dictionary
                return [seen[test], i] #if it is then return
            seen[nums[i]] = i #otherwise, add  current num to hash 

            
            

