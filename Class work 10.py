class Worker:
    def __init__(self,name=0,age=0):
        self.name=name
        self.age=age
    def work(self,a):
        self.name+=a
        print('Имя работника добавлен')
    def worker(self,b):
        self.age+=b
        print('Возраст работника добавлен')
worker=Worker()