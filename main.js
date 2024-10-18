const { Graph } = require('./graph')
const { people } = require('./people')


let graph = new Graph();

for (let person of people) {
    graph.addVertex(person);
}

for (let person of people) {
    for (let friendName of person.friends) {
        let friend = people.find(el => el.name === friendName);
        graph.addEdge(person, friend);
    }
}

/**
 * Return all matches from graph that pass test function
 */
function bfs(graph, startingNode, testFunc) {
    let discovered = new Set([startingNode])
    let processed = new Set();

    let matches = [];

    while (discovered.size > 0) {
        let currentNode = [...discovered].shift(); // Convert set 

        discovered.delete(currentNode);
    
        if (testFunc(currentNode)) {
            matches.push(currentNode)
        }

        processed.add(currentNode);

        let neighbours = graph.adjList.get(currentNode).filter(element => !processed.has(element));

        for (let neighbour of neighbours) {
            discovered.add(neighbour);
        }

    }

    return matches;
}

const isFriendsWithSally = personNode => personNode.friends.includes('Sally');

let sally = people.find(el => el.name = 'Sally');

console.log(bfs(graph, sally, isFriendsWithSally));
