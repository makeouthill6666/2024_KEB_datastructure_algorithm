graph = [
    [0, 1, 1, 0, 0, 0], #문별
    [1, 0, 0, 1, 0, 0], #솔라
    [1, 0, 0, 1, 0 ,0], #휘인
    [0, 1, 1, 0, 1, 1], #쯔위
    [0, 0, 0, 1, 0 ,1], #선미
    [0, 0, 0, 1, 1, 0], #화사
]



def dfs(g, v, visited):
    visited[v] = True
    print(chr(ord('A')+v), end=' ')
    for i in range(len(graph)):
        if graph[v][i] == True and not visited[i]:
            dfs(g, i, visited)

visited = [0 for _ in range(len(graph))]
dfs(graph, 0, visited)
#
#
# visited = [False] * len(graph)
# dfs(graph, 0 , visited)