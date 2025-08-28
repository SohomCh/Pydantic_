from pydantic import BaseModel, Field  # ✅ Pydantic's BaseModel for data validation and serialization
from typing import List, Dict


# ------------------------------
# Nested Models Example
# ------------------------------
# When one model contains another model inside it.
# Useful for structured data like Patient → Address.
class Address(BaseModel):
    city: str
    state: str
    pin: str


class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address   # 👈 Nested model inside Patient


# Example dictionaries for initialization
address_dict = {'city': 'Durgapur', 'state': 'West Bengal', 'pin': '722207'}
patient_dict = {'name': 'Sohom', 'gender': 'Male', 'age': 30, 'address': address_dict}

# Create instances
address1 = Address(**address_dict)
patient_1 = Patient(**patient_dict)

print("✅ Full Patient Object (with nested Address):")
print(patient_1)


# ------------------------------
# Exclude Example
# ------------------------------
# The "exclude" parameter lets you drop certain fields
# while dumping a model into a dict.
# Useful when you don’t want to expose sensitive/unnecessary data (like 'state').
temp = patient_1.model_dump(exclude={'address': {'state'}})  
# 👆 Correct syntax: nested exclude uses a dictionary
# Here we are excluding the "state" field inside "address".

print("\n✅ Patient Dict after Excluding 'state' from address:")
print(temp)
print(type(temp))


# ------------------------------
# Exclude Unset Example
# ------------------------------
# "exclude_unset=True" excludes fields that were NOT provided at initialization.
# Useful for PATCH/partial updates where you only want changed fields.
class User(BaseModel):
    username: str
    email: str | None = None
    age: int | None = None


user = User(username="Alice")  
# 👆 Only "username" was set, others remain unset (None).

print("\n✅ Default User Dict:")
print(user.model_dump())

print("\n✅ User Dict with exclude_unset=True:")
print(user.model_dump(exclude_unset=True))  
# 👆 Only includes fields that were actually provided (username).
