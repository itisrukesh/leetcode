
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # python library based solution
        return haystack.find(needle)
    
    def mannualCheck_strStr(self, haystack: str, needle: str)-> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

if __name__ == '__main__':
    sol = Solution()
    #case 1:
    hs = "sadbutsad"
    n = "sad"
    print(sol.strStr(hs, n))
    
    #case 2:
    hs = "leetcode"
    n = "leeto"
    print(sol.strStr(hs, n))
    
    #case 1:
    hs = "sadbutsad"
    n = "sad"
    print(sol.mannualCheck_strStr(hs, n))
    
    #case 2:
    hs = "leetcode"
    n = "leeto"
    print(sol.mannualCheck_strStr(hs, n))
    
    