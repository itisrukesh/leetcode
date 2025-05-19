class Solution:
    def romanToInt(self, s: str) -> int:
        # Roman Num Val Map:
        maps = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        
        num = 0
        prevVal = 0
        i = len(s)-1
        # Hint : Iterate over the string from back to front which make easier for us.
        while i >= 0:
            currVal = maps[s[i]]
            if currVal < prevVal:
                num -= currVal
                prevVal = currVal
                i -= 1
            else: 
                num += currVal
                prevVal = currVal
                i -= 1
        
        return num

if __name__ == '__main__':
    sol = Solution()
    # case 1:
    print(sol.romanToInt("III"))
    # case 2:
    print(sol.romanToInt("LVIII"))
    # case 3:
    print(sol.romanToInt("MCMXCIV"))