class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        cars=dict(zip(position,speed))
        asc = {k: v for k, v in sorted(cars.items(), key=lambda item: item[0])}
        post=sorted(position)
        for i in range (len(cars)-1,-1,-1):
            time=(target-post[i])/cars[post[i]]
            if not stack:
                stack.append(time)
            elif time > stack[-1]:
                stack.append(time)
        return len(stack)