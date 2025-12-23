class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(f"Student name is {self.name} and age of the student is {self.age}")

s1 = Student('Dumraliya Pratik',20)
s1.show()

