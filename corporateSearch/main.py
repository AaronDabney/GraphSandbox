from collections import deque
import requests
import json 
import random

def generatePerson():
    url = 'https://randomuser.me//api'
    headers = {'Accept' : 'application/json'}

    response =(requests.get(url, headers)).json()["results"][0]

    # Delete unneeded properties
    del response["login"]
    del response["picture"]
    del response["registered"]
    del response["nat"]
    del response["id"]
    del response["location"]
    del response["dob"]
    del response["email"]
    del response["phone"]
    del response["cell"]
    del response["gender"]

    # Add a reports property
    response["reports"] = []

    return response


# Returns nested dictonary
def generateOrganizationHiearchy(numEmployees):
    iter = 1
    # Employees are assigned an id property equal to their order of creation
    root = generatePerson() 
    root["id"] = iter
    queue = deque([root])
    
    while (len(queue) > 0 and iter < numEmployees):
        currentEmployee = queue.popleft()
        reports = []
        for i in range(random.randint(2, 4)):
            iter += 1
            newEmployee = generatePerson()
            newEmployee["id"] = iter
            currentEmployee["reports"].append(newEmployee)
            queue.append(newEmployee)
    
    return root 


def calculateReportNum(orgRoot, targetEmployeeID):
    # Guard clause
    if not orgRoot:
        print("WARNING: Invalid input")
        return -1
    
    # Init bfs queue
    queue = deque([orgRoot])
    
    # Find target employee
    targetEmployee = None
    while len(queue) > 0:
        currentNode = queue.popleft()
        if currentNode["id"] == targetEmployeeID:
            targetEmployee = currentNode
            break
        for report in currentNode["reports"]:
            queue.append(report)

    # Count is -1 for employees not in organization
    if targetEmployee == None:
        print("WARNING: Employee does not exist")
        return -1
    
    # Reset bfs queue
    queue = deque([targetEmployee])

    # Tally reports
    reportsNum = 0
    while(len(queue) > 0):
        currentNode = queue.popleft()
        for report in currentNode["reports"]:
            queue.append(report)
            reportsNum += 1

    return reportsNum




# -- Testing -- #

orgRoot = generateOrganizationHiearchy(7)

print("Example organization: ")
print(json.dumps(orgRoot, indent=4))
print('\n')

print("Calculate Subreport test:")
employeeID = 1
subReportCount = calculateReportNum(orgRoot, employeeID)
print(f"Employee with ID:{employeeID} is responsible for {subReportCount} report(s)")
print('\n')

print("Empty dict test: ")
orgRootEmpty = {}
print(calculateReportNum(orgRootEmpty, 2))
print('\n')

print("Nonexistent employeeID test: ")
print(calculateReportNum(orgRoot, 20))
print('\n')

print("Employee with no reports test: ")
employeeID = 7
subReportCount = calculateReportNum(orgRoot, employeeID)
print(f"Employee with ID:{employeeID} is responsible for {subReportCount} report(s)")
print('\n')

# Note: Characters in random names are often represented in console with escape characters due to alternate unicode formats. i.e. Arabic, Mongolian, Mandarin

# Output -> 
# Example organization: 
# {
#     "name": {
#         "title": "Mr",
#         "first": "Rodoljub",
#         "last": "Viloti\u0107"
#     },
#     "reports": [
#         {
#             "name": {
#                 "title": "Mr",
#                 "first": "William",
#                 "last": "Pena"
#             },
#             "reports": [
#                 {
#                     "name": {
#                         "title": "Miss",
#                         "first": "Emma",
#                         "last": "Alvarez"
#                     },
#                     "reports": [],
#                     "id": 6
#                 },
#                 {
#                     "name": {
#                         "title": "Mr",
#                         "first": "Noah",
#                         "last": "Lavigne"
#                     },
#                     "reports": [],
#                     "id": 7
#                 }
#             ],
#             "id": 2
#         },
#         {
#             "name": {
#                 "title": "Mr",
#                 "first": "Amaury",
#                 "last": "Brunet"
#             },
#             "reports": [],
#             "id": 3
#         },
#         {
#             "name": {
#                 "title": "Miss",
#                 "first": "Inaya",
#                 "last": "Giraud"
#             },
#             "reports": [],
#             "id": 4
#         },
#         {
#             "name": {
#                 "title": "Ms",
#                 "first": "Judith",
#                 "last": "Caldwell"
#             },
#             "reports": [],
#             "id": 5
#         }
#     ],
#     "id": 1
# }


# Calculate Subreport test:
# Employee with ID:1 is responsible for 6 report(s)


# Empty dict test: 
# WARNING: Invalid input
# -1


# Nonexistent employeeID test: 
# WARNING: Employee does not exist
# -1


# Employee with no reports test: 
# Employee with ID:7 is responsible for 0 report(s)
