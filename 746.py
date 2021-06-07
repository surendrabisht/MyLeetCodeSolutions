class Solution:
    def __init__(self) -> None:
        self.step_min_cost=[]

    def minCostClimbingStairs(self, cost: list[int]) -> int:
        cost.append(0)
        self.step_min_cost=[-1]*len(cost)
        self.step_min_cost[0]=cost[0]
        self.step_min_cost[1]=cost[1]
        minimum_cost=self.recursive_find_min(cost,len(cost)-1)
        return minimum_cost


    def recursive_find_min(self,cost: list[int],step_no:int):
        if self.step_min_cost[step_no]==-1:
            cost_from_second_last_Step=self.recursive_find_min(cost,step_no-2)
            cost_from_last_step=self.recursive_find_min(cost,step_no-1)
            self.step_min_cost[step_no]=min(cost_from_second_last_Step,cost_from_last_step) +cost[step_no]

        return self.step_min_cost[step_no]


        


if __name__ == '__main__':
    print(Solution().minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))

        