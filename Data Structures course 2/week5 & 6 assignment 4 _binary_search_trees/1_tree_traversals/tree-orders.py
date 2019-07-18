# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
#         self.n = int(input())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
#             [a, b, c] = map(int, input().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self):
        cur_id = 0
        stack = []

        while True:
            if cur_id != -1:
                stack.append(cur_id)
                cur_id = self.left[cur_id]
            elif stack:
                cur_id = stack.pop()
                yield self.key[cur_id]
                cur_id = self.right[cur_id]
            else:
                break
#         self.result = []
#         # Finish the implementation
#         # You may need to add a new recursive method to do that

#         return self.result

    def preOrder(self):
        cur_id = 0
        stack = []

        while True:
            if cur_id != -1:
                yield self.key[cur_id]
                stack.append(cur_id)
                cur_id = self.left[cur_id]
            elif stack:
                cur_id = stack.pop()
                cur_id = self.right[cur_id]
            else:
                break
#         self.result = []
#         # Finish the implementation
#         # You may need to add a new recursive method to do that

#         return self.result

    def postOrder(self):
        
        stack1 = [0]
        stack2 = []

        while stack1:
            cur_id = stack1.pop()
            stack2.append(self.key[cur_id])

            left_id = self.left[cur_id]
            right_id = self.right[cur_id]
            if left_id != -1:
                stack1.append(left_id)
            if right_id != -1:
                stack1.append(right_id)

        while stack2:
            yield stack2.pop()
#         self.result = []
#         # Finish the implementation
#         # You may need to add a new recursive method to do that

#         return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
