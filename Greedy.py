import heapq
from collections import defaultdict

# ---------- 1. Prim's Minimum Spanning Tree ----------
def prims_with_edges():
    # Step 1: Input number of vertices and edges
    V, E = map(int, input("Enter number of vertices and edges: ").split())
    print(f"Enter {E} edges (u v weight):")

    adj = defaultdict(list)

    # Step 2: Build adjacency list
    for _ in range(E):
        u, v, w = map(int, input().split())  # Read u, v, and weight w
        adj[u].append((v, w))
        adj[v].append((u, w))  # Because graph is undirected

    visited = [False] * (V + 1)
    min_heap = [(0, 1)]  # Start from node 1 with cost 0
    total_weight = 0
    mst_edges = []

    # Step 3: Prim's main loop using min heap
    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        total_weight += weight
        if weight != 0:
            mst_edges.append((u, weight))

        for v, w in adj[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v))

    # Step 4: Print MST
    print("\nMinimum Spanning Tree edges:")
    for u, w in mst_edges:
        print(f"{u} (weight: {w})")
    print("Total Weight of MST:", total_weight)

# ---------- 2. Greedy Job Scheduling ----------
def job_scheduling(jobs):
    # Step 1: Sort jobs by profit (descending)
    jobs.sort(key=lambda x: x[2], reverse=True)
    max_deadline = max(job[1] for job in jobs)
    result = [None] * max_deadline
    total_profit = 0

    # Step 2: Assign each job to latest possible time slot
    for job in jobs:
        for slot in range(min(max_deadline, job[1]) - 1, -1, -1):
            if result[slot] is None:
                result[slot] = job
                total_profit += job[2]
                break

    # Step 3: Print scheduled jobs
    print("\nScheduled Jobs:", [j[0] for j in result if j])
    print("Total Profit:", total_profit)

# ---------- 3. Selection Sort ----------
def selection_sort(arr):
    n = len(arr)
    # Loop through each element in array
    for i in range(n):
        min_idx = i
        # Find the minimum element in remaining array
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print("\nSorted array:", arr)

# ---------- Menu ----------
def main():
    while True:
        print("\n--- Greedy Algorithms Menu ---")
        print("1. Find MST using Prim's Algorithm")
        print("2. Perform Greedy Job Scheduling")
        print("3. Perform Selection Sort")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            prims_with_edges()

        elif choice == "2":
            n = int(input("Enter number of jobs: "))
            jobs = []
            for i in range(n):
                job_id = input(f"Job {i+1} ID: ")
                deadline = int(input("  Deadline: "))
                profit = int(input("  Profit: "))
                jobs.append((job_id, deadline, profit))
            job_scheduling(jobs)

        elif choice == "3":
            arr = list(map(int, input("Enter elements to sort (space-separated): ").split()))
            selection_sort(arr)

        elif choice == "4":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

# Entry point
if __name__ == "__main__":
    main()
