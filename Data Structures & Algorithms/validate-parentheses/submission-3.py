class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        op=['(','[','{']
        close={')':'(',']':'[','}':'{'}        
        for bracket in s:
            if bracket in op:
                stack.append(bracket)
            if bracket in close:
                if not stack:
                    return False            
                elif stack[-1]==close[bracket]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False
