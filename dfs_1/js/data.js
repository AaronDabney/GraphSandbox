const people = [
    {
        name: "Sally",
        age: 20,
    },
    {
        name: "Bob",
        age: 32,
    },
    {
        name: "Mike",
        age: 22,
    },
    {
        name: "Dave",
        age: 19,
    },
    {
        name: "Jim",
        age: 19,
    },
    {
        name: "Havier",
        age: 13,
    }
];

const friendships = [
    {
        edge:["Sally", "Bob"],
        weight: 0.1
    },
    {
        edge:["Sally", "Mike"],
        weight: 0.2
    },
    {
        edge:["Bob", "Mike"],
        weight: 0.8
    },
    {
        edge:["Dave", "Mike"],
        weight: 0.6
    },
    {
        edge:["Dave", "Jim"],
        weight: 0.9
    },
    {
        edge:["Jim", "Havier"],
        weight: 0.1
    },
    {
        edge:["Havier", "Sally"],
        weight: 0.3
    },
];

module.exports = {
    people,
    friendships
}
