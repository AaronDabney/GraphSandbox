import random
from utils import printDict

people = {
    0: {
        "name": "Sally",
        "age": 20,
    },
    1: {
        "name": "Bob",
        "age": 32,
    },
    2: {
        "name": "Mike",
        "age": 22,
    },
    3: {
        "name": "Dave",
        "age": 19,
    },
    4: {
        "name": "Jim",
        "age": 19,
    },
    5: {
        "name": "Havier",
        "age": 13,
    }
}


def buildFriendship(personID): # :)
    randomID = random.choice(list(people.keys()))

    while (randomID == personID):
        randomID = random.choice(list(people.keys()))

    return {
        "edge": [personID, randomID],
        "weight": random.random()
    }

# Autobuild friend network
friendships = list(map(buildFriendship, list(people.keys())))

# printDict(people)
# printDict(friendships)
