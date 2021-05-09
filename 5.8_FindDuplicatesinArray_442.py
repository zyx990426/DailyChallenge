class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
    
# Approach 1: hashmap (O(N), O(N))
        # c = collections.Counter(nums)
        # result = []
        # for i in c:
        #     if c[i] == 2:
        #         result.append(i)
        # return result
    
# Approach 2: pointer (O(N), O(1)) 找nums[i] 和 nums[nums[i] - 1] 之间的关系， 用相反数标记
        result = []
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] < 0:
                result.append(abs(nums[i]))
            nums[abs(nums[i]) - 1] *= -1
        return result
    
        