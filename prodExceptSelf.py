class Solution:
    def prodExceptSelf(self, nums: list[int]) -> list[int]:
        result = [1] * (len(nums))

        prefix = 1
        #calculate prefix product for the list from 0 to n-1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        print("prefix", result)
        postfix = 1
        # trevese the list in reverse order
        # while updating the result, using the prefix products
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
            print("updating i, result ", i, result[i])
            print("postfix", postfix)
        return result


a = [1, 2, 3,4]
print("Input", a)
result = Solution().prodExceptSelf(a)
print("Output", result)
            
