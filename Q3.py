# 3. Check if possible to survive on island

import math
def can_survive(N, S, M):
    total_food_required = S * M
    
    buying_days = S - (S // 7)
    
    if M > N or total_food_required > buying_days * N:
        return "No, survival is not possible."
    
    min_days = math.ceil(total_food_required / N)
    
    return f"Yes, survival is possible. Minimum days to buy food: {min_days}"

N = 16  
S = 10 
M = 2 

print(can_survive(N, S, M))
