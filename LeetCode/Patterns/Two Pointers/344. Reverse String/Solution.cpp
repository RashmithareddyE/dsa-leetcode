class Solution {
public:
    void reverseString(vector<char>& s) {
        int n=s.size();
        int end=n-1;
        int st=0;
        while(st<end){
            swap(s[st++],s[end--]);
        }
        
    }
};