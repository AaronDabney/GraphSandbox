from collections import deque

# Graph is circle with bridge in the middle
edges = [['A' ,'B'],['B', 'C'],['C', 'D'], ['D','E'],['E', 'F'] ,['F' ,'G'], ['G' ,'A'], ['B', 'Z'], ['Z', 'L'], ['L', 'G']]

def edges_to_adjacency_list(edges, directional = True):
    a_list = {}
    
    for vertex_A, vertex_B in edges:
        if vertex_A not in a_list:
            a_list[vertex_A] = set()
        if vertex_B not in a_list:
            a_list[vertex_B] = set()

        a_list[vertex_A].add(vertex_B)

        if not directional:
            a_list[vertex_B].add(vertex_A)
        
    return a_list

# Returns a tree that will guide the shortest number of hops from every node to target node
# Remeniscent of Djikstra but has defines no specific ordering of candidate nodes
def guiding_tree_to_target(edges, target_node):
    a_list = edges_to_adjacency_list(edges, False)
    guide_tree = {}

    for key in a_list:
        guide_tree[key] = set()

    queue = deque([target_node])
    visited = set([target_node])

    while (len(queue) > 0):
        current_node = queue.popleft()
        visited.add(current_node)

        for neighbor in a_list[current_node]:
            if neighbor not in visited:
                queue.append(neighbor)
                guide_tree[neighbor].add(current_node)
    
    return guide_tree

        
print(guiding_tree_to_target(edges, 'E'))
# TODO: More tests
