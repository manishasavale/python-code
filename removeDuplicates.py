
#from typing import List

#Remove duplicate elements from a given array

#Use a hashset and put each number in the hashset after making sure it 
#doesn't alreay presesnt. If present, you have duplicates

class Solution:
    def __init__(self):
        pass
    
    def containsDuplicate(self, nums: list[int]) -> bool:
       hashset = set()

       for n in nums:
           if n in hashset:
               return True
           hashset.add(n)
       return False
 

a = [1, 5, 3, 8, 3]
print("Input", a)
print(Solution().containsDuplicate(a)) 
