# Uses python3
import sys

def gcd_naive(a, b):
    m = max(a,b)
    n = min(a,b)
    if m%n ==0 :
        return n
    
    return gcd_naive(n,m%n)

def lcm_naive(a, b):
    n = min(a,b)
    if n ==0:
        return 0
    return int((a*b)/gcd_naive(a,b))
#     for l in range(1, a*b + 1):
#         if l % a == 0 and l % b == 0:
#             return l

#     return a*b

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

