# استفاده از متد همگانی----------------------------
class Rectangle2:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

# method Overriding
class Square(Rectangle2):
    def __init__(self, length, width):
        super().__init__(length, width)

    def calculate_area(self):
        return self.length * self.width