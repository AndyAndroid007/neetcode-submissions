class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        n = len(temperatures)
        i = 0
        final = [0]*n
        while i < n:
            if len(s) == 0:
                s.append(i)
            
            else:
                while s and temperatures[i] > temperatures[s[-1]]:
                    x = s.pop()
                    final[x] = i-x
                   

                s.append(i)
            i += 1
        return final
            

            


                
        

        

        