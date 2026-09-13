class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr = -1

        for i in range(len(arr)-1, -1, -1):
            temp = arr[i]
            arr[i] = curr
            curr = max(curr, temp)

        return arr