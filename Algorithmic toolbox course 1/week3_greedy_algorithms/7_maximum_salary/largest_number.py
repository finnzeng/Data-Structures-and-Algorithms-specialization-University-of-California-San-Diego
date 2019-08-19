#Uses python3

import sys

def IsGreaterOrEqual(digit, max_digit):
    '''check both the combinations digit_max_digit and max_digit_digit'''
    return int((digit)+(max_digit))>=int((max_digit)+(digit))

    
def largest_number(a):
    result = []
    
#     a = sorted(a, key = lambda x: int(x[0]), reverse=True)
    while a:
        max_digit = '0'
        for digit in a:
            if IsGreaterOrEqual(digit, max_digit):
                max_digit = digit
        result.append(max_digit)
        a.remove(max_digit)

    res = ""
    for x in result:
        res += x
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
