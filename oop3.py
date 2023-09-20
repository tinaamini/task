# -------------inheritance
class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type


class Cat(Animal):
    def __init__(self, food, voice, name='cat', type='mammal'):
        super().__init__(name, type)
        self.food = food
        self.voice = voice


class Dog(Animal):
    def __init__(self, food, voice):
        super().__init__('dog', 'mammal')
        self.food = food
        self.voice = voice


animal1 = Animal('lion', 'mammal')
animal2 = Cat('mouse', 'Meow,Meow...')
animal3 = Dog('meat', 'Hup!Hup!')
