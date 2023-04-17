# Find the subarray withh maximium product and return the sum

# a = [3, 6, -1, -4, 2, 7]
# max prod possible is [3, 6] = 18

# if there are consecutive -ve numbers then their product will be positive
# so we need to keep track of max as well as min ans also check for the case whe# element is zero

class Solution:
    def maxProdSubArray(self, nums: list[int]) -> int:
        # set result varible to the largest element in the list
         
        currMin = currMax = res = nums[0]
       
        for i in range(1, len(nums)):
            # inclue nums[i] so we can reset when a 0 is encountered
            currMax = max(nums[i] * currMax, nums[i] * currMin, nums[i])
            currMin = min(nums[i] * currMax, nums[i] * currMin, nums[i])
            res = max(res, currMax)
        return res

nums = [-2, 0, -1]
print("Input", nums)
res = Solution().maxProdSubArray(nums)
print("Output- maximum product subarray = ", res)


