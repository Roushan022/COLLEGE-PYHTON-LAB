def minimax(depth, index, maximizing, scores):
    if depth == 3:                                          # leaf node reached
        return scores[index]

    left  = minimax(depth + 1, index * 2,     not maximizing, scores)   # left child
    right = minimax(depth + 1, index * 2 + 1, not maximizing, scores)   # right child

    if maximizing:
        return max(left, right)                             # Maximizer picks the larger
    else:
        return min(left, right)                             # Minimizer picks the smaller
# Level 0: Max (root), Level 1: Min, Level 2: Max, Level 3: leaves
scores = [3, 5, 2, 9, 12, 5, 23, 23]

print("Leaf node values (terminal utilities):")
print(" ", scores)
optimal_value = minimax(0, 0, True, scores)
print("\nThe optimal value obtainable by the Maximizer (Player 1) is:", optimal_value)
