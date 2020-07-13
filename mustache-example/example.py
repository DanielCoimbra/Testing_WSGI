import pystache

data = {
    "items": [
        {"name": "Name 1", "description": "Description 1", "sale": True},
        {"name": "Name 2", "description": "Description 2", "sale": False},
    ]
}

with open("example.html.mustache") as template:
    result = pystache.render(template.read(), data)

print(result)
