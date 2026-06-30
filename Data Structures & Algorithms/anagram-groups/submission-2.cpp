class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> group; 
        vector < vector<string>> answer; 
        string sortedS;

    //making hash map of sorted stuff
        for (auto s : strs){
            sortedS = s; //assign s to sortedS and use sorting on sortedS so og s still there to use
            sort(sortedS.begin(), sortedS.end());
            group[sortedS].push_back(s);     //must use pushback for vectors to add elements

        }

    //display hashmap
        for (auto entry : group) {
            answer.push_back(entry.second);      //use .second to add value of the dictionary (the list of words that are anagrams)
                                                // to vector (this vector contains vectors of grouped anagrams)
        }
        

        return answer; 
    }
};
