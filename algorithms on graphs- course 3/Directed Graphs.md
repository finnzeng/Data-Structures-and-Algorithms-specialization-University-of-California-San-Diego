# Directed Graphs

## 1. Directed Acyclic Graphs
### (1) Directed Graphs
#### Definition
A **directed graph** is a graph where each edge has a start vertex and an end vertex.
### (2) Directed DFS
* Only follow **directed** edges.
* **explore(v)** finds all vertices **reachable** from v.
* Can still compute pre- and post- orderings.

### (3) Cycles
#### Definition
A **cycle** in a graph G is a sequence of vertices v1, v2, ..., vn so that (v1, v2), (v2, v3), ... , (vn-1, vn), (vn, v1) are all edges.
#### Theorem
If G contains a cycle, it cannot be linearly ordered.
### (4) DAGs
#### Definition
A directed graph G is a **Directed Acyclic Graph** (or DAG) if it has no cycles.
* Being a DAG is necessary to linearly order.

## 2. Topological Sort
### (1) Sources and Sinks
A **source** is a vertex with no incoming edges. </br>
A **sink** is a vertex with on outgoing edges.

### (2) Idea of producing linear order
* Find sink
* Put at end of order 
* Remove from graph 
* Repeat

### (3) How do we know that there is a sink?
#### Follow Path
Follow path as far as possible. </br>
v1 -> v2 -> ... ->vn. Eventually either.
* Cannot extend (found sink).
* Repeat a vertex (have a cycle).

### (4) First Try
```
LinearOrder(G)
    while G non-empty:
        Follow a path until cannot extend
        Find sink v
        Put v at end of order
        Remove v from G
```
#### Runtime
* O(|V|) paths.
* Each takes O(|V|) time.
* Runtime O(|V|^2)

### (5) Speed Up
* Retrace same path every time
* Instead only back up as far as necessary

### (6) Better Algorithm
```
TopologicalSort(G)
    DFS(G)
    sort vertices by reverse post-order
```
### (7) Theorem
If G is a DAG, with an edge u to v, post(u) > post(v).

## 3. Strongly Connected Components
### (1) Strongly Connected Components
#### Definition
Two vertices v, w in a directed graph are **connected** if you can reach v from w and can reach w from v.
#### Theorem
A directed graph can be partitioned into **strongly connected components** where two vertices are connected if and only if they are in the same component.
### (2) Metagraph
We can also draw a **metagraph** showing how the strongly connected components connect to one another. </br>
**Example** </br>
<img src="http://i.imgur.com/4OiCGm1.png"> </br>
**Note**: It's a DAG. </br>
#### Theorem
The metagraph of a graph G is always a DAG.

## 4. Computing Strongly Connected Components
### (1) Problem
**input**: A directed graph </br>
**output**: The strongly connected components of G.
### (2) Easy Algorithm
```
EasySCC(G)
    for each vertex v:
        run explore(v) to determine vertices reachable from v
    for each vertex v:
        find the u reachable from v that can also reach v
    these are the SCCs
```
#### Runtime
O(|V|^2 + |V||E|). Want faster.
### (3) Sink Components
**Idea**: If v is in a sink SCC, explore(v) finds vertices reachable from v. This is exactly the SCC of v. </br>
Need a way to find a sink SCC. </br>
### (4) Theorem
If C and C' are two strongly connected components with an edge from some vertex of C to some vertex of C', then largest post number in C bigger than the largest post number in C'. </br>
**Conclusion**: The vertex with the largest postorder number is in a source component! </br>
### (5) Reverse Graph
Let G^R be the graph obtained from G by revesing all of the edges. </br>
* G^R and G have same SCCs.
* Source components of G^R are sink components of G.

FInd sink components of G by running DFS on G^R </br>
**Note**: The vertex with the largest postorder number in G^R is in a sink SCC of G. </br>
### (6) Basic Algorithm
```
SCCs(G)
    run DFS(G^R)
    let v have largest post number
    run Explore(v)
    vertices found are first SCC
    Remove from G and repeat
```
### (7) Improvement Algorithm
* Don't need to rerun DFS on G^R.
* Largest remaining post number comes from sink component.
```
SCCs(G)
    run DFS(G^R)
    for v ∈ V in reverse postorder:
        if not visited(v):
            Explore(v)
            mark visited vertices as new SCC
```
#### Runtime
* Essentially DFS on R^G and then on G.
* Runtime O(|V| + |E|)