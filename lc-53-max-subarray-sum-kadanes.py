class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        currSum = 0
        maxSum = float("-inf")

        for x in nums:
            currSum += x
            maxSum = max(currSum, maxSum)

            if currSum < 0:
                currSum = 0
        
        return maxSum


        
