class Graph {
    constructor() {
        this.adjList = new Map();
    }

    addVertex(vertex) {
        this.adjList.set(vertex, []);
    }

    addEdge(vertexA, vertexB) {
        this.adjList.get(vertexA).push(vertexB);
        this.adjList.get(vertexB).push(vertexA);
    }
}

module.exports = {
    Graph
}
