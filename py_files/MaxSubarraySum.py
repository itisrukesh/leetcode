'''
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 
Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''

import sys
class Solution:
    def maxSubArray(self, nums) -> int:
        #optimal - Kadane's Algorithm - maximum subarray
        maxnum = -sys.maxsize-1
        sumval = 0
        for i in range(len(nums)):
            sumval += nums[i]
            if sumval > maxnum:
                maxnum = sumval
            if sumval < 0:
                sumval = 0
        return maxnum

    def bruteforce(self, nums) -> int:
        maxnum = - sys.maxsize - 1
        for i in range(len(nums)):
            sumval = 0
            for j in range(i,len(nums)):
                sumval += nums[j]
                maxnum = max(maxnum, sumval)
        return maxnum
    
if __name__ == '__main__':
    sol = Solution()
    #case 1:
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print("nums", nums)
    print(sol.bruteforce(nums))
    print(sol.maxSubArray(nums))
    
    #case 2:
    nums = [1]
    print("nums:",nums)
    print(sol.bruteforce(nums))
    print(sol.maxSubArray(nums))
    
    #case 3:
    nums = [5,4,-1,7,8]
    print("nums:", nums)
    print(sol.bruteforce(nums))
    print(sol.maxSubArray(nums))
    