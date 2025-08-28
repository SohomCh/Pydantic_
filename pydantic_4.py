from pydantic import (
    BaseModel, EmailStr, AnyUrl, Field,
    field_validator, model_validator, computed_field
)
from typing import List, Dict


# ------------------------------------------------
# Patient Model with Field Validators, Model Validators & Computed Fields
# ------------------------------------------------
class Patient(BaseModel):
    name: str
    email: EmailStr
    linkedin_url: AnyUrl
    age: int
    weight: float
    height: float = Field(..., gt=0)   # ✅ Required, must be > 0
    married: bool = False
    allergies: List[str]
    contact_details: Dict[str, str]

    # -------------------------
    # Field Validator Example
    # -------------------------
    # Runs validation logic on a single field.
    # Use when you want to enforce constraints or transform values.
    @field_validator("email")
    @classmethod
    def email_validator(cls, value: str) -> str:
        valid_domains = ['hdfc.com', 'icici.com']
        domain_name = value.split('@')[1]
        if domain_name not in valid_domains:
            raise ValueError("❌ Invalid domain name. Must be from HDFC or ICICI.")
        return value

    @field_validator("name")
    @classmethod
    def name_caps(cls, value: str) -> str:
        # Transform name → UPPERCASE
        return value.upper()

    # -------------------------
    # Model Validator Example
    # -------------------------
    # Runs validation logic on the WHOLE model (all fields together).
    # Use when a rule depends on multiple fields.
    @model_validator(mode="after")
    def check_emergency_contact(self):
        if self.age > 60 and 'emergency' not in self.contact_details:
            raise ValueError("❌ Emergency contact is required for patients above 60.")
        return self

    # -------------------------
    # Computed Field Example
    # -------------------------
    # Virtual fields that are NOT stored but calculated on the fly.
    # Use when a field depends on others (like BMI from weight + height).
    @computed_field
    @property
    def bmi(self) -> float:
        return round((self.weight / (self.height / 100) ** 2), 2)


# ------------------------------------------------
# Example Usage
# ------------------------------------------------
patient_info = {
    'name': 'Sohom',
    'email': 'sohom@hdfc.com',
    'linkedin_url': 'https://linkedin.com/in/sohom',
    'age': 65,
    'weight': 70.5,
    'height': 175,
    'married': False,
    'allergies': ['pollen', 'dust'],
    'contact_details': {
        'phone': '1234567890',
        'emergency': '9876543210'  # ✅ Required if age > 60
    }
}

patient_1 = Patient(**patient_info)
print("✅ Patient Created:", patient_1)
print("✅ BMI:", patient_1.bmi)


# ------------------------------------------------
# Update Function Example
# ------------------------------------------------
def update_patient(patient: Patient):
    print("Updating patient...")
    print("Name:", patient.name)
    print("Age:", patient.age)


update_patient(patient_1)
print("✅ Patient Updated:", patient_1)