class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count ={}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums: 
            count[n] = 1 + count.get(n, 0) #increment count of each num
        for n, c in count.items(): #gets key value pair
            freq[c].append(n) #append num value to index count 
        
        res = []
        for i in range(len(freq) - 1, 0, -1): #increment backwards
            for n in freq[i]: #increment thru list at that index i
                res.append(n)
                if len(res) == k: #done when length of result array is same as k for kth most frequent
                    return res
