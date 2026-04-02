class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        need={}
        for ch in t:
            need[ch] = need.get(ch,0) + 1
        required = len(need)    
        formed = 0
        window = {}
        i = 0
        j = 0
        min_len = float("inf")    
        min_window = ""
        while j<len(s):
            char = s[j]
            window[char] = window.get(char,0) + 1
            if char in need and window[char] == need[char]:
                formed += 1
            while i<=j and formed == required:
                if j-i+1 < min_len:
                    min_len = j-i+1
                    min_window = s[i:j+1]
                left_char =s[i]
                window[left_char]-=1
                if left_char in need and window[left_char]< need[left_char]:
                    formed-=1
                i+=1
            j+=1
        return min_window                

