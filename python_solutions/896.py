class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        is_monotonic= True
        if nums is not None and len(nums)>0:
            previous_no=nums[0]
            previous_diff_trend=None
            for i in range(1,len(nums)):
                diff= previous_no- nums[i]
                previous_no= nums[i]
                if diff!=0:
                    if previous_diff_trend is None:
                        if diff>0:
                            previous_diff_trend =1
                        elif diff<0:
                            previous_diff_trend = - 1
                    else:
                        if diff>0 and previous_diff_trend<0:
                            is_monotonic = False
                            break
                        elif diff<0 and previous_diff_trend>0:
                            is_monotonic = False
                            break
        
        return is_monotonic

if __name__ == '__main__':
    print(Solution().isMonotonic([1,3,2]))