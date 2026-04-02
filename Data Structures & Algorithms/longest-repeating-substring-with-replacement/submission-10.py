class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        j = 0
        n = len(s)
        count = {}
        max_freq = 0
        max_length = 0
        while j < n:
            count[s[j]] = count.get(s[j], 0) + 1
            max_freq = max(max_freq, count[s[j]])
            while((j-i+1) - (max_freq)
                    ) > k:
                count[s[i]] -=1
                i=i+1
            max_length = max(max_length, j-i+1)
            j=j+1
        return max_length