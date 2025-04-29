

def dfs(graph, vertex, visited):
  
    visited.add(vertex)
    print(vertex, end=' ')


    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

if __name__ == "__main__":
    graph = {}


    num_vertices = int(input("Enter the number of vertices: "))
    num_edges = int(input("Enter the number of edges: "))

   
    for i in range(num_vertices):
        vertex = input(f"Enter name of vertex {i+1}: ")
        graph[vertex] = []

    
    print("Enter edges (vertex1 vertex2):")
    for _ in range(num_edges):
        v1, v2 = input().split()
        graph[v1].append(v2)
        graph[v2].append(v1)  # because the graph is undirected

   
    print("\nThe adjacency list of the graph is:")
    for vertex in graph:
        print(f"{vertex} -> {graph[vertex]}")

    
    start_vertex = input("\nEnter the starting vertex for DFS: ")
    visited = set()

    print("\nDepth First Search traversal:")
    dfs(graph, start_vertex, visited)
