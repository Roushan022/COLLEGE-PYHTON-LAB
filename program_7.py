import heapq

def heuristic(a, b):                       # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):
    heap = [(heuristic(start, goal), 0, start, [start])]   # (f, g, cell, path)
    visited = set()

    while heap:
        f, g, current, path = heapq.heappop(heap)          # lowest f first

        if current == goal:                                # goal reached
            return path

        if current in visited:
            continue
        visited.add(current)
        r, c = current
        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:   # up, down, left, right
            if 0 <= nr < 4 and 0 <= nc < 4 and grid[nr][nc] == 0:
                new_g = g + 1
                f_score = new_g + heuristic((nr, nc), goal)
                heapq.heappush(heap, (f_score, new_g, (nr, nc), path + [(nr, nc)]))

    return None                                            # no path
grid = [[0, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 1],
        [0, 0, 0, 0]]

start = (0, 0)
goal = (3, 3)

print("4x4 Grid (0 = free, 1 = obstacle):")
for row in grid:
    print(" ", row)

print("\nStart:", start, ", Goal:", goal)
path = astar(grid, start, goal)
if path:
    print("\nShortest path found (", len(path) - 1, "moves ):")
    print(" -> ".join(str(p) for p in path))

    for r, c in path:                  # mark the path with *
        grid[r][c] = '*'
    print("\nGrid with path marked ('*'):")
    for row in grid:
        print(" ", row)
else:
    print("No path exists between start and goal.")
