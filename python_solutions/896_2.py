class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        is_monotonic = True
        if nums is not None and len(nums) > 0:
            previous_no = nums[0]
            previous_trend = None
            for i in range(1, len(nums)):
                diff = previous_no - nums[i]
                if diff == 0:
                    continue
                trend = 1 if diff > 0 else -1
                if previous_trend is not None and previous_trend != trend:
                    is_monotonic = False
                    break
                previous_no = nums[i]
                previous_trend = trend
        return is_monotonic


if __name__ == '__main__':
    print(Solution().isMonotonic([1, 3, 2]))
