🐍 Pydantic Revision Guide

Pydantic is a Python library for data validation and settings management using Python type hints. It ensures that the data you work with is valid, structured, and type-safe.

🔑 Key Concepts
1. BaseModel

All Pydantic models inherit from BaseModel.

Defines schema + validation for your data.

from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int


✅ Patient(name="Sohom", age=21) → valid
❌ Patient(name="Sohom", age="21") → auto converts "21" → 21 (type coercion)

2. Data Validation & Type Conversion

Pydantic automatically validates & converts types.

class Example(BaseModel):
    num: int
    is_active: bool

ex = Example(num="123", is_active="True")
print(ex)  # num=123, is_active=True

3. Field (extra validation & metadata)

Field() lets you add constraints, defaults, descriptions.

from pydantic import BaseModel, Field

class Patient(BaseModel):
    name: str = Field(..., min_length=2, max_length=50, description="Full name")
    age: int = Field(..., gt=0, lt=120, description="Age in years")
🐍 Pydantic Revision Guide

Pydantic is a Python library for data validation and settings management using Python type hints. It ensures that the data you work with is valid, structured, and type-safe.

🔑 Key Concepts
1. BaseModel

All Pydantic models inherit from BaseModel.

Defines schema + validation for your data.

from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int


✅ Patient(name="Sohom", age=21) → valid
❌ Patient(name="Sohom", age="21") → auto converts "21" → 21 (type coercion)

2. Data Validation & Type Conversion

Pydantic automatically validates & converts types.

class Example(BaseModel):
    num: int
    is_active: bool

ex = Example(num="123", is_active="True")
print(ex)  # num=123, is_active=True

3. Field (extra validation & metadata)

Field() lets you add constraints, defaults, descriptions.

from pydantic import BaseModel, Field

class Patient(BaseModel):
    name: str = Field(..., min_length=2, max_length=50, description="Full name")
    age: int = Field(..., gt=0, lt=120, description="Age in years")

4. Optional & Default Values

Use Optional or = None for nullable fields.

from typing import Optional

class Patient(BaseModel):
    name: str
    email: Optional[str] = None

5. Nested Models

Models can include other models → hierarchical validation.

class Address(BaseModel):
    city: str
    zipcode: int

class Patient(BaseModel):
    name: str
    address: Address

p = Patient(name="Sohom", address={"city": "Kolkata", "zipcode": 700001})

6. Lists & Dicts

Use List, Dict for collections.

from typing import List, Dict

class Patient(BaseModel):
    name: str
    medicines: List[str]
    test_results: Dict[str, float]

7. Model Methods
p = Patient(name="Sohom", age=21)

# Convert to dict/JSON
print(p.dict())   # {'name': 'Sohom', 'age': 21}
print(p.json())   # '{"name": "Sohom", "age": 21}'

# Create from dict with unpacking
patient_info = {"name": "Sohom", "age": 21}
p2 = Patient(**patient_info)

8. Validators

Add custom validation logic with @validator.

from pydantic import validator

class Patient(BaseModel):
    name: str
    age: int

    @validator("age")
    def check_age(cls, value):
        if value < 0:
            raise ValueError("Age must be positive")
        return value

9. Annotated Types (Extra Constraints)

Annotated combines types + constraints.

from typing import Annotated
from pydantic import Field

Age = Annotated[int, Field(gt=0, lt=120)]

class Patient(BaseModel):
    age: Age

10. Using Models in Functions

Pydantic models are great for function parameters & validation.

def insert_patient_data(patient: Patient):
    print(f"Inserted {patient.name}, {patient.age}")

p = Patient(name="Sohom", age=21)
insert_patient_data(p)

🚀 Why Use Pydantic?

✔️ Automatic validation & conversion
✔️ Easy to work with APIs & JSON
✔️ Great with FastAPI (built on Pydantic)
✔️ Clean, maintainable, type-safe code

⚡ Quick Recap🐍 Pydantic Revision Guide

