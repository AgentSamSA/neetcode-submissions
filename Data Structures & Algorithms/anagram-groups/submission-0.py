class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        possible_grams = {}
        grams = []

        for s in strs:
            chars = [0] * 26
            for char in s:
                index = ord(char) - ord('a')
                chars[index] += 1
            
            chars_freq = tuple(chars)
            if chars_freq not in possible_grams:
                possible_grams[chars_freq] = []
            
            possible_grams[chars_freq].append(s)
        
        for char_freq in possible_grams:
            grams.append(possible_grams[char_freq])
        
        return grams