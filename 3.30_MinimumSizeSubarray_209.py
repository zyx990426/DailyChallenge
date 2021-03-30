class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
  #Approach1: Two Pointers (O(N))
  #需要定义两个指针 left 和 right，分别记录子数组的左右的边界位置，然后让 right 向右移，直到子数组和大于等于给定值或者 right 达到数组末尾，此时更新最短距离，并且将 left 像右移一位，然后再 sum 中减去移去的值，然后重复上面的步骤，直到 right 到达末尾，且 left 到达临界位置，即要么到达边界，要么再往右移动，和就会小于给定值
    
        s, e, subsum = 0, 0, 0
        minimum_length = sys.maxsize
        n = len(nums)
        
        while e < n:
            while e < n and subsum < target:
                subsum += nums[e]
                e += 1
            
            while s < n and subsum >= target:
                minimum_length = min(minimum_length, e - s)
                subsum -= nums[s]
                s += 1
                
        if minimum_length == sys.maxsize:
            return 0
        return minimum_length
 


 # Approach2: BruteForce (O(N^2))
#         minimum_length = sys.maxsize
#         flag = False
#         for s in range(len(nums)):
#             for e in range(s + 1, len(nums) + 1):
#                 sub = nums[s : e]
#                 if sum(sub) >= target and len(sub) < minimum_length:
#                     minimum_length = len(sub)
#                     flag = True
#                     break
                
#         if flag: 
#             return minimum_length
#         return 0