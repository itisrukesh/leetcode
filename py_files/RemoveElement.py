
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        #brute force:
        ls = []

        for i in nums:
            if i == val:
                continue
            else: ls.append(i)
        
        for i in range(len(ls)):
            nums[i] = ls[i]
        
        return len(ls), nums
    
    def optimalRemoveElement(self, nums: list[int], val: int) -> int:
        # optimal - Two Pointer
        k = 0 # k is tracker for index to achieve IN-Place
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k+=1

        return k, nums 

if __name__ == '__main__':
    
    sol = Solution()
    # case 1:
    nums = [3,2,2,3]
    val = 3
    print(sol.removeElement(nums, val))
    # case 2:
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    print(sol.removeElement(nums, val))
    
    #optimal solution tryout:
    # case 1:
    nums = [3,2,2,3]
    val = 3
    print(sol.optimalRemoveElement(nums, val))
    # case 2:
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    print(sol.optimalRemoveElement(nums, val))