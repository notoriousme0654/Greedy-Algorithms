# 2. Lemonade Problem
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0] != 5:
            return False
        else:
            num_5 = 0
            num_10 = 0
            for i in range(len(bills)):
                if bills[i] == 5:
                    num_5 += 1
                    continue
                else:
                    change = bills[i] - 5
                    if change == 5:
                        num_5 -= 1
                        num_10 += 1
                    else:
                        num_5 -= 1
                        if num_10 != 0:
                            num_10 -= 1
                        else:
                            num_5 -=2
                    if num_5 < 0 or num_10 < 0:
                        return False
            return True