Pydantic is a Python library for data validation and settings management using Python type hints. It ensures that the data you work with is valid, structured, and type-safe.

🔑 Key Concepts
1. BaseModel

All Pydantic models inherit from BaseModel.

Defines schema + validation for your data.

from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int


✅ Patient(name="Sohom", age=21) → valid
❌ Patient(name="Sohom", age="21") → auto converts "21" → 21 (type coercion)

2. Data Validation & Type Conversion

Pydantic automatically validates & converts types.

class Example(BaseModel):
    num: int
    is_active: bool

ex = Example(num="123", is_active="True")
print(ex)  # num=123, is_active=True

3. Field (extra validation & metadata)

Field() lets you add constraints, defaults, descriptions.

from pydantic import BaseModel, Field

class Patient(BaseModel):
    name: str = Field(..., min_length=2, max_length=50, description="Full name")
    age: int = Field(..., gt=0, lt=120, description="Age in years")

4. Optional & Default Values

Use Optional or = None for nullable fields.

from typing import Optional

class Patient(BaseModel):
    name: str
    email: Optional[str] = None

5. Nested Models

Models can include other models → hierarchical validation.

class Address(BaseModel):
    city: str
    zipcode: int

class Patient(BaseModel):
    name: str
    address: Address

p = Patient(name="Sohom", address={"city": "Kolkata", "zipcode": 700001})

6. Lists & Dicts

Use List, Dict for collections.

from typing import List, Dict

class Patient(BaseModel):
    name: str
    medicines: List[str]
    test_results: Dict[str, float]

7. Model Methods
p = Patient(name="Sohom", age=21)

# Convert to dict/JSON
print(p.dict())   # {'name': 'Sohom', 'age': 21}
print(p.json())   # '{"name": "Sohom", "age": 21}'

# Create from dict with unpacking
patient_info = {"name": "Sohom", "age": 21}
p2 = Patient(**patient_info)

8. Validators

Add custom validation logic with @validator.

from pydantic import validator

class Patient(BaseModel):
    name: str
    age: int🐍 Pydantic Revision Guide

Pydantic is a Python library for data validation and settings management using Python type hints. It ensures that the data you work with is valid, structured, and type-safe.

🔑 Key Concepts
1. BaseModel

All Pydantic models inherit from BaseModel.

Defines schema + validation for your data.

from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int


✅ Patient(name="Sohom", age=21) → valid
❌ Patient(name="Sohom", age="21") → auto converts "21" → 21 (type coercion)

2. Data Validation & Type Conversion

Pydantic automatically validates & converts types.

class Example(BaseModel):
    num: int
    is_active: bool

ex = Example(num="123", is_active="True")
print(ex)  # num=123, is_active=True

3. Field (extra validation & metadata)

Field() lets you add constraints, defaults, descriptions.

from pydantic import BaseModel, Field

class Patient(BaseModel):
    name: str = Field(..., min_length=2, max_length=50, description="Full name")
    age: int = Field(..., gt=0, lt=120, description="Age in years")

4. Optional & Default Values

Use Optional or = None for nullable fields.

from typing import Optional

class Patient(BaseModel):
    name: str
    email: Optional[str] = None

5. Nested Models

Models can include other models → hierarchical validation.

class Address(BaseModel):
    city: str
    zipcode: int

class Patient(BaseModel):
    name: str
    address: Address

p = Patient(name="Sohom", address={"city": "Kolkata", "zipcode": 700001})

6. Lists & Dicts

Use List, Dict for collections.

from typing import List, Dict

class Patient(BaseModel):
    name: str
    medicines: List[str]
    test_results: Dict[str, float]

7. Model Methods
p = Patient(name="Sohom", age=21)

# Convert to dict/JSON
print(p.dict())   # {'name': 'Sohom', 'age': 21}
print(p.json())   # '{"name": "Sohom", "age": 21}'

# Create from dict with unpacking
patient_info = {"name": "Sohom", "age": 21}
p2 = Patient(**patient_info)

8. Validators

