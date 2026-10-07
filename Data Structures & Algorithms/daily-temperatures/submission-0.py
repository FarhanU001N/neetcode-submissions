class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output=[0]*len(temperatures)
        stack=[]
        for i in range(0,len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                a=stack.pop()
                output[a]=i-a
            stack.append(i)
        return output