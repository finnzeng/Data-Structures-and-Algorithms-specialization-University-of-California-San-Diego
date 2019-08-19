# Uses python3
import sys

# table = [0]*(n+1)
# for i in [0,1]:
#     table[i] = i
def get_fibonacci_last_digit_naive(n):
#     for i in range(2,n+1):
#         temp =  table[i-1]+table[i-2]
#         table[i] = temp%10
#     return table[n]
    
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current)%10

    return current

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
