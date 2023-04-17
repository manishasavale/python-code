class solution:
    def findTwoSum(self, nums: list[int], target: int) -> list[int]:
        """
         nums: Input List
         target: given target sum of two numbers
         returns: list of two numbers whose sum equals target
        """
        map = {}
        for i, num in enumerate(nums):
            if num in map:
               return i, map[num]
            else:
               map[target - num] = i
        return None


a = [5, 3, 8, 1]
target = 4

print("Input", a)
print("Target", target)

result = solution().findTwoSum(a, target)
print("Result", result)
 
