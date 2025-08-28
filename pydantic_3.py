from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):
    # ✅ Correct Annotated syntax: Annotated[type, constraints]
    name: Annotated[str, Field(max_length=50, min_length=2, title="Name of the patient", description="This is the name of the patient")]
    ### we can use Field to add more validation like here name should be between 2 to 50 characters

    email: EmailStr
    ### insted of using regex we can use EmailStr from pydantic

    linkedin_url: AnyUrl
    ### AnyUrl ensures the input is a valid URL (http/https)

    age: int = Field(..., gt=0, lt=150)
    ### we can use Field to add more validation like here age should be greater than 0 and less than 150

    weight: Annotated[float, Field(..., gt=0, lt=300, strict=True)]
    ### we can use Field to add more validation like here weight should be greater than 0 and less than 300
    ### strict=True ensures type is EXACT float (not coercible from string)

    marraied: bool = False
    ##$ dafalult value is false

    allergies: Optional[List[str]] = None
    ### we used this because of two level validation as it is list as well the content is a string
    ### Optional means the entire list can be None

    contact_detaild: Dict[str, str]
    ### dictionary type ensures both keys & values must be strings

    ### All the fields are required by default
    ### we can make them optional by using Optional from typing module


# ------------------------------------------------
# Example Data
# ------------------------------------------------
patient_info = {
    'name': 'Sohom',
    'email': 'sohom@gmail.com',          # ✅ must be valid EmailStr
    'linkedin_url': 'https://linkedin.com/in/sohom',  # ✅ must be valid URL
    'age': 21,
    'weight': 70.5,
    'marraied': False,
    'allergies': ['pollen', 'dust'],
    'contact_detaild': {'email': 'sohom', 'phone': '1234567890'}
}


# ------------------------------------------------
# Example Functions
# ------------------------------------------------
def insert_patient_data3(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Inserted")


def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Updated")


# ------------------------------------------------
# Creating Patient object
# ------------------------------------------------
patient_1 = Patient(**patient_info)
insert_patient_data3(patient_1)
update_patient_data(patient_1)
