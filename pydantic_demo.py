from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = 'Vedant'
    age: Optional[int] = None # default value if age is not given it will give none
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10)  # greater than (gt) and less than(lt)
    # we can add default value  and description as well
new_student = {'age': '32', 'email': 'abc@gmail.com', 'cgpa': 5}
student = Student(**new_student)
print(student)