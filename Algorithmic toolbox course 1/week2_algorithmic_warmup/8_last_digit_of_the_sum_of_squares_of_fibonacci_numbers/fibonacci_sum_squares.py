# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10
def fibonacci(n):
    if n<2:
        return n
    prev,curr = 0,1
    for i in range(n-1):
        prev, curr = curr, (curr+prev)%10
    return curr

square_digits = [0]*10
for i in range(10):
    square_digits[i] = (i*i)%10
square_digits = dict(zip(list(range(10)),square_digits))

def sum_squares_period60():
    square_digits = [0]*10
    for i in range(10):
        square_digits[i] = (i*i)%10
    square_digits = dict(zip(list(range(10)),square_digits))
    summ = 0
    for i in range(60):
        summ = (summ+square_digits[fibonacci(i)])%10
    return summ

def fibonacci_squares(n):
    if n<2:
        return n
    prev, curr, summ = 0,1,1
    num_time_periods = n//60
    n%=60
    square_digits = [0]*10
    for i in range(10):
        square_digits[i] = (i*i)%10
    square_digits = dict(zip(list(range(10)),square_digits))
    
    if n<2:
        return (num_time_periods*sum_squares_period60() + n)%10
    for i in range(n-1):
        prev,curr = curr, (prev+curr)%10
        summ = (summ+square_digits[curr])%10
    return (summ +num_time_periods*sum_squares_period60())%10


if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_squares(n))
