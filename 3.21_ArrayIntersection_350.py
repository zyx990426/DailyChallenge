class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) == 0 or len(nums2) == 0:
            return []

        if len(nums1) >= len(nums2):
            dic = self.createhash(nums1)
            use = nums2
        else:
            dic = self.createhash(nums2)
            use = nums1
        
        output = []
        for i in use:
            if i in dic and dic[i] > 0:
                output.append(i)
                dic[i] -= 1
        return output
                

    
    def createhash(self, nums):
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        return dic