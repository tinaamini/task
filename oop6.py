# ساختار داده ساده-----------------------
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def display_info(self):
        print(self.name, "taken", self.score)


student1 = Student('ali', 20)
student1.display_info()
