class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        finder={}
        for i,num in enumerate(nums):
            diff=target-num
            if diff in finder:
                return [finder[diff],i]
            else:
                finder[num]=i

        