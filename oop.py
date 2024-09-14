class Student: 
    Name = ""
    Age = 12
    Teacher_name = "Mrs Bhavana"
    school = "SuttonGrammarSchool"
    House = "Warwick"
    Class = "year 7"

    def __init__(self):
        print("making a new student")

    def changedetales(self):
        print("Please enter your age.")
        self.Age=input()
        print("Please enetr the name of the student.")
        self.Name=input()

    def showdetales(self):
        print("The detales of the students are")
        print(self.Name)
        print(self.Age)
        print(self.Teacher_name)
        print(self.school)
        print(self.Class)
        print(self.House)
    
Ahmadjon = Student()
Ahmadjon.changedetales()
Ahmadjon.showdetales()