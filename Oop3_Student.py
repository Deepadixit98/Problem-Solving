"""Problem Statement
A university wants to automate their admission process. Students are admitted based on marks scored in a qualifying exam.
A student is identified by student id, age and marks in qualifying exam. Data are valid, if:

1.Age is greater than 20
2.Marks is between 0 and 100 (both inclusive)
3.A student qualifies for admission,Age and marks are valid and Marks is 65 or more

Write a python program to represent the students seeking admission in the university.
Validate marks and age.
If valid, check if marks is 65 or more.
If so return true
Else return false
Else return false
 
setter methods

Include setter methods for all instance variables to set its values

getter methods

Include getter methods for all instance variables to get its values

 """
class Student:
    def __init__(self):
        self.__student_id=None
        self.__marks=None
        self.__age=None

    def set_marks(self,marks):
        self.__marks=marks
    def set_age(self,age):
        self.__age=age
    def set_student_id(self,student_id):
        self.__student_id=student_id
    
    def get_student_id(self):
        return self.__student_id
    def get_marks(self):
        return self.__marks
    def get_age(self):
        return self.__age

    def validate_age(self):
        if self.__age > 20:
            print("Valid age")
        else:
            print("InValid age")    
    
    def validate_marks(self):
        if 0<=self.__marks<=100:
            print("Valid marks")
        else:
            print("InValid marks")    
    
    def check_qualification(self):
        if 0<=self.__marks<=100 and self.__age > 20 and self.__marks>=65:
            print("qualified") 
        else:
            print("Not qualified")     

s = Student()
s.set_marks(45)
s.set_age(20)
# s.set_student_id(101)
# s.get_student_id()
s.validate_age()   
s.validate_marks()
s.check_qualification()

# ends