class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(x):
            if len(x) == 1:
                return True
            left = 0
            right = len(x)-1
            while left <= right:
                if x[left] != x[right]:
                    return False
                left+=1
                right-=1
            return True
        
        def backtrack(arr, ind):
            if ind == len(s):
                final.append(arr.copy())
                return
            
            for i in range(ind,len(s)):
                x = s[ind:i+1]
                if isPalindrome(x):
                    arr.append(x)
                    backtrack(arr, i+1)
                    arr.pop()
        final = []
        backtrack([],0)
        return final
                
                
        