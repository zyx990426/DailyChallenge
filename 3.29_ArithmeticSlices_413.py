class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        
    # Approach1: Brute Force (Time: O(N^2)) 
        # count = 0
        # for s in range(0, len(nums) - 2):
        #     d = nums[s + 1] - nums[s]
        #     for e in range(s + 2, len(nums)):
        #         if nums[e] - nums[e - 1] == d:
        #             count += 1
        #         else:
        #             break
        # return count
        
    
    # Approach2: DP (Time: O(N))
        count = 0
        dp = [0] * len(nums)
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp[i] = dp[i - 1] + 1
            count += dp[i]
        return count