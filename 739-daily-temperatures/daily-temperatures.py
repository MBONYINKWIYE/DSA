class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                day = stack.pop()
                # the No of days is equal to the current temp index - latest maximum warmer temp
                ans[day] = idx - day 

            stack.append(idx)

        return ans
        


        