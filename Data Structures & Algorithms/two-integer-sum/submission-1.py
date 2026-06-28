class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j == i:
                    j += 1
                add = nums[i] + nums[j]
                if add == target:
                    yay = list([i, j])
                    return yay
                else:
                    continue 
        
                    
