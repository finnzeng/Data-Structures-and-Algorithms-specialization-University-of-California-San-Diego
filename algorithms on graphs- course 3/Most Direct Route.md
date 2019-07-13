# Most Direct Route

## 1. Most Direct Route
### (1) Paths and lengths
Length of the path L(P) is the number of edges in the path.
### (2) Distances
The **distance** between two vertices is the length of the shortest path between them.

## 2. Breadth-First Search

## 3. Implementation and Analysis
### (1) Breadth-First Search
```
BFS(G, S)
  for all u ∈ V:
    dist[u] ← ∞ // you can assign infinity to number of nodes + 1 or number of edges + 1
  dist[S] ← 0
  Q ← {S} {queue containing just S}
  while Q is not empty:
    u ← Dequeue(Q)
    for all (u, v) ∈ E:
      if dist[v] = ∞:
        Enqueue(Q, v)
        dist[v] ← dist[u] + 1
```

**Note** : The efficient way to implement for all (u, v) ∈ E is go through the adjacency list of vertex u.

### (2) Running time
**Lemma** </br>
The running time of breadth-first search is O(|E| + |V|).</br>

**Proof**
* Each vertex is enqueued at most once.
* Each edge is examined eith once (for directed graphs) or twice (for undirected graphs).

## 4. Proof of Correctness
### (1) Reachability
**Definition** </br>
Node u is **reachable** from node S if there is a path from S to u. </br>

**Lemma** </br>
Reachable nodes are discovered at some point, so they get a finite distance estimate from the source. Unreachable nodes are not discovered at any point, and the distance to them stays infinite. </br>

### (2) Order Lemma
**Lemma** </br>
By the time node u at distance d from S is dequeued, all the nodes at distance at most d have already been discovered (enqueued).

### (3) Correct distances
**Lemma** </br>
When node u is discovered (enqueued), dist[u] is assigned exactly d(S, u).

### (4) Queue property
**Lemma** </br>
At any moment, if the first node in the queue is at distance d from S, then all the nodes in the queue are either at distance d from S or at distance d+1 from S. All the nodes in the queue at distance d go before (if any) all the nodes at distance d+1.

## 5. Shortest-path tree
**Lemma** </br>
Shortest-path tree in indeed a tree, i.e. it doesn't contain cycles (it is a connected component by construction).

### Constructing shortest-path tree
```
BFS(G, S)
  for all u ∈ V:
    dist[u] ← ∞, prev[u] ← nil
  dist[S] ← 0
  Q ← {S} {queue containing just S}
  while Q is not empty:
    u ← Dequeue(Q)
    for all (u, v) ∈ E:
      if dist[v] = ∞:
        Enqueue(Q, v)
        dist[v] ← dist[u] + 1, prev[v] ← u
```

## 6. Reconstructing Shortest Path
```
ReconstructPath(S, u, prev)
  result ← empty
  while u ̸= S:
    result.append(u)
    u ← prev[u]
  return Reverse(result)
```