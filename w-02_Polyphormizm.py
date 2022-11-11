# Перегрузка
class Base:
    def __init__(self, a):
           self.aa = a

    def print_a (self, square, multipler = None):
        if square == True and not multipler:
            print(self.aa ** 2)
        elif square == False and multipler:
            print(self.aa * multipler)
        elif square == True and multipler:
            print(self.aa * 4)
        else:
            print(self.aa)

base = Base(4)
base.print_a (0)
base.print_a (square=True)
base.print_a (square=False, multipler=10)
base.print_a (square=True, multipler=5)

print('--------------------------------------------')

# Переопределение
class Multiplier:
    def __init__(self, a):
           self.a = a

    def print_a (self, x):
        print(self.a * x)

class Exponent (Multiplier):

    def print_a (self, x):
        print(self.a ** x)

mult = Multiplier (3)
mult.print_a(5)
expo = Exponent (3)
expo.print_a(2)


print('--------------------------------------------')

class Paralelogram:
    def __init__(self, w, h):
           self.w = w
           self.h = h

    def get_area (self):
        return self.w * self.h

class Square(Paralelogram):

    def get_area (self):
        return self.w ** 2

w_ = 2
h_ = 2
paral = Paralelogram (w_,h_)
sq = Square(w_,h_)

print (paral.get_area()) if w_ != h_ else print (sq.get_area())



print('--------------------------------------------')

def fn_detect (data, new_value):
    if isinstance (data, list):
        data.append(new_value)
    elif isinstance (data, set):
        data.add(new_value)
    elif isinstance (data, str):
        if isinstance (new_value, str):
            data += new_value
    return data
    
print (fn_detect ("1", 2))
