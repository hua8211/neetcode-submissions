class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = []

        for x in range(len(arr)-1):
            arr.pop(0)
            result.append(max(arr))
        
        result.append(-1)
        return result