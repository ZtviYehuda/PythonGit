from datetime import datetime

class Student:
    def __init__(self, name, year, id):
        self.name = name
        self.year = year
        self.id = id

    def age_student(self):
        current_year = datetime.now().year
        age = (current_year - self.year)
        return age

    def len_of_name(self):
        langth_name = len(self.name)
        return langth_name

    def __str__(self):
        return f"name = {self.name} year =  {self.year} id = {self.id}"

s = Student("ztvi", 2000, "17297999")
print(s)
