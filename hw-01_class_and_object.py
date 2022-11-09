class Cat:
    def __init__(self, color, cat_type):
           self.size = 'undefined'
           self.color = color
           self.cat_type = cat_type
    
    def set_size (self):
        if self.cat_type == 'indoor':
            self.size = 'small'


my_cat = Cat (color='white', cat_type = 'indoor')

print ('-------------------------------------------')

print(f"This is cat {my_cat.cat_type} it's color {my_cat.color} and size {my_cat.size}")
my_cat.set_size()
print(f"If this is cat {my_cat.cat_type} and color {my_cat.color} then size {my_cat.size}")


class Tiger(Cat):
    
    def set_size (self):
        if self.cat_type == 'wild':
            self.size = 'big'


my_cat_2 = Tiger (color='white', cat_type = 'wild')

print ('-------------------------------------------')

print(f"This is cat {my_cat_2.cat_type} it's color {my_cat_2.color} and size {my_cat_2.size}")
my_cat_2.set_size()
print(f"If this is cat {my_cat_2.cat_type} and color {my_cat_2.color} then size {my_cat_2.size}")
