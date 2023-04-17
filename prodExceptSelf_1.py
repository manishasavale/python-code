class Solution:
    def prodExceptSelf(self, nums:list[int]) -> list[int]:
        result = []
        for num in nums:
            c = 1
            for i, n in enumerate(nums):
                if(n != num ):
                     c = c * nums[i]
                     print("c",c)
            result.append(c)
        return result

a = [1, 2, 3, 4]
print("Input:", a)
result = Solution().prodExceptSelf(a)
print("Output", result)




