from collections import Counter
class Solution:
    def majorityElement(self, nums) -> int:
        #optimal approach - Moore's Voting Algorithm
        elem = nums[0]
        count = 0
        for i in range(len(nums)):
            if count == 0:
                elem = nums[i]
            if nums[i] == elem: count += 1
            else: count -= 1
        return elem

    def bruteforce(self, nums) -> int:
        #bruteforce - time limit will exceeds
        for i in range(len(nums)):
            element = nums[i]
            count = 0
            for j in range(len(nums)):
                if nums[j] == element:
                    count+=1
                if count > (len(nums) // 2):
                    return element

    def better_approach(self, nums) -> int:
        freqMap = Counter(nums)
        maxval = max(freqMap.values())
        for key, val in freqMap.items():
            if val == maxval:
                return key
            
    def sorting_approach(self, nums) -> int:
        '''
        Once the array is sorted, the majority element will always be present at index n/2
        where n is the size of the array. This is because the majority element occurs more 
        than n/2 times, and when the array is sorted, it will occupy the middle position.
        The code returns the element at index n/2 as the majority element.
        '''
        nums.sort()
        return nums[len(nums)//2]
    
if __name__ == '__main__':
    
    sol = Solution()
    
    nums = [2,2,1,1,1,2,2]
    print("nums:", nums)
    print("bruteForce:",sol.bruteforce(nums))
    print("Better_approach:", sol.better_approach(nums))
    print("optimal_approach:", sol.majorityElement(nums))

    arr = [2,2,1,1,1,2,2]
    print("arr:", arr)
    print("Sorting-Return arr[n/2]:", sol.sorting_approach(arr))
    print("arr afterSorting:", arr)