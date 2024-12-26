class Student:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def display(self):
        print("Student ID",self.id)
        print("Student Name",self.name)
def main():
      id = input("Enter Student ID: ")
      name = input("Enter Student Name: ")
      stu=Student(id,name)
      stu.display()
main()