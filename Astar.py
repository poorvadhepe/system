import heapq

# Goal configuration
GOAL_STATE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Possible movement directions (up, down, left, right)
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Manhattan distance heuristic
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                goal_x = (val - 1) // 3
                goal_y = (val - 1) % 3
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

# Generate valid neighboring states
def get_neighbors(state):
    neighbors = []
    x, y = next((i, j) for i in range(3) for j in range(3) if state[i][j] == 0)
    for dx, dy in DIRECTIONS:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

# Convert list of lists to a tuple of tuples (for hashing)
def state_to_tuple(state):
    return tuple(tuple(row) for row in state)

# Print a 3x3 state
def print_state(state):
    for row in state:
        print(row)
    print()

# Take 3x3 user input
def get_user_input():
    print("Enter the puzzle state row by row (use 0 for the blank space):")
    state = []
    used = set()
    for i in range(3):
        while True:
            row_input = input(f"Row {i+1} (3 space-separated numbers from 0-8): ")
            try:
                row = list(map(int, row_input.strip().split()))
                if len(row) != 3 or not all(0 <= x <= 8 for x in row):
                    raise ValueError
                if any(x in used for x in row):
                    raise ValueError
                used.update(row)
                state.append(row)
                break
            except ValueError:
                print("❌ Invalid row. Please enter 3 unique numbers between 0 and 8.")
    return state

# Check if a puzzle is solvable
def is_solvable(state):
    flat = sum(state, [])
    inv_count = 0
    for i in range(len(flat)):
        for j in range(i + 1, len(flat)):
            if flat[i] != 0 and flat[j] != 0 and flat[i] > flat[j]:
                inv_count += 1
    return inv_count % 2 == 0

# A* Search Algorithm
def a_star(start_state):
    if not is_solvable(start_state):
        print("❌ This puzzle configuration is unsolvable.")
        return

    open_set = []
    heapq.heappush(open_set, (manhattan_distance(start_state), 0, start_state, []))
    visited = set()

    while open_set:
        f, g, current, path = heapq.heappop(open_set)
        if current == GOAL_STATE:
            print(f"\n✅ Goal reached in {g} moves!\n")
            for step_num, step in enumerate(path + [current]):
                print(f"Step {step_num}:")
                print_state(step)
            return

        visited.add(state_to_tuple(current))
        for neighbor in get_neighbors(current):
            if state_to_tuple(neighbor) not in visited:
                heapq.heappush(open_set, (
                    g + 1 + manhattan_distance(neighbor),
                    g + 1,
                    neighbor,
                    path + [current]
                ))

    print("❌ No solution found.")

# Main
if __name__ == "__main__":
    print("🧩 8-Puzzle Solver using A* Algorithm")
    initial_state = get_user_input()
    print("\n🔍 Solving the puzzle...")
    a_star(initial_state)
