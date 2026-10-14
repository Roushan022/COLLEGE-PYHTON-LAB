from collections import deque

def water_jug_bfs(cap1, cap2, target):
    start = (0, 0)
    visited = {start}
    queue = deque([[start]])            # queue of paths

    while queue:
        path = queue.popleft()
        x, y = path[-1]                 # current state

        if x == target or y == target:  # goal reached
            return path

        pour_12 = min(x, cap2 - y)      # amount that moves from jug1 to jug2
        pour_21 = min(y, cap1 - x)      # amount that moves from jug2 to jug1

        next_states = [
            (cap1, y),                  # fill jug1
            (x, cap2),                  # fill jug2
            (0, y),                     # empty jug1
            (x, 0),                     # empty jug2
            (x - pour_12, y + pour_12), # pour jug1 -> jug2
            (x + pour_21, y - pour_21)  # pour jug2 -> jug1
        ]

        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append(path + [state])

    return None                         # no solution

jug1 = 4
jug2 = 3
target = 2

print("Jug1 capacity =", jug1, ", Jug2 capacity =", jug2, ", Target =", target)

solution = water_jug_bfs(jug1, jug2, target)

if solution:
    print("\nSolution found in", len(solution) - 1, "steps:")
    for step, (j1, j2) in enumerate(solution):
        print("  Step", step, ": Jug1 =", j1, ", Jug2 =", j2)
else:
    print("No solution exists for the given target.")
