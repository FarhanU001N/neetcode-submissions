class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[1]*len(nums)
        for x in range(0,len(nums)):
            if x==0:
                output[x]*=1
            else:
                output[x]=output[x-1]*nums[x-1]
        post=1
        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1:
                output[i]*=1
            else:
                post*=nums[i+1]
                output[i]*=post
        return output
            