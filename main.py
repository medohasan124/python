students = [
    {"name": "Ali", "grade": 75},
    {"name": "Sara", "grade": 60},
    {"name": "Omar", "grade": 92}
]

result = [ {i["name"],i["grade"] } for i in students if i["grade"] >= 50]

print(result)