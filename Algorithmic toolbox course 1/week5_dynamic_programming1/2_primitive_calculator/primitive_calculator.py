# Uses python3
import sys

# def optimal_sequence(n):
#     sequence = []
#     while n >= 1:
#         sequence.append(n)
#         if n % 3 == 0:
#             n = n // 3
#         elif n % 2 == 0:
#             n = n // 2
#         else:
#             n = n - 1
#     return reversed(sequence)

def dp_solution(n):
    operations_count = [0] * (n + 1)

    operations_count[1] = 1
    for i in range(2, n + 1):
        count_index = [i - 1] #the worst case where i have to add 1 all the time, so index of prev number
        if i % 2 == 0:
            count_index.append(i // 2)   # steps to i//2 times +1, so index of i//2
        if i % 3 == 0:
            count_index.append(i // 3) # steps to i//3 + 1, so index of i//3

        operations_count[i] = min([operations_count[x] for x in count_index]) +1 # previous values are already counted. 
                                                                             #so see which one is min and add 1 to it

    current_value = n
    intermed_numbers = [current_value]
    while current_value != 1: #until the value we are looking at is 1
        option_list = [current_value - 1] #possibilty of coming from prev number
        if current_value % 2 == 0:    #possibility of arriving from current_value//2
            option_list.append(current_value // 2)
        if current_value % 3 == 0:     #possibility of arriving from current_value//3
            option_list.append(current_value // 3)

        current_value = min([(c, operations_count[c]) for c in option_list],key=lambda x: x[1])[0] #choose the one with min 
                                                                        #operations as everything reaches to n with 1 step. 
        intermed_numbers.append(current_value)
    return reversed(intermed_numbers)


input = sys.stdin.read()
n = int(input)
sequence = list(dp_solution(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
