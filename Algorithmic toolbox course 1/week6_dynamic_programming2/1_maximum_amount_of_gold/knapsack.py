# Uses python3
import sys

import numpy as np
def optimal_weight(W, w):
    # write your code here
#     result = 0
#     for x in w:
#         if result + x <= W:
#             result = result + x
#     return result
    
    weights = [0]
    for item in w:
        if item <= W:
            weights.append(item)

    item_length = len(weights)
    capacity = W + 1

    values = [[0 for _ in range(item_length)] for _ in range(capacity)] #here values[i][j] represents the maximum gold I have
                                        #filled till capacity i with first j items

    for j in range(1, item_length):
        for i in range(1, capacity):
            previous = values[i][j - 1]
            current = weights[j] + values[i - weights[j]][j - 1]
            if current > i: #it doesn't fit in the sack
                values[i][j] = previous
            else: #it does fit in the sack. so take max
                values[i][j] = max(previous, current)

    return values[-1][-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))