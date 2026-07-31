class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # really naive: store each element in a hash map as a key. Then, if we come across a value that is 1 greater than the key, update the length
        # issue: we have to update the previous element
        # sorting list will be O(n logn) so thats out
        # unsorted array so this doesn't work
        # try every element as start of sequence and count length of sequences formed from that element
        sequences = {}
        sequence_starters = set(nums)

        for num in nums:
            if num not in sequences and num - 1 not in sequence_starters:
                sequences[num] = 1
            else:
                continue
            
            curr = num
            while (curr + 1 in sequence_starters):
                curr += 1
                sequences[num] += 1
        
        return max(sequences.values(), default=0)