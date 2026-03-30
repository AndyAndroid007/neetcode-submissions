class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            t1 = target - numbers[i]
            j = n-1
            while i < j:
                if numbers[j] < t1:
                    i+=1
                    break
                elif numbers[j] == t1:
                    return [i+1,j+1]
                else:
                    j-=1
                



        