import random


def generate_dot_file(filename: str, num_vertices: int, num_edges: int) -> None:
    """
    Generates a random directed graph and writes it to a file in DOT format.

    The function creates a graph with the specified number of vertices and edges.
    The edges are randomly generated, ensuring no self-loops (edges from a vertex to itself),
    and the resulting graph is written in DOT format for further processing or visualization.

    :param filename: The name of the output file where the graph will be saved.
    :param num_vertices: The number of vertices in the graph.
    :param num_edges: The number of edges in the graph.
    """
    # Validate if the number of edges exceeds the maximum possible for the graph
    if num_edges > num_vertices * (num_vertices - 1):
        raise ValueError(f"Too many edges for {num_vertices} vertices. Maximum allowed: {
                         num_vertices * (num_vertices - 1)}")

    edges = set()

    # Generate unique edges (no self-loops)
    while len(edges) < num_edges:
        start = random.randint(0, num_vertices - 1)
        end = random.randint(0, num_vertices - 1)
        if start != end:  # Ensure no self-loop
            edges.add((start, end))

    # Write the graph to a file in DOT format
    with open(filename, 'w', encoding='utf-8') as file:
        file.write("digraph generated_graph {\n")
        for start, end in edges:
            file.write(f"\t{start} -> {end};\n")
        file.write("}\n")


def main():
    print("Enter <number of vertices>, <number of edges>. To end input press enter.")
    sizes = []
    while True:
        try:
            graph = input()
            if graph == '':
                break
            vertices, edges = [int(i) for i in graph.strip().split()]
            sizes.append((vertices, edges))
        except ValueError:
            print('Wrong input. Enter <number of vertices>, <number of edges>')
        except EOFError:
            break

    print(f"\nCollected graph sizes: {sizes}")
    for i, (vertices, edges) in enumerate(sizes):
        try:
            generate_dot_file(f"{i+1}.dot", vertices, edges)
            print(f"Generated file: {
                  i+1}.dot with {vertices} vertices and {edges} edges")
        except ValueError as e:
            print(f"Error generating graph {i+1}.dot: {e}")


if __name__ == "__main__":
    main()
