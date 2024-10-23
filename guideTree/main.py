from collections import deque

# Graph is circle with bridge in the middle
edges = [['A' ,'B'],['B', 'C'],['C', 'D'], ['D','E'],['E', 'F'] ,['F' ,'G'], ['G' ,'A'], ['B', 'Z'], ['Z', 'L'], ['L', 'G']]

def edgesToAdjacencyList(edges, directional = True):
    aList = {}
    
    for vertexA, vertexB in edges:
        if vertexA not in aList:
            aList[vertexA] = set()
        if vertexB not in aList:
            aList[vertexB] = set()

        aList[vertexA].add(vertexB)

        if not directional:
            aList[vertexB].add(vertexA)
        
    return aList

# Returns a tree that will guide the shortest number of hops from every node to target node
def guidingTreeToTarget(edges, targetNode):
    aList = edgesToAdjacencyList(edges, False)
    guideTree = {}

    for key in aList:
        guideTree[key] = set()

    queue = deque([targetNode])
    visited = set([targetNode])

    while (len(queue) > 0):
        currentNode = queue.popleft()
        visited.add(currentNode)

        for neighbor in aList[currentNode]:
            if neighbor not in visited:
                queue.append(neighbor)
                guideTree[neighbor].add(currentNode)
    
    return guideTree

        
print(guidingTreeToTarget(edges, 'E'))
