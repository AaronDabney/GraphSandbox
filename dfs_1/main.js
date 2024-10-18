const { Graph } = require('./graph')
const { people } = require('./people')


const graph = new Graph();


// Add vertices to graph
for (let person of people) {
    graph.addVertex(person);
}

// Add edges to graph
for (let person of people) {
    for (let friendName of person.friends) {
        let friend = people.find(el => el.name === friendName);
        graph.addEdge(person, friend);
    }
}

/**
 * Return an array of matching nodes from graph that pass test function
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

const sally = people.find(el => el.name = 'Sally');


console.log(graph);
console.log('\n')
console.log('Matches: ')
console.log(bfs(graph, sally, isFriendsWithSally));


// Output -> 

// Graph {
//     adjList: Map(6) {
//       { name: 'Sally', age: 20, friends: [Array] } => [ [Object], [Object], [Object] ],
//       { name: 'Bob', age: 202, friends: [Array] } => [ [Object], [Object] ],
//       { name: 'Mike', age: 2, friends: [Array] } => [ [Object], [Object] ],
//       { name: 'Dave', age: 19, friends: [Array] } => [ [Object], [Object] ],
//       { name: 'Jim', age: 19, friends: [Array] } => [ [Object], [Object] ],
//       { name: 'Havier', age: 13, friends: [Array] } => [ [Object] ]
//     }
//   }
  
  
//   Matches: 
//   [
//     { name: 'Dave', age: 19, friends: [ 'Sally' ] },
//     { name: 'Jim', age: 19, friends: [ 'Sally' ] }
//   ]
