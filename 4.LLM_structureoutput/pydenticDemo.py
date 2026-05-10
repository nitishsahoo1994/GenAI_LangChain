from pydantic import BaseModel,EmailStr,Field
from typing import Optional


class Student(BaseModel):
    name:str ='nitish'
    age:Optional[int]=None
    cgpa: float = Field(gt=0,lt=10,description="It's a decimal "
                                              "value representing the cgpa of that person")


new_student={'age':'32','cgpa':'5'}

student1=Student(**new_student)
print(student1)