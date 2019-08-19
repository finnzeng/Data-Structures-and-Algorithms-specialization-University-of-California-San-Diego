# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    sum1 = 0

    current = 0
    nex  = 1

    for i in range(to + 1):
        if i >= from_:
            sum1 = (sum1 + current)%10

        current, nex = nex, (current + nex)%10

    return sum1 


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))