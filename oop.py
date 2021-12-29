class Stanok:
    def __init__(self, name = "это главный станок", time = "10 минут", materials = 10):
        self.name = name
        self.time = time
        self.materials = materials

    def display_info(self):
        print("Название: {}, Время создания: {}, Материалов нужно: {}".format(self.name, self.time, self.materials))

class AutoStanok(Stanok):
    def __init__(self, name = "стандартная деталь автомобиля", time = "15 минут", materials = 15):
        self.name = name
        self.time = time
        self.materials = materials

class PlaneStanok(Stanok):
    def __init__(self, name = "стандартная деталь самолета", time = "25 минут", materials = 14):
        self.name = name
        self.time = time
        self.materials = materials

class ShipStanok(Stanok):
    def __init__(self, name = "стандартная деталь корабля", time = "1 час", materials = 20):
        self.name = name
        self.time = time  
        self.materials = materials
        
auto1 = AutoStanok()
auto1.display_info()
auto2 = AutoStanok(name = "педаль", time = "10 минут", materials=10)
auto2.display_info()
auto3 = AutoStanok()
auto3.display_info()
auto4 = AutoStanok(name = "аккумулятор", time = "20 минут", materials=30)
auto4.display_info()
auto5 = AutoStanok()
auto5.display_info()

plane1 = PlaneStanok()
plane1.display_info()
plane2 = PlaneStanok(name = "двигатель самолета", time = "2 часа", materials=50)
plane2.display_info()
plane3 = PlaneStanok()
plane3.display_info()
plane4 = PlaneStanok()
plane4.display_info()
plane5 = PlaneStanok(name = "крыло самолета", time = "3  часа", materials=60)
plane5.display_info()

ship1 = ShipStanok(name = "парус", time = "25 минут", materials=10)
ship1.display_info()
ship2 = ShipStanok()
ship2.display_info()
ship3 = ShipStanok(name = "якорь", time = "15 минут", materials=16)
ship3.display_info()
ship4 = ShipStanok()
ship4.display_info()
ship5 = ShipStanok()
ship5.display_info()