class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        answer = [0]*len(temp)
        stack = []
        for i,t in enumerate(temp):
            while stack and t>temp[stack[-1]]:
                p = stack.pop()
                answer[p]= i-p
            stack.append(i)
        return answer
        