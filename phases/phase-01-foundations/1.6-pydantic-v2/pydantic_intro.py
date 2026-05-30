from pydantic import BaseModel


class Student(BaseModel):
    name: str
    age: int
    percentage: float


def print_info(student: Student):
    print(student.name)
    print(student.age)
    print(student.percentage)


Student_info = {"name": "Abdurrehman", "age": 21, "percentage": 89.90}

Student1 = Student(**Student_info)
print_info(Student1)
