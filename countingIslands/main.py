vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
edges = [('A' ,'B'),('B' ,'A'), ('D' ,'E'), ('F' ,'G'), ('G' ,'F')]

def countDistinctIslands(vertices, edges):
    adjancencyList = {}

    # For every vertex add it to the adjacency list with an empty set
    for vertex in vertices:
        adjancencyList[vertex] = set()

    for vertexA, vertexB in edges:
        adjancencyList[vertexA].add(vertexB)
        adjancencyList[vertexB].add(vertexA)

    globabllyUnvistedVertices = set(adjancencyList.keys())

    def dfs_util(node, visited):
        visited.add(node)
        neighbours = adjancencyList[node]

        globabllyUnvistedVertices.remove(node)

        for neighbour in neighbours:
            if neighbour not in visited:
                dfs_util(neighbour, visited)


    count = 0
    while len(globabllyUnvistedVertices) > 0:
        dfs_util(list(globabllyUnvistedVertices)[0], set())
        count += 1
    
    return count




result = countDistinctIslands(vertices, edges)

print(result)
