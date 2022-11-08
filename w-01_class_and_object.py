class Human:
    def __init__(self, age, name, gender) -> None:
           self.age = age
           self.name = name
           self.gender = gender
    def get_name (self):
        return self.name
    def get_age_and_name (self):
        return self.age, self.name, self.get_name()


human_1 = Human (age=25, name='John', gender = 'male')
print(human_1.age, human_1.name, human_1.gender)
print(human_1.get_name()) 
print(human_1.get_age_and_name())



class Humann:
    def __init__(self, age):
           self.age = age

    def say_hello (self):
        print("Hello? I am {}".format(self.age))


human_2 = Humann(age=35)
human_2.say_hello()


class HumanExtented(Humann):
    def __init__(self, age, name):
        super().__init__(age)
        self.name = name

    def say_hello (self):
        print("Hello? My name {}".format(self.name))



human_3 = HumanExtented(age=54, name='Igor')
human_3.say_hello()
print(human_3.age, human_3.name)


class A:
    def __init__(self) -> None:
         self.a = 10

class B:
    def  __init__(self) -> None:
         self.b = 20

class C (A,B):
    def __init__(self, c):
        A.__init__(self)
        B.__init__(self)
        self.c = c
        

d = C(50)
print(d.a,d.b,d.c)


print('-----------------------')

class Car:
    def __init__(self, brand, color, volume) -> None:
        self.brand = brand
        self.color = color
        self.volume = volume

    def move_left(self):
        print("Car {} {} {} move left".format(self.brand, self.color,self.volume))

    def move_right(self):
        print("Car {} {} {} move right".format(self.brand, self.color,self.volume))
    
    @staticmethod
    def move_stop():
        print("Car stop")

my_car = Car(brand="Opel", color="black", volume=2)
my_car.move_left ()
my_car.move_right ()
my_car.move_stop ()
Car.move_stop

class CarExtented(Car):
    @staticmethod
    def move_forward():
        print("Car forward")

    @staticmethod
    def move_back():
        print("Car back")

print('-----------------------')

carr = CarExtented("Opel", "black", 2)
carr.move_back()
carr.move_forward()
carr.move_left()
carr.move_right()
carr.move_stop()


class Fly:
    def __init__(self, model) -> None:
        self.model = model
     
    def fly_flying(self):
        print("Fly {} flying".format(self.model))

    def fly_land(self):
        print("Fly {} landing".format(self.model))

print('-----------------------')

fly_my = Fly('Boing')
fly_my.fly_flying()


class FlyCar (CarExtented, Fly):
    def __init__(self, brand, color, volume, model):
        CarExtented.__init__(self, brand, color, volume)
        Fly.__init__(self, model)

print('-----------------------')
fly_car = FlyCar (brand='zaz', color='white', volume=3, model='ukravia')
fly_car.move_back()
fly_car.move_forward()
fly_car.move_stop()
fly_car.move_left()
fly_car.move_right()
fly_car.fly_flying()
fly_car.fly_land()







