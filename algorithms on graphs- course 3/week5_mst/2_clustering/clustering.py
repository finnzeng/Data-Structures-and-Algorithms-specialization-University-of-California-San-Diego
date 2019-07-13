#Uses python3
import sys
import math

def distance(v1,v2,x,y):
    return math.sqrt((x[v1]-x[v2])**2 +  (y[v1]-y[v2])**2) 
    

def clustering(x, y, k):
    #create edge list
    edges = []
    for i in range(len(x)):
        for j in range(i,len(x)):
            if i != j:
                edges.append([i,j,distance(i,j,x,y)])

    #sort edges
    sorted_Edges = sorted(edges, key=lambda x: x[2])
    
    for i in sorted_Edges:
        pass #print(i)
 

    #Krusgal's algorthm       
    membership = range(n)
    
    
    #run Kruskal algorithm
    MST = []  #initialize minimum spanning tree
    minDist = 0
    for i in sorted_Edges:

        #make sure vertices are not already joined
        if membership[i[0]] != membership[i[1]]:
            #stop if number of partitions eqals desired number of clusters
            if len(set(membership)) == k:
                nextEdge = i
                break
            #add edge
            MST.append(i)
            minDist += i[2]
            #join groups
            membership = list(map(lambda x: membership[i[0]] if x == membership[i[1]] else x, membership))
            
    return nextEdge[2]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
