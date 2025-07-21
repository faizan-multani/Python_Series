# Pydantic : 
- Pydantic is a powerful data validation and settings management library for Python, built on top of Python type hints. It allows you to define data models using standard Python types and provides automatic parsing and validation of incoming data.

## ✅ Key Features of Pydantic :
- Data validation based on Python type annotations.

- Automatic conversion of input data (e.g., converting strings to integers).

- Clear error messages when validation fails.

- Nested models and complex structures.

- Supports JSON Schema generation.

- Used heavily in modern web frameworks like FastAPI.

## Basic Example :
```
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    signup_ts: str | None = None
    friends: list[int] = []

data = {
    'id': '123',
    'name': 'Alice',
    'friends': [1, '2', 3]
}

user = User(**data)

print(user)
print(user.id)         # 123 (converted from string to int)
print(user.friends)    # [1, 2, 3] (strings converted to integers)

```

##  Validation Errors Example :
```
from pydantic import ValidationError

try:
    User(id='not-a-number', name=123)
except ValidationError as e:
    print(e)
#Output: 2 validation errors:
#id
#  value is not a valid integer (type=type_error.integer)
# name
#  str type expected (type=type_error.str)

```

## 🧩 Nested Models Example :
```
class Address(BaseModel):
    city: str
    country: str

class Person(BaseModel):
    name: str
    address: Address

data = {
    "name": "Bob",
    "address": {
        "city": "New York",
        "country": "USA"
    }
}

person = Person(**data)
print(person.address.city)  # New York

```

## 📦 Why Use Pydantic ?
- Cleaner, declarative way to manage structured data.

- Less manual validation code.

- Widely used in APIs (e.g., FastAPI).

- Ensures type safety and data integrity.