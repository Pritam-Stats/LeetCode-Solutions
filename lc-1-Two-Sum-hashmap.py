'''  
    Author: Pritam
''' 
'''  
Problem: https://leetcode.com/problems/two-sum/description/
Technique: hashmap
Intuition: keep track of seen
Mistake: none
Time: O(n)
Space: O(1)
''' 

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, x in enumerate(nums):
            complement = target - x
            if complement in seen:
                return [i, seen[complement]]
            seen[x] = i


        