Add custom validation logic with @validator.
🐍 Pydantic Revision Guide

Pydantic is a Python library for data validation and settings management using Python type hints. It ensures that the data you work with is valid, structured, and type-safe.

🔑 Key Concepts
1. BaseModel

All Pydantic models inherit from BaseModel.

Defines schema + validation for your data.

from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int


✅ Patient(name="Sohom", age=21) → valid
❌ Patient(name="Sohom", age="21") → auto converts "21" → 21 (type coercion)

2. Data Validation & Type Conversion

Pydantic automatically validates & converts types.

class Example(BaseModel):
    num: int
    is_active: bool

ex = Example(num="123", is_active="True")
print(ex)  # num=123, is_active=True

3. Field (extra validation & metadata)

Field() lets you add constraints, defaults, descriptions.

from pydantic import BaseModel, Field

class Patient(BaseModel):
    name: str = Field(..., min_length=2, max_length=50, description="Full name")
    age: int = Field(..., gt=0, lt=120, description="Age in years")

4. Optional & Default Values

Use Optional or = None for nullable fields.

from typing import Optional

class Patient(BaseModel):
    name: str
    email: Optional[str] = None

5. Nested Models

Models can include other models → hierarchical validation.

class Address(BaseModel):
    city: str
    zipcode: int

class Patient(BaseModel):
    name: str
    address: Address

p = Patient(name="Sohom", address={"city": "Kolkata", "zipcode": 700001})

6. Lists & Dicts

Use List, Dict for collections.

from typing import List, Dict

class Patient(BaseModel):
    name: str
    medicines: List[str]
    test_results: Dict[str, float]

7. Model Methods
p = Patient(name="Sohom", age=21)

# Convert to dict/JSON
print(p.dict())   # {'name': 'Sohom', 'age': 21}
print(p.json())   # '{"name": "Sohom", "age": 21}'

# Create from dict with unpacking
patient_info = {"name": "Sohom", "age": 21}
p2 = Patient(**patient_info)

8. Validators

Add custom validation logic with @validator.

from pydantic import validator

class Patient(BaseModel):
    name: str
    age: int

    @validator("age")
    def check_age(cls, value):
        if value < 0:
            raise ValueError("Age must be positive")
        return value

9. Annotated Types (Extra Constraints)

Annotated combines types + constraints.

from typing import Annotated
from pydantic import Field

Age = Annotated[int, Field(gt=0, lt=120)]

class Patient(BaseModel):
    age: Age

10. Using Models in Functions

Pydantic models are great for function parameters & validation.

def insert_patient_data(patient: Patient):
    print(f"Inserted {patient.name}, {patient.age}")

p = Patient(name="Sohom", age=21)
insert_patient_data(p)

🚀 Why Use Pydantic?

✔️ Automatic validation & conversion
✔️ Easy to work with APIs & JSON
✔️ Great with FastAPI (built on Pydantic)
✔️ Clean, maintainable, type-safe code

⚡ Quick Recap

Use BaseModel → define schema

Use Field → add rules (min/max, default, descriptions)

Use Optional, List, Dict, Nested Models → structure data

Use .dict() / .json() → convert models

Use @validator → custom checks

Use Annotated → cleaner constraints
from pydantic import validator

class Patient(BaseModel):
    name: str
    age: int

    @validator("age")
    def check_age(cls, value):
        if value < 0:
            raise ValueError("Age must be positive")
        return value

9. Annotated Types (Extra Constraints)

Annotated combines types + constraints.

from typing import Annotated
from pydantic import Field

Age = Annotated[int, Field(gt=0, lt=120)]

class Patient(BaseModel):
    age: Age

10. Using Models in Functions

Pydantic models are great for function parameters & validation.

def insert_patient_data(patient: Patient):
    print(f"Inserted {patient.name}, {patient.age}")

p = Patient(name="Sohom", age=21)
insert_patient_data(p)

🚀 Why Use Pydantic?

