class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        possible_grams = {}

        for s in strs:
            chars = [0] * 26
            for char in s:
                index = ord(char) - ord('a')
                chars[index] += 1
            
            chars_freq = tuple(chars)
            if chars_freq not in possible_grams:
                possible_grams[chars_freq] = []
            
            possible_grams[chars_freq].append(s)
        
        return list(possible_grams.values())