class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''  
            Author: Pritam
        ''' 
        '''  
        Problem: https://leetcode.com/problems/sort-colors/description/
        Technique: Two pointer
        Intuition: we know that, 0 will be at the start and 2 will be at the end, so the only place remains is 1
        Mistake: 
        Time: 
        Space: 
        '''    
        n = len(nums)

        l, r = 0, n-1
        mid = 0

        while mid <= r:
            if nums[mid] == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                mid += 1
            elif nums[mid] == 2:
                nums[r], nums[mid] = nums[mid], nums[r]
                r -= 1
            else:
                mid += 1
        return nums
            
        
        
    