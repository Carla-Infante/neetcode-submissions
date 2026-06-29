class Solution {
public:
    bool isPalindrome(string s) {
        string sReversed, s2; 

        for(int i = 0; i < s.length(); i++){
            if(isalnum(s[i])){
                s2 += tolower(s[i]);
            }
        }

        for(int i = s2.length()-1; i >= 0; i--){
            sReversed += s2[i]; 
        }

        return s2 == sReversed; 
    }
};
