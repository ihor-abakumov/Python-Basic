class User:
    def __init__(self, age, name, user_type):
           self.age = age
           self.name = name
           self.user_type = user_type
    
    def access_database (self):
        if self.user_type == 'superuser':
            print('access granted') 
        else:
            print('access denied')

class SuperUser (User):

    def access_database (self):
        print('access level_god')

print ('-------------------------------------------')

user_access = User (age='33', name = 'Jesus', user_type = 'superur')
user_access.access_database ()

user_access_1 = SuperUser (age='33', name = 'Jesus', user_type = 'superuser')
user_access_1.access_database ()

print ('-------------------------------------------')

