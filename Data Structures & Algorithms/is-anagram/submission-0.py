class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq_s = {}
        freq_t = {}

        for i in range(len(s)):
            if s[i] not in freq_s:
                freq_s[s[i]] = 1
            else:
                freq_s[s[i]] += 1
        
        for i in range(len(t)):
            if t[i] not in freq_t:
                freq_t[t[i]] = 1
            else:
                freq_t[t[i]] += 1
        
        if freq_s == freq_t:
            return True
        else:
            return False
