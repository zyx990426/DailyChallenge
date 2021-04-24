class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        result = []
        
        left, right = 0, 0
        while left < len(nums1) and right < len(nums2):
            if nums1[left] == nums2[right] and nums1[left] not in result:
                result.append(nums1[left])
                left += 1
                right += 1
            elif nums1[left] > nums2[right]:
                right += 1
            elif nums1[left] < nums2[right]:
                left += 1
            else:
                left += 1
                right += 1
                
        return result