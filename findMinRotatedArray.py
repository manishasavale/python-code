# Find minimum element in a rotated sorted array
# we use a binary search approach

class Solution:
    def findMin(self, nums:list[int]) -> int:
        res = nums[0]
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break

            mid = (left + right) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        return res


nums = [5,6,7,1,3,4]
print("Input", nums)
result = Solution().findMin(nums)
print("Minimum element = ", result)



