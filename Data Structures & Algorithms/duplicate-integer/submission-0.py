class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        instance=set(nums)
        return (len(nums)!=len(instance))

        