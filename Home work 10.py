class Animal():
    def __init__(self,sound=''):
        self.sound = sound

    def make_sound(self):
        print(f'{self.sound}')

class Cat(Animal):
    def __init__(self,sound='may'):
        super().__init__(sound)

Cat().make_sound()