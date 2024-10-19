from socialNetworkData import people, friendships
from utils import printDict

class Graph:
    def __init__(self):
        print("Initalized")
        self.adjencyList = {}
    
    def addVertex(self, vertexID):
        self.adjencyList[vertexID] = set()

    def addEdge(self, vertexOneID, vertexTwoID):
        self.adjencyList[vertexOneID].add(vertexTwoID)
        self.adjencyList[vertexTwoID].add(vertexOneID)

graph = Graph()

# Populate vertices
for personID in people.keys():
    # print(person)
    graph.addVertex(personID)

# Build Edges
for friendship in friendships:
    friendOneID = friendship["edge"][0]
    friendTwoID = friendship["edge"][1]

    graph.addEdge(friendOneID, friendTwoID)

printDict(people)
printDict(friendships)
print(graph.adjencyList)

# Output -> 
# Initalized
# {
#     "0": {
#         "name": "Sally",
#         "age": 20
#     },
#     "1": {
#         "name": "Bob",
#         "age": 32
#     },
#     "2": {
#         "name": "Mike",
#         "age": 22
#     },
#     "3": {
#         "name": "Dave",
#         "age": 19
#     },
#     "4": {
#         "name": "Jim",
#         "age": 19
#     },
#     "5": {
#         "name": "Havier",
#         "age": 13
#     }
# }
# [
#     {
#         "edge": [
#             0,
#             4
#         ],
#         "weight": 0.2872606507206431
#     },
#     {
#         "edge": [
#             1,
#             4
#         ],
#         "weight": 0.3303935677333757
#     },
#     {
#         "edge": [
#             2,
#             0
#         ],
#         "weight": 0.0009720112170390482
#     },
#     {
#         "edge": [
#             3,
#             4
#         ],
#         "weight": 0.13617202805494055
#     },
#     {
#         "edge": [
#             4,
#             5
#         ],
#         "weight": 0.589385716262556
#     },
#     {
#         "edge": [
#             5,
#             4
#         ],
#         "weight": 0.9509297763982734
#     }
# ]
# {0: {2, 4}, 1: {4}, 2: {0}, 3: {4}, 4: {0, 1, 3, 5}, 5: {4}}
