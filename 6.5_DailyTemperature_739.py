class Solution:
    def dailyTemperatures(self, T):

        ans = [0]*len(T) 
        stack = []

        for i,v in enumerate(T):

            while stack and stack[-1][1] < v:
                index,value = stack.pop()
                ans[index] = i - index # we are checking how many indices we have crossed since we last have a lesser temperature
	
            stack.append([i,v])      

        return ans
	