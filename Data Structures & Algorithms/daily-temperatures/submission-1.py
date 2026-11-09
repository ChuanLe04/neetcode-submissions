class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        results = [0] * n
        stack = []

        for current_day, current_temp in enumerate(temperatures):
            while stack and current_temp > temperatures[stack[-1]]:
                prev_day = stack.pop()
                results[prev_day] = current_day - prev_day

        
            stack.append(current_day)

        return results