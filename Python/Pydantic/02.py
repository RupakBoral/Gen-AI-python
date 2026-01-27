from pydantic import BaseModel, Field

class Employee(BaseModel):
    id: int
    first_name: str = Field(
        ...,
        min_length=2,
        max_length=50,
        description="Employee Name",
        examples="Rupak",
    )
    last_name: str = Field(
        default="N/A"
    )
    salary: float = Field(
        ...,
        ge=10000, # greater than equal to 10,000
    )
    
dummy1 = {
    "id": 1,
    "first_name": "Rupak",
    "last_name": "Boral",
    "salary": 45000
}    
    
emp1 = Employee(**dummy1)

print(emp1)
