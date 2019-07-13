# Minimum Spanning Trees
## 1. Building a Network
### 1-1. Minimum spanning tree (MST)
* Input: A connected, undirected graph G = (V , E) with positive edge weights.
* Output: A subset of edges E′ ⊆ E of minimum total weight such that the graph (V , E′) is connected.

#### Remark
The set E′ always forms a tree.

### 1-2. Properties of Trees
* A tree is an undirected graph that is connected and acyclic.
* A tree on n vertices has n − 1 edges.
* Any connected undirected graph G(V , E) with |E| = |V | − 1 is a tree.
* An undirected graph is a tree iff there is a unique path between any pair of its vertices.

## 2. Greedy Algorithms
### 2-1. Kruskal’s algorithm
repeatedly add the next lightest edge if this doesn’t produce a cycle
### 2-2. Prim’s algorithm
repeatedly attach a new vertex to the current tree by a lightest edge

## 3. Cut property
Let a subset of edges X ⊆ E be a part of a MST of G(V, E), S ⊆ V be such that no edge of X crosses between S and V − S, and e ∈ E be a lightest edge across this partition. Then X + {e} is a part of some MST.

## 4. Kruskal’s Algorithm
### 4-1. Kruskal’s Algorithm
* Algorithm: repeatedly add to X the next lightest edge e that doesn’t produce a cycle
* At any point of time, the set X is a forest, that is, a collection of trees
* The next edge e connects two different trees—say, T1 and T2
* The edge e is the lightest between T1 and V − T1, hence adding e is safe

### 4-2. Implementation Details
* use disjoint sets data structure
* initially, each vertex lies in a separate set
* each set is the set of vertices of a connected component
* to check whether the current edge {u, v} produces a cycle, we check whether u and v belong to the same set

#### Algorithm
```
Kruskal(G)
  for all u ∈ V :
    MakeSet(v)
  X ← empty set
  sort the edges E by weight
  for all {u, v} ∈ E in non-decreasing
    weight order:
    if Find(u) ̸= Find(v):
      add {u, v} to X
      Union(u, v)
  return X
 ```
 
#### Running Time
* Sorting edges: O(|E|log|E|) = O(|E|log|V|^2) = O(2|E|log|V|) = O(|E|log|V|)
* Processing edges: 2|E|·T(Find)+|V|·T(Union) = O((|E|+|V|)log|V|) = O(|E|log|V|)
* Total running time: O(|E|log|V|)

## 5. Prim’s Algorithm
### 5-1. Prim’s Algorithm
* X is always a subtree, grows by one edge at each iteration
* we add a lightest edge between a vertex of the tree and a vertex not in the tree
* very similar to Dijkstra’s algorithm

#### Algorithm
```
Prim(G)
  for all u ∈ V:
    cost[u] ← ∞, parent[u] ← nil
  pick any initial vertex u0
  cost[u0] ← 0
  PrioQ ← MakeQueue(V) {priority is cost}
  while PrioQ is not empty:
    v ← ExtractMin(PrioQ)
    for all {v, z} ∈ E:
      if z ∈ PrioQ and cost[z] > w(v, z):
        cost[z] ← w(v, z), parent[z] ← v
        ChangePriority(PrioQ, z, cost[z])
```

#### Running Time
* the running time is |V|·T(ExtractMin)+|E|·T(ChangePriority)
* for array-based implementation, the running time is O(|V|^2)
* for binary heap-based implementation, the running time is O((|V|+|E|)log|V|) = O(|E|log|V|)

## 6. Summary
**Kruskal**: repeatedly add the next lightest edge if this doesn’t produce a cycle; use disjoint sets to check whether the current edge joins two vertices from different components</br>
**Prim**: repeatedly attach a new vertex to the current tree by a lightest edge; use priority queue to quickly find the next lightest edge</br>