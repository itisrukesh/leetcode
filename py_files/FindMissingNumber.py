class Solution:
    def missingNumber(self, nums) -> int:
        #optimal solution
        xor1, xor2 = 0, 0
        for i in range(len(nums)):
            xor1 = xor1 ^ (i+1)
            xor2 = xor2 ^ nums[i]
        return xor1 ^ xor2

    def bruteforce_missingNumber(self, nums) -> int:
        #bruteforce
        nums.sort()
        n = len(nums)
        # adding plus one to consider the last value also. That is if list is [0,1], then len is 2. then we need to include the 2 as well. (to get [0,1,2] here 2 is missing number)
        for i in range(n + 1): 
            if i not in nums:
                return i
    
    def better_missingNumber(self, nums) -> int:
        #better approach
        n = len(nums)
        expected_sum = n*(n+1)/2
        return int(expected_sum - sum(nums))

if __name__ == '__main__':
    
    sol = Solution()
    
    print("BruteForce:")
    #case1:
    nums = [0,1,3]
    print(sol.bruteforce_missingNumber(nums))
    #case2:
    nums = [0,1]
    print(sol.bruteforce_missingNumber(nums))
    #case3:
    nums = [9,6,4,2,3,5,7,0,1]
    print(sol.bruteforce_missingNumber(nums))
    
    print("Better solution:")
    #case1:
    nums = [0,1,3]
    print(sol.better_missingNumber(nums))
    #case2:
    nums = [0,1]
    print(sol.better_missingNumber(nums))
    #case3:
    nums = [9,6,4,2,3,5,7,0,1]
    print(sol.better_missingNumber(nums))
    
    print("optimal solution:")
    #case1:
    nums = [0,1,3]
    print(sol.missingNumber(nums))
    #case2:
    nums = [0,1]
    print(sol.missingNumber(nums))
    #case3:
    nums = [9,6,4,2,3,5,7,0,1]
    print(sol.missingNumber(nums))