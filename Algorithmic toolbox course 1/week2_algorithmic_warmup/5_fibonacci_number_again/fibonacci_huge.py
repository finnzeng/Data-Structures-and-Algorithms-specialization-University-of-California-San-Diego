# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    curr, prev = 1,0
    for i in range(m*m+1):
#         print(i)
        prev,curr =  curr, (curr+prev)%m
        if (prev, curr) == (0,1):
            time_period = i+1
#             print('here',time_period)
            break
        
    index = n%time_period
#     print(index)
    if index<1:
        return index
    prev,curr = 0,1
    for i in range(2, index+1):
        prev,curr = curr, (curr+prev)%m
    return curr

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
