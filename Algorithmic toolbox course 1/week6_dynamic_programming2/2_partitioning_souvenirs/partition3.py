# Uses python3
import sys
import itertools


def solution(arr):
    import numpy as np
    total = sum(arr)
    if len(arr) < 3 or total % 3:
        return 0
    per_person = total // 3
#     dp = [[0] * (len(arr) + 1) for _ in range(per_person + 1)] #create a matrix for dp solution
    dp = np.zeros((per_person+1,len(arr)+1))

    for i in range(1, per_person+1): # variable for sum
        for j in range(1, len(arr)+1): #variable for values given as input
            ii = i - arr[j - 1]     # as i is iterative variable from per_person, it will sometime be equal to or bigger than arr[j-1], else it will not be possible to partition
            if arr[j - 1] == i or (ii > 0 and dp[ii][j - 1]): # arr[j-1] is contributing to the sum
                # dp[ii][j-1] is already calculated, if dp[i-arr[j-1]][j-1] is something worthy to contribute to sum but not 0
                dp[i][j] = 1 if dp[i][j - 1] == 0 else 2 # if dp[i][j-1]==0, it means nothing till j-1 items were included in it.
                # 1 and 2 for saying 1 or 2 subsets have been found with subset sum equal to per_person, finding 2 basically means finding 3
            else: #if arr[i][j-1] doesn't contirbute just take prev value
                dp[i][j] = dp[i][j - 1]

#     print(dp)
    return 1 if dp[-1][-1] == 2 else 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
#     print(partition3(A))
    print(solution(A))

    
# def partition3(A):
#     for c in itertools.product(range(3), repeat=len(A)):
#         sums = [None] * 3
#         for i in range(3):
#             sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

#         if sums[0] == sums[1] and sums[1] == sums[2]:
#             return 1

#     return 0
# def solution(arr):
#     total = sum(arr)
#     if len(arr) < 3 or total % 3:
#         return 0
#     per_person = total // 3
#     dp = [[0] * (len(arr) + 1) for _ in range(per_person + 1)] #create a matrix for dp solution

#     for i in range(1, per_person + 1):
#         for j in range(1, len(arr) + 1):
#             ii = i - arr[j - 1]
#             if arr[j - 1] == i or (ii > 0 and dp[ii][j - 1]):
#                 dp[i][j] = 1 if dp[i][j - 1] == 0 else 2
#             else:
#                 dp[i][j] = dp[i][j - 1]

#     return 1 if dp[-1][-1] == 2 else 0

