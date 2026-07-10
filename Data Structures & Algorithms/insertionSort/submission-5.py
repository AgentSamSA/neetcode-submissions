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
            print('i', i)
            for j in range(i, 0, -1):
                print('j', j)
                curr = temp[j]
                print('curr', (curr.key, curr.value))
                prev = temp[j - 1]
                print('prev', (prev.key, prev.value))

                if curr.key < prev.key:
                    temp[j] = prev
                    temp[j - 1] = curr
            print('temp inner', [(t.key, t.value) for t in temp])
            
            states.append(temp)
            temp = [t for t in temp]
        
        return states