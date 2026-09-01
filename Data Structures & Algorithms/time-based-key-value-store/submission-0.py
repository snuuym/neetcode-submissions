class TimeMap:

    def __init__(self):
        #the structure
        self.store = {} #every key follows a list of lists as[value, timestamp]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        
        res = ""
        if key not in self.store:
            return res
        #since all the timestamps are strictly increasing, use binary search
        values = self.store[key]
        l, r = 0, len(values)-1
        while l<=r:
            m = (l+r)//2
            if values[m][1] == timestamp:
                return values[m][0]
            elif values[m][1] > timestamp:
                r = m-1
            else:
                res = values[m][0] #this is the closest one so far, update the result.
                l = m+1


        return res
        
