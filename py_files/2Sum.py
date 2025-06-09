class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """            
        #optimal approach
        maps = dict()
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in maps:
                return [maps[rem], i]
            else: maps[nums[i]] = i 

    def bruteforce(self, nums, target):
        for i in range(len(nums)):
            checkval = target - nums[i]
            if checkval in nums:
                j = nums.index(checkval) 
                if j != i:return i,j 


if __name__ == '__main__':
    
    sol = Solution()
    #case:
    nums = [3,2,4]
    target = 6
    print(sol.twoSum(nums, target))