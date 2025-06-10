'''
75. Sort Colors
Solved
Medium

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]

Constraints:
n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.'''

class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #optimal - Dutch National Flag Algorithm:
        low = mid = 0
        high = len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

    
    def bruteforce(self, nums) -> None:
        i = 1
        while i < len(nums):
            while nums[i] < nums[i-1] and i != 0:
                nums[i-1], nums[i] = nums[i], nums[i-1]
                i -= 1
            i += 1
            
if __name__ == '__main__':
    
    sol = Solution()
    #case 1: 
    nums = [2,0,1]
    print("nums:",nums, end="")
    sol.bruteforce(nums)
    print("\tBruteForce Ans:", nums)
    nums = [2,0,2,1,1,0]
    print("nums:",nums, end="")
    sol.sortColors(nums) #optimal
    print("\toptimal Ans:", nums)