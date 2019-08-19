# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
#         print('now',a[left])
        return a[left]
#     print('call 1')
    left_elem = get_majority_element(a, left, (left+right+1)//2)
#     print('call 2')
    right_elem = get_majority_element(a, (left+right+1)//2, right)

    lcount = 0
#     print('left_elem',left_elem)
#     print('right_elem',right_elem)
    for i in range(left, right):
        if a[i] == left_elem:
            lcount += 1
    if lcount > (right - left) // 2:
        return left_elem

    rcount = 0
    for i in range(left, right):
        if a[i] == right_elem:
            rcount += 1
    if rcount > (right - left) // 2:
        return right_elem

    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
