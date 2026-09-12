class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        myMap = {} # value : index

        for i, num in enumerate(nums):
            if num not in myMap:
                myMap[num] = [i]
            else:
                indexs = myMap[num]
                for j in indexs:
                    print(i,j)
                    if abs(i-j) <= k:
                        return True
                myMap[num].append(i)
        return False