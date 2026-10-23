employees = [
    {"name": "Ali", "score": 90, "exp": 5},
    {"name": "Sara", "score": 95, "exp": 3},
    {"name": "Usman", "score": 90, "exp": 7},
    {"name": "Hina", "score": 90, "exp": 5},
    {"name": "Bilal", "score": 80, "exp": 10},
]
ranked = sorted(employees, key=lambda e: (-e["score"], -e["exp"], e["name"]))

for number, e in enumerate(ranked, start=1):
    print(number, e["name"], e["score"], e["exp"])

by_name = sorted(ranked, key=lambda e: e["name"])

def find(name):
    low = 0
    high = len(by_name) - 1
    while low <= high:
        mid = (low + high) // 2
        if by_name[mid]["name"] == name:
            return by_name[mid]
        elif by_name[mid]["name"] < name:
            low = mid + 1          
        else:
            high = mid - 1         
    return None

print(find("Hina"))
print(find("Rahul"))
