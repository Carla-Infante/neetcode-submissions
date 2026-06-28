class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for num in nums:  
             d[num] += 1

        m = []
        for key, value in d.items():
            m.append([key, value])
        
        m.sort(key = lambda x:x[1])

        res = []
        while k!= 0:
            s = m.pop()
            res.append(s[0])

            k -= 1

        return res

           
        

