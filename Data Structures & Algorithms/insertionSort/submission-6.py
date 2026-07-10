# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        # key idea: place in correct position based on key
        # one idea: compare against base value and move to front if smaller
        # do we swap positions? we need to maintain relative order
        
        states = []
        temp = [p for p in pairs]

        for i in range(len(temp)):
            for j in range(i, 0, -1):
                curr = temp[j]
                prev = temp[j - 1]

                if curr.key < prev.key:
                    temp[j] = prev
                    temp[j - 1] = curr
                else:
                    break
            
            states.append(temp)
            temp = [t for t in temp]
        
        return states