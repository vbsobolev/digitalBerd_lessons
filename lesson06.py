class Human:
    hands: int
    foots: int
    head: int
    eyes: int
    age: int
    sex: int
    name: str

    def __init__(self, v_name='Ivan'):
        self.hands = 2
        self.foots = 2
        self.head = 1
        self.eyes = 2
        self.age = 30
        self.sex = 1
        self.name = v_name

    def mobilize(self):
        if self.sex == 1:
            self.hands = int(self.hands / 2)
            self.foots = int(self.foots / 2)
            self.eyes = int(self.eyes / 2)

    def see_info(self):
        print(f'\nname  =  {str(self.name)}')
        print(f'hands =  {str(self.hands)}')
        print(f'foots =  {str(self.foots)}')
        print(f'head  =  {str(self.head)}')
        print(f'eyes  =  {str(self.eyes)}')
        print(f'age   =  {str(self.age)}')
        print(f'sex   =  {str(self.sex)}')

    def __str__(self):
        return self.name + ' ' + str(self.age)


class Woman(Human):  # Наследуем от класса Human
    def __init__(self, v_name='Glasha'):
        super().__init__(v_name)
        self.sex = 0
        self.cycle = 28

    def see_info(self):
        super().see_info()
        print(f"cycle =  {str(self.cycle)}")


o_petya = Human("Petya")
o_petya.see_info()
o_vasya = Human(v_name="Vasya")
o_vasya.see_info()
o_vasya.mobilize()
o_vasya.see_info()
print(f'\n{o_vasya}')
o_masha = Woman("Masha")
o_masha.see_info()
print(f'\nMasha\'s age = {o_masha.age}')
