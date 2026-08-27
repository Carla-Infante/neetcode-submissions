class Solution:
    def isPalindrome(self, s: str) -> bool:
        lPtr = 0
        rPtr = len(s)-1 #set up 2 pointers

        while lPtr < rPtr:

            while (lPtr < rPtr and not self.alphaNum(s[lPtr])): #test lPtr < rPtr again bc Ah, the key is that the first while only checks l < r once per iteration. It doesn't guarantee that l < r will still be true after the inner loops move the pointer
                lPtr += 1
            
            while (rPtr > lPtr and not self.alphaNum(s[rPtr])):
                rPtr -= 1

            if (s[lPtr].lower() != s[rPtr].lower()): #compare lowercase versions
                return False
            lPtr +=1
            rPtr -=1

        return True
    
    def alphaNum(self, c): #function for seeing if the char is alphanumeric
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9') )