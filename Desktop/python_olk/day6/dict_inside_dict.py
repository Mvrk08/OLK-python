data = {
    "user1": {
        "name": "Alice",
        "age": 25,
        "skills": {
            "python": "advanced",
            "javascript": "intermediate"
        }
    },
    "user2": {
        "name": "Bob",
        "age": 30,
        "skills": {
            "python": "beginner",
            "java": "advanced"
        }
    }
}

# print(data["user1"])
# print(data["user2"]["skills"])
# print(data["user2"]["age"])

for name,skills in  data.items() :
    print(f"name={name} , you got these skills :{skil ls}")