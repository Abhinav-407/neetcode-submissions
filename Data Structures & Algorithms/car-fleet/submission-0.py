class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort()
        stack = []
        for pos,spd in reversed(cars):
            time = (target-pos)/spd
            if not stack or time > stack[-1]:
                stack.append(time)
        
        return len(stack)