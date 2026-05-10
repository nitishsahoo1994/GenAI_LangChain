from langchain_text_splitters import RecursiveCharacterTextSplitter,Language


splitter=RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=400,
    chunk_overlap=0
)

text="""class Student:

    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print("Name :", self.name)
        print("Age  :", self.age)
        print("Marks:", self.marks)

    def is_pass(self):
        if self.marks >= 40:
            return "Pass"
        else:
            return "Fail"


# Creating objects
student1 = Student("Nitish", 22, 85)
student2 = Student("Rahul", 21, 35)

# Display details
student1.display()
print("Result:", student1.is_pass())

print("------------------")

student2.display()
print("Result:", student2.is_pass())"""


res=splitter.split_text(text)
print(type(res))
print(len(res))