from collections import deque
import requests
import json 
import random


def generate_person():
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
def generate_organization_hiearchy(num_employees):
    iter = 1
    # Employees are assigned an id property equal to their order of creation
    root = generate_person() 
    root["id"] = iter
    queue = deque([root])
    
    while (len(queue) > 0 and iter < num_employees):
        current_employee = queue.popleft()
        reports = []
        for i in range(random.randint(2, 4)):
            iter += 1
            new_employee = generate_person()
            new_employee["id"] = iter
            current_employee["reports"].append(new_employee)
            queue.append(new_employee)
    
    return root 


def calculate_report_num(org_root, target_employee_ID):
    # Guard clause
    if not org_root:
        print("WARNING: Invalid input")
        return -1
    
    # Init bfs queue
    queue = deque([org_root])
    
    # Find target employee
    target_employee = None
    while len(queue) > 0:
        current_node = queue.popleft()
        if current_node["id"] == target_employee_ID:
            target_employee = current_node
            break
        for report in current_node["reports"]:
            queue.append(report)

    # Count is -1 for employees not in organization
    if target_employee == None:
        print("WARNING: Employee does not exist")
        return -1
    
    # Reset bfs queue
    queue = deque([target_employee])

    # Tally reports
    reports_num = 0
    while(len(queue) > 0):
        current_node = queue.popleft()
        for report in current_node["reports"]:
            queue.append(report)
            reports_num += 1

    return reports_num




# -- Testing -- #

org_root = generate_organization_hiearchy(7)

print("Example organization: ")
print(json.dumps(org_root, indent=4))
print('\n')

print("Calculate Subreport test:")
employee_ID = 1
sub_report_count = calculate_report_num(org_root, employee_ID)
print(f"Employee with ID:{employee_ID} is responsible for {sub_report_count} report(s)")
print('\n')

print("Empty dict test: ")
org_root_empty = {}
print(calculate_report_num(org_root_empty, 2))
print('\n')

print("Nonexistent employeeID test: ")
print(calculate_report_num(org_root, 20))
print('\n')

print("Employee with no reports test: ")
employee_ID = 7
sub_report_count = calculate_report_num(org_root, employee_ID)
print(f"Employee with ID:{employee_ID} is responsible for {sub_report_count} report(s)")
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
