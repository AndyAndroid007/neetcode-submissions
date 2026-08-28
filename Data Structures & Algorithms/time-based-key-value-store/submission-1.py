class TimeMap:

    def __init__(self):
        self.timeMap = dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = [(timestamp,value)]
        self.timeMap[key].append((timestamp,value))
        return


    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.timeMap:
            return ""
        
        arr = self.timeMap[key]
        left = 0 
        right = len(arr)-1
        ans = ""
        while left <= right:
            mid = (left + right)//2
            
            if arr[mid][0] <= timestamp:
                ans = arr[mid][1]
                left = mid+1
            else:
                right = mid-1
        return ans
        
