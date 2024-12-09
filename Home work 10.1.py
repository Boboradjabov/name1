class Vehicle:
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year
    def display_info(self):
        print('Транспортное средство – это техническое устройство, предназначенное для перемещения людей, грузов или оборудования, установленного на нем')
baybay=Vehicle('car',1666)
baybay.display_info()
print(baybay.year,baybay.brand)
class Car(Vehicle):
    def __init__(self,brand,year,model):
        super().__init__(brand,year)
        self.model=model
    def display_info(self):
        print('\n\nPorsche 911 (нем. Neunelfer) — общее название семейства спортивных автомобилей и автомобилей категории GT,\nвыпускающихся немецкой компанией Porsche AG с 1965 года по настоящее время. \nПоколения семейства принято разделять на Porsche 911 Classic, выпускавшихся в 1964-1989 годах, и автомобили нового поколения,\nсохранивших с семейством Classic лишь общую компоновку и внешнюю стилистику.\nОтствующие в модельной линейке Porsche с 1967 года по настоящее время (2024 год).')
car911=Car(year='year:2021 год',brand='Porsche',model='model:Porsche 911 GT3')
car911.display_info()
print(car911.brand,car911.model,car911.year)
class Motorcycle(Vehicle):
    def __init__(self,brand,year,speed,):
        super().__init__(brand,year,)
        self.speed=speed
    def display_info(self):
        print('--------------------------------------------------------------------------------------------------------------------------------\n\nKawasaki Ninja H2 — это четырехтактный мотоцикл класса суперспорт с наддувом из серии спортивных мотоциклов Ninja ,\nвыпускаемый компанией Kawasaki , оснащенный центробежным нагнетателем с переменной скоростью .')
kawasaki=Motorcycle('Kawasaki Ninja H2','year:2015 год','speed:380–400km/h')
kawasaki.display_info()
print(kawasaki.brand,kawasaki.speed,kawasaki.year)