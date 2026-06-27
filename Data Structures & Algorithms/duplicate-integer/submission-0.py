class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set(nums);
        print(my_set);
        return len(nums) != len(my_set)