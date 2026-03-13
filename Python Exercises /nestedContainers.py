# ============================================
# NESTED CONTAINERS PRACTICE (NO SOLUTIONS)
# ============================================

# RULES:
# - Do NOT print the whole structure unless needed
# - Write your answers as Python expressions or statements
# - Use indexing, keys, membership tests, and assignment
# - Comment out each answer after you're done if you want to retry later


# ---------------------------
# EXERCISE 1: Lists & Tuples
# ---------------------------
data1 = [5, 10, (15, 20), 25]

# Q1: Access the value 15
print(data1[2][0])
# Q2: Access the value 20
print(data1[2][1])


# ---------------------------
# EXERCISE 2: Dict with List
# ---------------------------
data2 = {
    "user": "Sam",
    "scores": [70, 85, 90]
}

# Q1: Access the value 85
print(data2["scores"][1])
# Q2: Change the last score to 95
data2["scores"][-1]=95
print(data2)


# ---------------------------
# EXERCISE 3: List of Dicts
# ---------------------------
data3 = [
    {"id": 1, "colors": ("red", "blue")},
    {"id": 2, "colors": ("green", "yellow")}
]

# Q1: Access "yellow"
print(data3[1]["colors"][1])
# Q2: Access the id of the first dictionary
print(data3[0]["id"])

# ---------------------------
# EXERCISE 4: Dict with List & Set
# ---------------------------
data4 = {
    "employees": [
        {"name": "Alice", "skills": {"python", "sql"}},
        {"name": "Bob", "skills": {"excel"}}
    ]
}

# Q1: Access "Bob"
print(data4["employees"][1]["name"])
# Q2: Check if "python" is in Alice's skills
print("python" in data4["employees"][0]["skills"])


# ---------------------------
# EXERCISE 5: Realistic Nesting
# ---------------------------
data5 = {
    "store": {
        "products": [
            {"name": "pen", "prices": [1.5, 1.7]},
            {"name": "notebook", "prices": [3.0, 3.5]}
        ]
    }
}

# Q1: Access the second price of "notebook"
print(data5["store"]["products"][1]["prices"][1])
# Q2: Change the first price of "pen" to 2.0
data5["store"]["products"][0]["prices"][1]=2.0
print(data5["store"]["products"][0]["prices"][1])

# ---------------------------
# EXERCISE 6: Tuple + Dict + List
# ---------------------------
data6 = [
    ("teamA", {"scores": [10, 20, 30]}),
    ("teamB", {"scores": [40, 50, 60]})
]

# Q1: Access the value 50
# Q2: Replace 60 with 65


# ---------------------------
# EXERCISE 7: Deep Nesting
# ---------------------------
data7 = {
    "school": {
        "classes": [
            {
                "name": "math",
                "students": [
                    {"name": "Eva", "grades": (90, 95)},
                    {"name": "Leo", "grades": (85, 88)}
                ]
            }
        ]
    }
}

# Q1: Access Leo's second grade
# Q2: Change Eva's first grade to 92


# ---------------------------
# EXERCISE 8: Mixed Everything
# ---------------------------
data8 = [
    {
        "group": "X",
        "members": (
            {"id": 1, "tags": {"a", "b"}},
            {"id": 2, "tags": {"c"}}
        )
    }
]

# Q1: Access the tag "c"
# Q2: Check if "a" is in the first member's tags


# ---------------------------
# EXERCISE 9: Mutation Check
# ---------------------------
data9 = {
    "config": (
        {"modes": ["on", "off"]},
        {"modes": ["auto", "manual"]}
    )
}

# Q1: Access "manual"
# Q2: Change "off" to "disabled"


# ---------------------------
# EXERCISE 10: Think Carefully
# ---------------------------
data10 = [
    {"a": [1, {"b": (2, 3)}]},
    {"c": ({4, 5}, {"d": [6, 7]})}
]

# Q1: Access the value 3
print(data10[0]["a"][1]["b"][1])
# Q2: Access the value 7
# Q3: Check if 4 is in the set
