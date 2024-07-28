# 13. Insert interval

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals)==0:
            return [newInterval]
        idx = None
        for i in range(len(intervals)):
            if intervals[i][0]<newInterval[0]:
                continue
            else:
                idx = i
                break
        if idx is None:
            intervals.append(newInterval)
        else:
            intervals.insert(idx, newInterval)
        ret = []
        for i in range(len(intervals)):
            if len(ret)==0:
                ret.append(intervals[i])
                continue
            if ret[-1][1]>=intervals[i][0]:
                ret[-1][1] = max(ret[-1][1], intervals[i][1])
            else:
                ret.append(intervals[i])
        return ret
