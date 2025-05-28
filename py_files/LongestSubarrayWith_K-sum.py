class Solution():

    #BruteForce solution
    def getLongestSubarray(self, nums, k) -> int:
        lenval = 0
        for i in range(len(nums)):
            sumval = 0
            for j in range(i, len(nums)):
                sumval += nums[j]
                if sumval == k:
                    lenval = max(lenval, j-i+1)
        
        return lenval

if __name__ == '__main__':
    
    sol = Solution()
    #case 1:
    nums = [1,2,1,0,1]
    k = 4
    print(sol.getLongestSubarray(nums, k))
    #case 2:
    nums = [2,3,5]
    k = 5
    print(sol.getLongestSubarray(nums, k))
    #case 3:
    nums = [1,-1,1]
    k = 1
    print(sol.getLongestSubarray(nums, k))