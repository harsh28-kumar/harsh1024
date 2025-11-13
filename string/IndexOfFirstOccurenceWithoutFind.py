class Solution(object)
def string(self, laystack,needle):
    
    n,m =len(laystack), len(needle)
    if n == 0:
        return 0
    
    for i in range(n-m+1):
        if laystack[i:i+1] == needle:
            return i
    
    return -1
    
obj = Solution
print(obj.strStr("sadbutsad","sad"))