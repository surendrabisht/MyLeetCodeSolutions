class Solution:
    def __init__(self) -> None:
        self.step_min_cost=[]

    def minCostClimbingStairs(self, cost: list[int]) -> int:
        cost.append(0)
        self.step_min_cost=[-1]*len(cost)
        self.step_min_cost[0]=cost[0]
        self.step_min_cost[1]=cost[1]
        for i in range(2,len(self.step_min_cost)):
            self.step_min_cost[i]=min(self.step_min_cost[i-1],self.step_min_cost[i-2])+cost[i]
        
        return self.step_min_cost[len(cost)-1]


        


if __name__ == '__main__':
    print(Solution().minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))

        