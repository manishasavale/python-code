#Function that finds the subarray with the largest sum
# and returns the sum
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
#Explanation: The subarray [4,-1,2,1] has the largest sum 6.


#Solution is to use kadane's algorithm 
# the max subarray at an index i is either x where is is the element at index i
# or m where m is the max subarray at prev index


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        globalSum = nums[0]
        maxSum = nums[0]
      
        for i in range(1,len(nums)):
            maxSum = max(nums[i], (maxSum + nums[i]))
            print("maxSum", maxSum)
            if( maxSum > globalSum):
                globalSum = maxSum
                print("globalSum", globalSum)
        return globalSum


a = [-2, 3, 2, -1]
print("Input", a)
sum = Solution().maxSubArray(a)
print("The maximum subarray sum =", sum)


 
