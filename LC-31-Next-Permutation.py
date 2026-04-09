'''
    Problem: https://leetcode.com/problems/next-permutation/description/
'''

class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        idx = -1
        # find the dip
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                idx = i
                break

        # edge case: when it's the biggest element like fully sorted
        if idx == -1:
            # remains -1 just rev the whole array
            return nums.reverse()

        # find the element JUST greater than the A_idx
        for i in range(n-1, idx, -1):
            if nums[i] > nums[idx]:
                # swap
                nums[i], nums[idx] = nums[idx], nums[i]
                break

        # for the last part
        l, r = idx+1, n-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

