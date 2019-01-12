import json #import the javascript

# a Python object (dict):
x = {
  "name": "Ranjith",
  "age": 21,
  "city": "India"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)




x = {
  "name": "Ranjith",
  "age": 31,
  "married": True,
  "divorced": False,
  "children": ("kumar","Roy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))