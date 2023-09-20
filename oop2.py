# محاسیه مساحت و محیط مستطیل--------------
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def Circumference(self):
        return 2 * (self.length + self.width)

    def Area(self):
        return self.length * self.width


rectangle1 = Rectangle(20, 30)
area = rectangle1.Area()
circumference = rectangle1.Circumference()

