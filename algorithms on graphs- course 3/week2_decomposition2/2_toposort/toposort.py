#Uses python3

import sys

def dfs(adj, used, order, x):
    used[x] = 1  #checks neighbours of x, and add them before you add x.
    for i in adj[x]:
#         print(i,'   nah')
        if not used[i]:
            dfs(adj,used,order,i)
    order.append(x)
    return


def toposort(adj):
    used = [0] * len(adj)
    order = []
    for i in range(len(adj)):
#         print(i,'  ha')
        if not used[i]:
            dfs(adj,used,order,i)
    return order[::-1] #because we are kinda adding the last points first, print in reverse. Don't need to print in reverse if you
# change the command in dfs file from order.append to order.insert(0,x)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

