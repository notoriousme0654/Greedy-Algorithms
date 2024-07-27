# Fractional knapsack

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
class Solution:    
    def fractionalknapsack(self, w,arr,n):
        valPerUnitWeight=[[item.value/item.weight,item.value,item.weight] for item in arr]
        valPerUnitWeight.sort(reverse=True)
        totalVal=0
        for i in range(n):
            if valPerUnitWeight[i][2]<=w:
                totalVal+=valPerUnitWeight[i][1]
                w-=valPerUnitWeight[i][2]
            else:
                totalVal+=(w*(valPerUnitWeight[i][0]))
                return totalVal
        return totalVal
