# Assignment 1: 

This repository contains the comparisons of the results in problems 1 and 2.

## Problem 1: BFS vs. DFS Implementation and Analysis

### Comparisons
Compare the results and write your findings on the differences between BFS and DFS (e.g., traversal order, memory usage, path length):

***Traversal Order**: BFS always expands the shallowest node in the frontier. DFS always expands the deepest node in the frontier.
***Memory Usage**: BFS is O(b^d) (exponential), it requires more memory which in return being it's biggest problem. DFS O(bm) (linear) and requires less memory.
***Path Length**: BFS is optimal if cost = 1 per step, so in the case for an unweighted graph or grid this would be useful. DFS is not optimal; it finds the leftmost solution regardless of depth or cost, it is less optimal than the BFS result.

---

## Problem 2: DLS on the grid

### Comparisons
Compare the two runs. Discuss how changing the depth limit impacts
success/completeness, node expansions, and path quality. Briefly contrast DLS with your BFS/DFS results.

I ran the DLS implementation with two different depth limits:

***Limit = 4**: The search failed to find a path. Because the goal B is further than 4 steps from start A, the algorithm reached the depth cutoff before encountering the goal.
***Limit = 8**: The search successfully found a path. With a sufficient depth limit, the algorithm was able to reach coordinate (3, 3).

### Discussion
***Impact of Depth Limit**: Increasing the limit makes it easier for DLS to find the goal, but it also makes the search longer with more node expansions.
***Path Quality**: DLS is not optimal if L > d.
***Contrast with BFS/DFS**: DLS provides a controlled cutoff. Unlike BFS, it still does not guarantee the shortest path.