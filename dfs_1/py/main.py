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
