graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F','G'],
    'D':[],
    'E':['H'],
    'F':[],
    'G':['I','J'],
    'H':[],
    'I':[],
    'J':[],
}
def dfs(grapg,node,visited):
    if node not in visited:
        print(node,end=" ")
        visited.add(node)
        for child in graph[node]:
            dfs(grapg,child,visited)

visited_nodes=set()
print("D F S")
dfs(graph,'A',visited_nodes)