✔️ Automatic validation & conversion
✔️ Easy to work with APIs & JSON
✔️ Great with FastAPI (built on Pydantic)
✔️ Clean, maintainable, type-safe code

⚡ Quick Recap

Use BaseModel → define schema

Use Field → add rules (min/max, default, descriptions)

Use Optional, List, Dict, Nested Models → structure data

Use .dict() / .json() → convert models

Use @validator → custom checks

Use Annotated → cleaner constraints

    @validator("age")
    def check_age(cls, value):
        if value < 0:
            raise ValueError("Age must be positive")
        return value

9. Annotated Types (Extra Constraints)

Annotated combines types + constraints.

from typing import Annotated
from pydantic import Field

Age = Annotated[int, Field(gt=0, lt=120)]

class Patient(BaseModel):
    age: Age

10. Using Models in Functions

Pydantic models are great for function parameters & validation.

def insert_patient_data(patient: Patient):
    print(f"Inserted {patient.name}, {patient.age}")

p = Patient(name="Sohom", age=21)
insert_patient_data(p)

🚀 Why Use Pydantic?

✔️ Automatic validation & conversion
✔️ Easy to work with APIs & JSON
✔️ Great with FastAPI (built on Pydantic)
✔️ Clean, maintainable, type-safe code

⚡ Quick Recap

Use BaseModel → define schema

Use Field → add rules (min/max, default, descriptions)

Use Optional, List, Dict, Nested Models → structure data

Use .dict() / .json() → convert models

Use @validator → custom checks

Use Annotated → cleaner constraints

Use BaseModel → define schema

Use Field → add rules (min/max, default, descriptions)

Use Optional, List, Dict, Nested Models → structure data

Use .dict() / .json() → convert models

Use @validator → custom checks

Use Annotated → cleaner constraints
4. Optional & Default Values

Use Optional or = None for nullable fields.

from typing import Optional

class Patient(BaseModel):
    name: str
    email: Optional[str] = None

5. Nested Models

Models can include other models → hierarchical validation.

class Address(BaseModel):
    city: str
    zipcode: int

class Patient(BaseModel):
    name: str
    address: Address

p = Patient(name="Sohom", address={"city": "Kolkata", "zipcode": 700001})

6. Lists & Dicts

Use List, Dict for collections.

from typing import List, Dict

class Patient(BaseModel):
    name: str
    medicines: List[str]
    test_results: Dict[str, float]

7. Model Methods
p = Patient(name="Sohom", age=21)

# Convert to dict/JSON
print(p.dict())   # {'name': 'Sohom', 'age': 21}
print(p.json())   # '{"name": "Sohom", "age": 21}'

# Create from dict with unpacking
patient_info = {"name": "Sohom", "age": 21}
p2 = Patient(**patient_info)

8. Validators

Add custom validation logic with @validator.

from pydantic import validator

class Patient(BaseModel):
    name: str
    age: int

    @validator("age")
    def check_age(cls, value):
        if value < 0:
            raise ValueError("Age must be positive")
        return value

9. Annotated Types (Extra Constraints)

Annotated combines types + constraints.

from typing import Annotated
from pydantic import Field

Age = Annotated[int, Field(gt=0, lt=120)]

class Patient(BaseModel):
    age: Age

10. Using Models in Functions

Pydantic models are great for function parameters & validation.

def insert_patient_data(patient: Patient):
    print(f"Inserted {patient.name}, {patient.age}")

p = Patient(name="Sohom", age=21)
insert_patient_data(p)

🚀 Why Use Pydantic?

✔️ Automatic validation & conversion
✔️ Easy to work with APIs & JSON
✔️ Great with FastAPI (built on Pydantic)
✔️ Clean, maintainable, type-safe code

⚡ Quick Recap

Use BaseModel → define schema

Use Field → add rules (min/max, default, descriptions)

Use Optional, List, Dict, Nested Models → structure data

Use .dict() / .json() → convert models

Use @validator → custom checks

Use Annotated → cleaner constraintsgit branch -M main
git push -u origin main
