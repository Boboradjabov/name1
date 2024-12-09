class Animal:
  def make_sound(self):
        print('Эти животные издают звук')
  def rr(self):
      print('Кот муркает')
  def gav(self):
      print('собака гавкает')
  def muu(self):
      print('корова мычит')
animal1=Animal()
animal1.make_sound()
class Cat(Animal):
    def __init__(self,a):
        a=a
cat1=Cat
cat1.rr(animal1)
class Dog(Animal):
    def __init__(self,b):
        b=b
dag=Dog
dag.gav(animal1)
class Cow(Animal):
    def __init__(self,c):
        c=c
caw=Cow
caw.muu(animal1)