const { Graph } = require('./graph')
const { people, friendships } = require('./data')


const graph = new Graph();

// Add vertices to graph
for (let person of people) {
    graph.addVertex(person);
}

// Add edges to graph
for (let person of people) {
    const friendshipContainsPerson = friendship => friendship.edge.includes(person.name);
  
    let relevantFriendships = friendships.filter(friendship => friendshipContainsPerson(friendship));


    for (let friendShip of relevantFriendships) {
        let [friendOneName, friendTwoName] = friendShip.edge;

        let friendOne = Array.from(graph.adjList).find(([key, value]) => key.name === friendOneName)[0];
        let friendTwo = Array.from(graph.adjList).find(([key, value]) => key.name === friendTwoName)[0];

        graph.addEdge(friendOne, friendTwo);
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


const personYoungerThanTwenty = person => person.age < 20;

const sally = people.find(el => el.name = 'Sally');

console.log(graph);
console.log('\n')
console.log('Matches: ')
console.log(bfs(graph, sally, personYoungerThanTwenty));


// Graph {
//     adjList: Map(6) {
//       { name: 'Sally', age: 20 } => [ [Object], [Object], [Object], [Object], [Object], [Object] ],
//       { name: 'Bob', age: 32 } => [ [Object], [Object], [Object], [Object] ],
//       { name: 'Mike', age: 22 } => [ [Object], [Object], [Object], [Object], [Object], [Object] ],
//       { name: 'Dave', age: 19 } => [ [Object], [Object], [Object], [Object] ],
//       { name: 'Jim', age: 19 } => [ [Object], [Object], [Object], [Object] ],
//       { name: 'Havier', age: 13 } => [ [Object], [Object], [Object], [Object] ]
//     }
//   }
  
  
//   Matches: 
//   [
//     { name: 'Havier', age: 13 },
//     { name: 'Dave', age: 19 },
//     { name: 'Jim', age: 19 }
//   ]