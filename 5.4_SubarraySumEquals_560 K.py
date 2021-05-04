class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums or len(nums) == 0:
            return 0
        
#1. Hashmap (O(N))
    # sum of nums[i:j] = prefix of nums[0:j] - prefix of nums[0:i]
        dic = {0:1}
        count = 0
        prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            
            if prefix_sum - k in dic:
                count += dic[prefix_sum - k]
            
            if prefix_sum in dic:
                dic[prefix_sum] += 1
            else:
                dic[prefix_sum] = 1
                
        return count
                
        
        
        
        
#2. 前项和list with space (O(N^2))
#         prefix = [0] * len(nums)
#         prefix[0] = nums[0]
        
#         for i in range(1, len(nums)):
#             prefix[i] = prefix[i - 1] + nums[i]
            
#         count = 0
#         for m in range(len(prefix)):
#             if prefix[m] == k:
#                 count += 1
#             for n in range(m - 1, -1, -1):
#                 if prefix[m] - prefix[n] == k:
#                     count += 1
        
#         return count
            
        
#3. prefix without space (O(N^2))
#         count = 0
#         result = 0
#         for i in range(len(nums)):
            
#             result = nums[i]
#             if result == k:
#                 count += 1
                
#             for j in range(i + 1, len(nums)):
#                 result += nums[j]
#                 if result == k:
#                     count += 1
                    
#         return count
    