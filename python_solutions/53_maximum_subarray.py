# insp
class Solution:
    
    def max(n1,n2):
        if n1>n2:
            return n1
        return n2
    
    def maxSubArray(self, nums: list) -> int:
        current_sum=-1000000000
        global_sum= -1000000000
        for element in nums:
            global_sum = max(global_sum,current_sum)
            if current_sum >=0:
                if element+current_sum<=0:
                    current_sum=element
                else:
                    current_sum +=element
            else:
                current_sum = element

        return max(global_sum,current_sum)
                
                
            

       
inputs=[[-2,1,-3,4,-1,2,1,-5,4],[-3, -1] ]
for input in inputs:          
    print(Solution().maxSubArray(input))
        