head = {
    "value": 11,
    "next": {
        "value": 3,
        "next": {
            "value": 23,
            "next": {
                "value": 7,
                "next": {"value": 2, "next": None},
            },
        },
    },
}


print(head["next"]["next"]["next"]["value"])

# This will aonly run with a linked list
print(head)