# Importing BaseModel and Field from Pydantic
# BaseModel -> Used to create data models with validation
# Field     -> (not used here) but helpful when you want default values, constraints, descriptions
from pydantic import BaseModel, Field

# Typing imports:
# List, Dict     -> For type hinting collections (lists, dictionaries)
# Optional       -> For optional fields (can be None)
# Annotated      -> Used in Pydantic v2+ for advanced validations (like constraints)
from typing import List, Dict, Optional, Annotated


# Define a Pydantic model for a Patient
# - Every attribute is automatically validated by Pydantic
# - Example: if you try to pass 'age="twenty"', Pydantic will throw an error
class Patient(BaseModel):
    name: str   # Must be a string
    age: int    # Must be an integer


# Example dictionary representing patient info
# This will be used to create a Patient object
patient_info = {'name': 'Sohom', 'age': 21}


# Function to insert patient data
# - Accepts only a Patient object
# - Ensures that invalid data can't be passed accidentally
def insert_patient_data3(patient: Patient):
    print(patient.name)  # Access patient name safely
    print(patient.age)   # Access patient age safely
    print("Inserted")    # Simulation of inserting into DB


# Function to update patient data
# - Similar to insert but represents updating an existing record
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Updated")


# Create a Patient instance from dictionary using unpacking (**)
# - Validates fields at creation
# - patient_1 is guaranteed to have correct types
patient_1 = Patient(**patient_info)
