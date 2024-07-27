# 1. You are given an array of integers and an integer k. Your task is to select k elements from the array such that their sum is maximized?

def max_sum_k_elements(arr, k):
    sorted_arr = sorted(arr, reverse=True)
    max_elements = sorted_arr[:k]
    max_sum = sum(max_elements)
    return max_sum

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
k = 3
print(max_sum_k_elements(arr, k))
