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



orgRoot = generateOrganizationHiearchy(7)
employeeID = 1
subReportCount = calculateReportNum(orgRoot, employeeID)


print("Organization: ")
print(json.dumps(orgRoot, indent=4))
print('\n')
print(f"Employee #{employeeID} is responsible for {subReportCount} report(s)")

# Note: Characters in random names are often represented in console with escape characters due to alternate unicode formats. i.e. Arabic, Mongolian, Mandarin

# Output -> 
# Organization: 
# {
#     "name": {
#         "title": "Ms",
#         "first": "\u0641\u0627\u0637\u0645\u0647 \u0632\u0647\u0631\u0627",
#         "last": "\u0639\u0644\u06cc\u0632\u0627\u062f\u0647"
#     },
#     "reports": [
#         {
#             "name": {
#                 "title": "Monsieur",
#                 "first": "Ethan",
#                 "last": "Barbier"
#             },
#             "reports": [
#                 {
#                     "name": {
#                         "title": "Mr",
#                         "first": "Crist\u00f3bal",
#                         "last": "Moreno"
#                     },
#                     "reports": [],
#                     "id": 6
#                 },
#                 {
#                     "name": {
#                         "title": "Mr",
#                         "first": "\u0645\u062d\u0645\u062f\u0627\u0645\u064a\u0646",
#                         "last": "\u0632\u0627\u0631\u0639\u06cc"
#                     },
#                     "reports": [],
#                     "id": 7
#                 },
#                 {
#                     "name": {
#                         "title": "Mr",
#                         "first": "Brede",
#                         "last": "Furre"
#                     },
#                     "reports": [],
#                     "id": 8
#                 },
#                 {
#                     "name": {
#                         "title": "Mrs",
#                         "first": "Sofia",
#                         "last": "Kristensen"
#                     },
#                     "reports": [],
#                     "id": 9
#                 }
#             ],
#             "id": 2
#         },
#         {
#             "name": {
#                 "title": "Mr",
#                 "first": "Owen",
#                 "last": "Rodriguez"
#             },
#             "reports": [],
#             "id": 3
#         },
#         {
#             "name": {
#                 "title": "Mr",
#                 "first": "Rasmus",
#                 "last": "Petersen"
#             },
#             "reports": [],
#             "id": 4
#         },
#         {
#             "name": {
#                 "title": "Ms",
#                 "first": "Eylem",
#                 "last": "Bogaers"
#             },
#             "reports": [],
#             "id": 5
#         }
#     ],
#     "id": 1
# }


# Employee #1 is responsible for 8 report(s)