class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        ops = {
    "-": lambda a, b: b - a,
    "+": lambda a, b: a + b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: int(b/a)
}
        
        for char in tokens:
            if char not in ops:
                stack.append(int(char))
            elif stack:
                a , b =stack.pop(), stack.pop()
                stack.append(ops[char](a,b))
        return stack[-1]
