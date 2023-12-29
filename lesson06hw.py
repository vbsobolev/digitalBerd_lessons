# 2. Создайте несколько классов - например: человек и т.д.
# 3. От класса человек отнаследуйте класс "ребёнок"
# 4. Создайте класс "автобус". В автобусе должно содержаться несколько "детей" - например в list.
#    Для класса автобус напишите методы добавления ребёнка в автобус, удаления ребёнка из автобуса.
# 5. Для каждого ребёнка сделайте хранение его текущего местоположения и методы для его изменения/отображения.
#    У автобуса сделайте метод - при вызове которого будет меняться местоположение у всех детей,
#    кто в нём находится на заданное (новое положение передавать в метод изменения положения)
# 6. Проявите смекалку - и создайте ещё несколько классов,
#    которые будут содержать переменные других классов и делать что-нибудь забавное.

import time


class Human:
    name: str
    age: int

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return 'Human - ' + self.name + ' (' + str(self.age) + ')'


class Dogs:
    def __init__(self, name: str):
        self.name = name
        self.tails = 1


class Cats:
    def __init__(self, name: str):
        self.name = name
        self.tails = 1


class Child(Human):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.geo = {}

    def __str__(self):
        self.geo = {'x': 0, 'y': 0}
        return 'Child - ' + self.name + ' (' + str(self.age) + ')'

    def geo_print(self):
        print(f'{self.name} ({str(self.age)}): {self.geo}')

    def geo_change(self, geo: dict):
        self.geo = geo.copy()


class Bus:
    def __init__(self, name: str, seats: int):
        self.name = name
        self.seats = seats
        self.passengers = []
        self.geo = {'x': 0, 'y': 0}

    def __str__(self):
        return 'Bus - ' + self.name + ' (' + str(self.seats) + ' seats)'

    def append_child(self, child: Child):
        self.passengers.append(child)
        print('Passenger ' + child.name + ' (' + str(child.age) + ') is appended to the bus ' + self.name)

    def remove_child(self, child: Child):
        self.passengers.remove(child)
        print('Passenger ' + child.name + ' (' + str(child.age) + ') is removed from the bus ' + self.name)

    def see_passengers(self):
        passengers_names = []
        for i in self.passengers:
            passengers_names.append(i.name + ' (' + str(i.age) + ')')
        print('Passengers in ' + self.name + ': ' + str(passengers_names))

    def temp_geo(self):
        return self.geo

    def write_children_geo(self):
        for i in self.passengers:
            i.geo_change(self.geo)
            i.geo_print()

    def start_excursion(self):
        print(f'\nStart Excursion')
        ex_time = 0
        while ex_time < 3:
            time.sleep(1)
            self.geo['x'] += 2
            self.geo['y'] += 1
            ex_time += 1
            self.write_children_geo()
        while ex_time > 0:
            time.sleep(1)
            self.geo['x'] -= 2
            self.geo['y'] -= 1
            ex_time -= 1
            self.write_children_geo()
        print(f'Finish Excursion')


class BusService:
    def __init__(self, name: str, parking_spaces: int):
        self.name = name
        self.parking_spaces = parking_spaces
        self.buses = []

    def see_info(self):
        buses_names = []
        for i in self.buses:
            buses_names.append(i.name + ' (' + str(i.seats) + ')')
        print(buses_names)

    def append_bus(self, bus: Bus):
        if self.parking_spaces - len(self.buses) > 0:
            self.buses.append(bus)
            print(f'{bus.name} is appended to the bus service')
        else:
            print('No spaces for the bus')

    def remove_bus(self, bus: Bus):
        self.buses.remove(bus)
        print(f'{bus.name} is removed from the bus service')

    @staticmethod
    def change_seats(bus: Bus, seats: int):
        bus.seats += seats
        if seats > 0:
            print(f'+ {seats} to {bus.name}')
        elif seats < 0:
            print(f'{seats} to {bus.name}')


print(f'\nObjects:')
oleg = Human('Oleg', 33)
print(oleg)
oleg.nationality = 'Russian'
print(f'{oleg.name} - {oleg.nationality}')
mitya = Child('Mitya', 9)
print(mitya)
zhorik = Child('Zhorik', 15)
print(zhorik)
katya = Child('Katya', 4)
print(katya)
anna = Child('Anna', 12)
print(anna)
ikarus = Bus('Ikarus', 47)
print(f'{ikarus}')
volvo = Bus('Volvo', 17)
print(f'{volvo}')
buhanka = Bus('Buhanka', 7)
print(f'{buhanka}\n')

ikarus.see_passengers()
ikarus.append_child(mitya)
ikarus.append_child(zhorik)
ikarus.append_child(katya)
ikarus.append_child(anna)
ikarus.see_passengers()
ikarus.remove_child(zhorik)
ikarus.see_passengers()
ikarus.start_excursion()

print('')
sto = BusService('STO', 2)
sto.append_bus(ikarus)
sto.append_bus(buhanka)
sto.append_bus(volvo)
sto.remove_bus(ikarus)
sto.append_bus(volvo)
print(sto.buses)
sto.see_info()
sto.change_seats(volvo, 6)
sto.change_seats(buhanka, -2)
sto.see_info()
