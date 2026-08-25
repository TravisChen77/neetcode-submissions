class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsCopy = set()
        size = len(nums)
        for num in nums:
            numsCopy.add(num)
        if size == len(numsCopy):
            return False 
        else:
            return True
