# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def min_max(Mx, mn, i, j, operations):
    import math
    min_value = math.inf
    max_value = -math.inf
    for k in range(i, j):
        a = evalt(Mx[i][k], Mx[k+1][j], operations[k]) 
        b = evalt(Mx[i][k], mn[k+1][j], operations[k])
        c = evalt(mn[i][k], Mx[k+1][j], operations[k])
        d = evalt(mn[i][k], mn[k+1][j], operations[k])
        min_value = min(min_value, a, b, c, d)
        max_value = max(max_value, a, b, c, d)
    return min_value, max_value


def get_maximum_value(dataset):
    numbers, operations = list(map(int,dataset[::2])),dataset[1::2] # get numbers and operations from provided string input
    n = len(numbers)
    # two matrices store minimum and maximum numbers
    mn = [[None for x in range(n)] for x in range(n)]
    Mx = [[None for x in range(n)] for x in range(n)]

    for i in range(n):
        mn[i][i] = numbers[i]
        Mx[i][i] = numbers[i]

    #calculate only half part of the matrix, the upper part
    for s in range(1, n):
        for i in range(n-s):
            j = i + s
            mn[i][j], Mx[i][j] = min_max(Mx, mn, i, j, operations) #find min and max from min_max function

    return Mx[0][n-1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
