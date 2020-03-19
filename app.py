from random import random


class IdNumberGenerator:
    """"" Class to create ID number according to Lithuanian ID number reglament """
    def __init__(self, f_name, l_name, gender): 
        self.f_name = f_name
        self.l_name = l_name
        self.gender = gender


    def birthday(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    

    def randomiser(self):   # ''.join(["{}".format(random.randint(0, 9)) for number in range(0, 10)]) -- randomized for last 4 digits
        pass
    
    @classmethod
    def user_input(cls):
        return cls(
            input("Please enter your first name: ").title(),
            input("Please enter your last name: ").title(),
            input("Please enter your gender: ").title())

user_id = IdNumberGenerator.user_input()
print(user_id.f_name)       #  f"Hello, {name}. You are {age}."
