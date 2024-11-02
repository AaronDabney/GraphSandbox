#Four islands (A-B) (C) (D-E) (F-G)
vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
edges = [('A' ,'B'), ('D' ,'E'),  ('F' ,'G')]

# Expects undirected input
def count_distinct_islands(vertices, edges):
    adjancency_list = {}

    # For every vertex add it to the adjacency list with an empty set
    for vertex in vertices:
        adjancency_list[vertex] = set()

    for vertexA, vertexB in edges:
        adjancency_list[vertexA].add(vertexB)
        adjancency_list[vertexB].add(vertexA)

    globablly_unvisted_vertices = set(adjancency_list.keys())

    def dfs_util(node, visited):
        visited.add(node)
        neighbours = adjancency_list[node]

        globablly_unvisted_vertices.remove(node)

        for neighbour in neighbours:
            if neighbour not in visited:
                dfs_util(neighbour, visited)


    count = 0
    while len(globablly_unvisted_vertices) > 0:
        dfs_util(list(globablly_unvisted_vertices)[0], set())
        count += 1
    
    return count



result = count_distinct_islands(vertices, edges)

print(result)
# Output - 4

# TODO: More test cases
