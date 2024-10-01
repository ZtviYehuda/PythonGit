from datetime import datetime

class Student:
    def __init__(self, name, year, id):
        self.name = name
        self.year = year
        self.id = id

    def age_student(self):
        current_year = datetime.now().year
        return current_year - self.year

    def len_of_name(self):
        langth_name = len(self.name)
        return langth_name

    def __str__(self):


print(Student)