# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        states = []
        temp = pairs.copy()

        for i in range(len(temp)):
            j = i
            while j > 0 and temp[j].key < temp[j - 1].key:
                temp[j], temp[j - 1] = temp[j - 1], temp[j]
                j -= 1

            states.append(temp.copy())
        
        return states
        