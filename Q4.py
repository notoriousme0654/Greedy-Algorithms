# 4. Shortest Job Fisrt

class Solution:
    def solve(self, bt):
        bt.sort()
        time = 0
        ans = 0
        for i in bt:
            ans += time
            time += i
        return ans//len(bt)
