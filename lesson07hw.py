# Во всех заданиях из lesson6hw используйте только приватные поля, геттеры и сеттеры:

import time


class Human:
    """Класс родительский Human для Child"""
    heads = 1
    bodies = 1
    hands = 2
    legs = 2
    tails = 0

    @classmethod
    def __check_name(cls, x):
        return type(x) is str

    @classmethod
    def __check_value(cls, x):
        return type(x) is int

    def __init__(self, name: str, age: int):
        self.__name = 'NoNameHuman'
        self.__age = 0
        if self.__check_name(name):
            self.__name = name
        if self.__check_value(age):
            self.__age = age

    def __str__(self):
        return f'Human - {self.__name} ( {str(self.__age)})'

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

class Dogs:
    heads = 1
    bodies = 1
    hands = 0
    legs = 4
    tails = 1

    @classmethod
    def __check_name(cls, x):
        return type(x) in str

    def __init__(self, name: str):
        self.__name = 'NoNameDog'
        if self.__check_name(name):
            self.name = name


class Cats:
    heads = 1
    bodies = 1
    hands = 0
    legs = 4
    tails = 1

    @classmethod
    def __check_name(cls, x):
        return type(x) in str

    def __init__(self, name: str):
        self.__name = 'NoNameCat'
        if self.__check_name(name):
            self.name = name


class Mice:
    pass


class Child(Human):
    @classmethod
    def __check_coordinates(cls, x):
        return type(x) is dict

    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.__name = name
        self.__age = age
        self.__coordinates = {'x': 0, 'y': 0}

    def __str__(self):
        return f'Child - {self.__name} ( {str(self.__age)})'

    def coordinates_print(self):
        print(f'{self.__name} ({str(self.__age)}): {self.__coordinates}')

    def coordinates_change(self, coordinates: dict):
        if self.__check_coordinates(coordinates):
            self.__coordinates = coordinates.copy()

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


class Bus:
    __wheels = 4

    @classmethod
    def __check_name(cls, x):
        return type(x) is str

    @classmethod
    def __check_value(cls, x):
        return type(x) is int

    @classmethod
    def __check_child(cls, x):
        return type(x) is Child

    def __init__(self, name: str, seats: int):
        self.__name = 'NoNameBus'
        self.__seats = 0
        if self.__check_name(name):
            self.__name = name
        if self.__check_value(seats):
            self.__seats = seats
        self.__passengers = []
        self.__coordinates = {'x': 0, 'y': 0}

    def __str__(self):
        return f'Bus - {self.__name} ({str(self.__seats)} seats)'

    def append_child(self, child: Child):
        if self.__check_child(child):
            self.__passengers.append(child)
            print(f'Passenger {child.get_name()} ({str(child.get_age())}) is appended to the bus {self.__name}')

    def remove_child(self, child: Child):
        if self.__check_child(child):
            self.__passengers.remove(child)
            print(f'Passenger {child.get_name()} ({str(child.get_age())}) is removed from the bus {self.__name}')

    def see_passengers(self):
        passengers_names = []
        for i in self.__passengers:
            passengers_names.append(i.get_name() + ' (' + str(i.get_age()) + ')')
        print(f'Passengers in {self.__name}: {str(passengers_names)}')

    def temp_coordinates(self):
        return self.__coordinates

    def write_children_coordinates(self):
        for i in self.__passengers:
            i.coordinates_change(self.__coordinates)
            i.coordinates_print()

    def get_name(self):
        return self.__name

    def get_seats(self):
        return self.__seats

    def set_seats(self, seats: int):
        self.__seats += seats

    def start_excursion(self):
        print(f'Start Excursion')
        ex_time = 0
        while ex_time < 3:
            time.sleep(1)
            self.__coordinates['x'] += 2
            self.__coordinates['y'] += 1
            ex_time += 1
            self.write_children_coordinates()
        while ex_time > 0:
            time.sleep(1)
            self.__coordinates['x'] -= 2
            self.__coordinates['y'] -= 1
            ex_time -= 1
            self.write_children_coordinates()
        print(f'Finish Excursion')


class BusService:
    @classmethod
    def __check_name(cls, x):
        return type(x) is str

    @classmethod
    def __check_value(cls, x):
        return type(x) is int

    @classmethod
    def __check_bus(cls, x):
        return type(x) is Bus

    def __init__(self, name: str, parking_spaces: int):
        self.__name = 'NoNameBusService'
        self.__parking_spaces = 0
        if self.__check_name(name):
            self.__name = name
        if self.__check_value(parking_spaces):
            self.__parking_spaces = parking_spaces
        self.__buses = []

    def see_info(self):
        buses_names = []
        for i in self.__buses:
            buses_names.append(i.get_name() + ' (' + str(i.get_seats()) + ')')
        print(buses_names)

    def append_bus(self, bus: Bus):
        if self.__check_bus(bus) is False:
            return None
        if self.__parking_spaces - len(self.__buses) > 0:
            self.__buses.append(bus)
            print(f'{bus.get_name()} is appended to the bus service')
        else:
            print('No spaces for the bus')

    def remove_bus(self, bus: Bus):
        if self.__check_bus(bus) is False:
            return None
        self.__buses.remove(bus)
        print(f'{bus.get_name()} is removed from the bus service')

    def get_buses_list(self):
        return self.__buses

    @staticmethod
    def change_seats(bus: Bus, seats: int):
        bus.set_seats = bus.get_seats() + seats
        if seats > 0:
            print(f'+ {seats} to {bus.get_name()}')
        elif seats < 0:
            print(f'{seats} to {bus.get_name()}')


print(f'\nСоздание объекта класса Human:')
print(Human.__doc__)
print(Human.__dict__)
oleg = Human('Oleg', 33)
print(oleg)
print(isinstance(oleg, Human))
print(oleg.__dict__)
print(getattr(oleg, '_Human__name'))  # метод получения аттрибутов (не желательно обращаться к этому аттрибуту)
print(setattr(oleg, '_Human__age', 34))  # метод установки аттрибутов (не желательно обращаться к этому аттрибуту)
print(oleg)

print(f'\nСоздание локальных аттрибутов для Human:')
oleg.nationality = 'Russian'
print(f'{oleg.get_name()} - {oleg.nationality}')

print(f'\nСоздание объектов отнаследованного класса Child:')
mitya = Child('Mitya', 9)
print(mitya)
zhorik = Child('Zhorik', 15)
print(zhorik)
katya = Child('Katya', 4)
print(katya)
anna = Child('Anna', 12)
print(anna)

print(f'\nСоздание объекта класса Bus:')
ikarus = Bus('Ikarus', 47)
print(f'{ikarus}')
volvo = Bus('Volvo', 17)
print(f'{volvo}')
buhanka = Bus('Buhanka', 7)
print(f'{buhanka}')

print(f'\nДобавление, удаление детей из автобуса')
ikarus.see_passengers()
ikarus.append_child(mitya)
ikarus.append_child(zhorik)
ikarus.append_child(katya)
ikarus.append_child(anna)
ikarus.see_passengers()
ikarus.remove_child(zhorik)
ikarus.see_passengers()

print(f'\nИзменение координат автобуса и, находящихся в нем, детей')
ikarus.start_excursion()

print(f'\nЗамена сидений у автобусов в сервисе:')
sto = BusService('STO', 2)
sto.append_bus(ikarus)
sto.append_bus(buhanka)
sto.append_bus(volvo)
sto.remove_bus(ikarus)
sto.append_bus(volvo)
print(sto.get_buses_list())
sto.see_info()
sto.change_seats(volvo, 6)
sto.change_seats(buhanka, -2)
sto.see_info()
