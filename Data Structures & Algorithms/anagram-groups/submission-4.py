class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqs = {}

        for s in strs:
            freq = [0] * 26
            for char in s:
                index = ord(char) - ord('a')
                freq[index] += 1
            
            freq_key = tuple(freq)

            if freq_key not in freqs:
                freqs[freq_key] = []
            freqs[freq_key].append(s)
        
        return list(freqs.values())