# Graph Traversals

This repository contains Python scripts for working with graphs, including graph generation, traversal algorithms, and performance analysis. These scripts have been designed to fulfill specific lab tasks and include templates for various graph operations.

---

## Lab Tasks

### Reading Graphs
Implement functions to read a graph from a `.dot` file in different representations:
- **Incidence Matrix**: A 2D Python list.
- **Adjacency Matrix**: A 2D Python list.
- **Adjacency List**: A Python dictionary mapping vertices to lists of adjacent vertices.

### Recursive Traversal
Implement recursive Depth-First Search (DFS) and Breadth-First Search (BFS) algorithms for the following graph representations:
- **Adjacency Matrix**
- **Adjacency List**

### Iterative Traversal
Implement iterative versions of DFS and BFS for the **Adjacency Matrix** representation.

### Task 4: Graph Radius
Calculate the radius of a graph for the following representations:
- **Adjacency Matrix**
- **Adjacency List**
- **Incidence Matrix**

### Performance Analysis
Compare the performance of the implemented algorithms by testing them on graphs of varying sizes. Analyze the results and visualize the data with graphs to support your conclusions.

---

## Features

### Graph Representations
The repository supports reading and working with graphs in multiple formats:
- **Incidence Matrix**
- **Adjacency Matrix**
- **Adjacency List**

### Graph Traversal Algorithms
- **DFS (Depth-First Search)**
  - Recursive and iterative implementations.
- **BFS (Breadth-First Search)**
  - Recursive and iterative implementations.

### Graph Metrics
- Calculate the radius of a graph from its representation.

### Performance Comparison
- Analyze and compare execution times of traversal algorithms.

---

## File Overview

### 1. **`function_comparison.py`**
- Compares the execution time of different traversal algorithms (DFS and BFS) across various graph representations.
- Uses the `track_time` decorator to measure and report performance.
- **Example Workflow**:
  - Reads a graph from a `.dot` file.
  - Runs traversal algorithms (both iterative and recursive).
  - Prints the execution time for each method.

### 2. **`generate_graph.py`**
- Generates random directed graphs and saves them in `.dot` format for testing and visualization.
- **Key Features**:
  - Specify the number of vertices and edges.
  - Prevents self-loops.
  - Outputs a `.dot` file in a `graphs/` directory.
- **Example Workflow**:
  - Input graph parameters (number of vertices and edges).
  - Generate graphs in DOT format.
  - Use these graphs for testing traversal algorithms.

### 3. **`traversals.py`**
This module provides functions to read graphs in different formats (incidence matrix,
adjacency matrix, and adjacency list) and perform Depth-First Search (DFS) and
Breadth-First Search (BFS) on these graphs. It also includes functions to calculate
the radius of a graph.

#### Functions:
- `read_incidence_matrix`: Reads an incidence matrix from a file.
- `read_adjacency_matrix`: Reads an adjacency matrix from a file.
- `read_adjacency_dict`: Reads an adjacency list from a file.

#### Depth-First Search (DFS) Functions:
- `iterative_adjacency_dict_dfs`: Performs iterative DFS on an adjacency list.
- `iterative_adjacency_matrix_dfs`: Performs iterative DFS on an adjacency matrix.
- `recursive_adjacency_dict_dfs`: Performs recursive DFS on an adjacency list.
- `recursive_adjacency_matrix_dfs`: Performs recursive DFS on an adjacency matrix.

#### Breadth-First Search (BFS) Functions:
- `iterative_adjacency_dict_bfs`: Performs iterative BFS on an adjacency list.
- `iterative_adjacency_matrix_bfs`: Performs iterative BFS on an adjacency matrix.

#### Graph Radius Calculation:
- `adjacency_matrix_radius`: Calculates the radius of a graph from an adjacency matrix.
- `adjacency_dict_radius`: Calculates the radius of a graph from an adjacency list.
---

## Getting Started

### Installation
#### 1. Clone the repository:
   ```bash
   git clone https://github.com/mohinska/traversals_lab.git
   cd traversals_lab
   ```
#### 2. Usage

1. Generate a Graph

Use `generate_graph.py` to create a graph:

```bash
python generate_graph.py
```

Follow the prompts to input the number of vertices and edges. The script saves the graph in .dot format.

2. Read Graph Representations

Use traversals.py to read graphs:

```bash
from traversals import read_adjacency_matrix, read_incidence_matrix

adj_matrix = read_adjacency_matrix("graphs/example.dot")
inc_matrix = read_incidence_matrix("graphs/example.dot")
```

3. Perform Traversals

Run DFS or BFS on a graph representation:

```bash
from traversals import recursive_adjacency_dict_dfs, iterative_adjacency_matrix_bfs

dfs_result = recursive_adjacency_dict_dfs(adj_list, start=0)
bfs_result = iterative_adjacency_matrix_bfs(adj_matrix, start=0)
print("DFS:", dfs_result)
print("BFS:", bfs_result)
```

4. Compare Performance

Run `function_comparison.py` to measure traversal times:

```bash
python function_comparison.py
```

Provide the input graph file when prompted.
