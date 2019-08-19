# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    values = [float(values[i])/float(weights[i]) for i in range(len(values))]
    aka = sorted(values,reverse = True)
    filled = 0
    answer = 0
    i = 0
    weights = [weights[values.index(aka[i])] for i in range(len(values))]
#     print(aka,'\t', weights)
    values = aka
    while filled<capacity and i<len(values):
        if weights[i]+filled>capacity:
#             print('yay', filled)
            return answer+ (values[i]*(capacity-filled))
        else:
            answer += values[i]*weights[i]
            filled+=weights[i]
#             print('yee',filled)
            i+=1
    return answer


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
