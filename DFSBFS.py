from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # Undirected graph

    def display_graph(self):
        print("Adjacency List:")
        for vertex in self.graph:
            print(f"{vertex} -> {self.graph[vertex]}")

    def dfs_util(self, vertex, visited):
        print(vertex, end=' ')
        visited.add(vertex)
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

    def dfs(self, start):
        visited = set()
        print("DFS Traversal:")
        self.dfs_util(start, visited)
        print()

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        print("BFS Traversal:")
        while queue:
            vertex = queue.popleft()
            print(vertex, end=' ')
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        print()

def main():
    g = Graph()

    while True:
        print("\nMenu:")
        print("1. Add Edge")
        print("2. Display Graph")
        print("3. DFS Traversal")
        print("4. BFS Traversal")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            u = input("Enter vertex 1: ")
            v = input("Enter vertex 2: ")
            g.add_edge(u, v)
        elif choice == '2':
            g.display_graph()
        elif choice == '3':
            start = input("Enter starting vertex for DFS: ")
            g.dfs(start)
        elif choice == '4':
            start = input("Enter starting vertex for BFS: ")
            g.bfs(start)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
