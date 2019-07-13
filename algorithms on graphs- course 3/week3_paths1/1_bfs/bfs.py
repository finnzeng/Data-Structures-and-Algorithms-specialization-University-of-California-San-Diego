#Uses python3

import sys
import queue

def distance(adj, start, end):
    #set all distances to infinity or -1
    distance = [-1] * len(adj)
    distance[start] = 0
    #run bfs to get 
    q = queue.Queue()
    q.put(start)
    while not q.empty():
        u = q.get()
        for i in adj[u]:  #first cover all nodes which are at same distance from start
            if distance[i] == -1: # check if distance = inifinity
                distance[i] = distance[u] + 1
                q.put(i)  # add to queue 
    #print(distance)
    return distance[end]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
