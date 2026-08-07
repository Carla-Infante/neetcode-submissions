class Solution:

    def encode(self, strs: List[str]) -> str:
        newWord = ""
        for word in strs:
            newWord += str(len(word)) + "#" + word
        return newWord

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1 #put j pointer on delimiter in case length of word requires more than 1 space like ex: 20
            length = int(s[i:j]) #length of word u gotta decode
            i = j + 1 #put i pointer on start of actual word, which isi one more than #
            j = i + length #do i + legnth bc just doing j + length would put j at last char of word but slicing won't include the last number in slice
            #so j is at next number
            res.append(s[i:j])
            i = j #repoint i to j for next word

        return res

            
            
