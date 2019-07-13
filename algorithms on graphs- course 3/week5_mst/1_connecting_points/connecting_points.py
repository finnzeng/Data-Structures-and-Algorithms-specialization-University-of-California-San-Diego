#Uses python3
import sys
import math

def distance(v1,v2,x,y):
    return math.sqrt((x[v1]-x[v2])**2 +  (y[v1]-y[v2])**2) 

def minimum_distance(x, y):
    #create edge list
    edges = []
    for i in range(n):
        for j in range(i,n):
            if i != j:
                edges.append([i,j,distance(i,j,x,y)])

    #sort edges based on the distances
    sorted_Edges = sorted(edges, key=lambda x: x[2])
    

    #initialize disjoint data structure
    membership = range(n)
    
    #run Kruskal algorithm
    MST = []  #initialize minimum spanning tree
    minDist = 0
    for i in sorted_Edges:
        #make sure vertices are not already joined
        if membership[i[0]] != membership[i[1]]:
            #add edge
            MST.append(i)
            minDist += i[2]
            #join groups
            membership = list(map(lambda x: membership[i[0]] if x == membership[i[1]] else x, membership))
            
    return minDist


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
