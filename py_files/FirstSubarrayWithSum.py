'''Given an array arr[] containing only non-negative integers, your task is to find a continuous subarray (a contiguous sequence of elements) 
whose sum equals a specified value target. You need to return the 1-based indices of the leftmost and rightmost elements of this subarray. 
You need to find the first subarray whose sum is equal to the target.

Note: If no such array is possible then, return [-1].

Examples:

Input: arr[] = [1, 2, 3, 7, 5], target = 12
Output: [2, 4]
Explanation: The sum of elements from 2nd to 4th position is 12.
Input: arr[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], target = 15
Output: [1, 5]
Explanation: The sum of elements from 1st to 5th position is 15.
Input: arr[] = [5, 3, 4], target = 2
Output: [-1]
Explanation: There is no subarray with sum 2.
Constraints:
1 <= arr.size()<= 106
0 <= arr[i] <= 103
0 <= target <= 109
'''

#User function Template for python3
class Solution:
    def Optimal_subarraySum(self, arr, target):
        # optimal approach Time complexity = O(n) , space complexity = O(1)
        left = 0
        right = 0
        sumval = 0
        n = len(arr)-1
        
        while right <= n:
            sumval += arr[right]
            
            while sumval > target and left <= right:
                sumval -= arr[left]
                left+=1
            if sumval == target:
                return [left+1, right+1]
            
            right += 1
        
        return [-1]
    
    def BruteForce_subarraySum(self, arr, target):
        #bruteforce Time complexity = O(n^2) , space complexity = O(1)
        for i in range(len(arr)):
            sumval = 0
            for j in range(i, len(arr)):
                sumval += arr[j]
                if sumval == target:
                    return [i+1, j+1]
        
        return [-1]
    
if __name__ == '__main__':
    
    sol = Solution()
    
    # case 1
    arr1 = [1, 2, 3, 7, 5]
    target1 = 12
    
    # case 2
    arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target2 = 15
    
    # case 3
    arr3 = [5,6,10]
    target3 = 7
    
    # case 1 :  
    print(sol.BruteForce_subarraySum(arr1, target1))
    
    # case 2 :
    print(sol.BruteForce_subarraySum(arr2, target2))
    
    #case 3 :
    print(sol.BruteForce_subarraySum(arr3, target3))
    
    # case 1
    print(sol.Optimal_subarraySum(arr1, target1))
    
    # case 2
    print(sol.Optimal_subarraySum(arr2, target2))
    
    #case 3 :
    print(sol.Optimal_subarraySum(arr3, target3))
    
    
                