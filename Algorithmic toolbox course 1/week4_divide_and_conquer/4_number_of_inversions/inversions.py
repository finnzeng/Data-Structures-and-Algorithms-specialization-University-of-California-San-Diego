# Uses python3
import sys

# def get_number_of_inversions(a, b, left, right):
#     number_of_inversions = 0
#     if right - left <= 1:
#         return number_of_inversions
#     ave = (left + right) // 2
#     number_of_inversions += get_number_of_inversions(a, b, left, ave)
#     number_of_inversions += get_number_of_inversions(a, b, ave, right)
#     #write your code here
#     return number_of_inversions

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     n, *a = list(map(int, input.split()))
#     b = n * [0]
#     print(get_number_of_inversions(a, b, 0, len(a)))
# Uses python3
import sys

def get_num_of_inv_mid(a,b,left,mid,right):
    #left and right are already sorted
#     print('left',left,'mid',mid,'right',right)
    num_of_inv = 0
    i = left
    j = mid
    curr = left
    while i<(mid) and j<right+1:
        if a[i]<a[j]:
            b[curr] = a[i]
            i+=1
        else:
            b[curr] = a[j]
            j+=1
            num_of_inv += (mid-i-1)
#             print('\n',num_of_inv)
        curr+=1
    while i< mid:
        b[curr] = a[i]
        i+=1
        curr+=1
    while j<right+1:
#         print(curr)
        b[curr] = a[j]
        j+=1
        curr+=1
    for i in range(left,right):
        a[i] = b[i]
    return num_of_inv

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
#     if right - left <= 1:
#         return number_of_inversions
    if right>left:
        ave = (left + right) // 2
        number_of_inversions += get_number_of_inversions(a, b, left, ave)
#         print(number_of_inversions,'this1')
        number_of_inversions += get_number_of_inversions(a, b, ave+1, right)
#         print(number_of_inversions,'this2')
        number_of_inversions += get_num_of_inv_mid(a,b,left,ave+1,right)
#         print(number_of_inversions,'this3')
        #write your code here
    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)-1))
