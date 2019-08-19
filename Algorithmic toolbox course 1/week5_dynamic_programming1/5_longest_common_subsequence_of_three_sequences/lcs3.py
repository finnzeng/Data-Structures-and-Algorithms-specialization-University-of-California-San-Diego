#Uses python3

import sys

def lcs3(a,b,c):
    import numpy as np
    dp = np.zeros((len(a)+1, len(b)+1, len(c)+1)) #keep a matrix of size len(a)+1 and len(b)+1 first row and first column has 0s only as there is no matching at all. we use it for next rows and columns
    
    for i,num1 in enumerate(a):   #enumerate for index and values of both arrays, note that I am starting from index 0 but adding it as dp[i+1]dp[j+1]
        for j,num2 in enumerate(b):
            for k,num3 in enumerate(c):
                if num1 == num2 == num3:  # if numbers match, common sequence length increases by 1
                    dp[i+1][j+1][k+1] = dp[i][j][k]+1
#                     print(dp[i+1][j+1][k+1])
                else:  #else just take the max of the square just above or just left
                    dp[i+1][j+1][k+1] = max([dp[i+1][j+1][k],dp[i][j+1][k+1],dp[i+1][j][k+1]])
#                     print('here',dp[i+1][j+1][k+1], ([dp[i+1][j][k],dp[i][j+1][k],dp[i][j][k+1]]))
    return int(dp[len(a)][len(b)][len(c)])
#     return (int(dp[-1][-1][-1]),dp)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
