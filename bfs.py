from collections import deque

def create_graph():
    graph = {}
    num_vertices = int(input("Enter the number of vertices: "))

    for _ in range(num_vertices):
        vertex = input("Enter the vertex: ")
        neighbors = input(f"Enter the neighbors of {vertex} (comma-separated): ")
        
        neighbors_list = [n.strip() for n in neighbors.split(",")]
        graph[vertex] = neighbors_list

    return graph


def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node)
            visited.add(node)
            queue.extend(neighbor for neighbor in graph.get(node, []) if neighbor not in visited)


def bfs_main():
    graph = create_graph()

    start_node = input("Enter the starting node for BFS traversal: ")

    print("BFS traversal order:")
    bfs(graph, start_node)


if __name__ == "__main__":
    bfs_main()
