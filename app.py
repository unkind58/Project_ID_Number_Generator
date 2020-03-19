from random import randint


class IdNumberGenerator:
    """"" Class to create ID number according to Lithuanian ID number regulation """
    version = "[0.1]"

    def __init__(self, f_name, l_name, gender): #  f"Hello, {f_name}. You are {age}."
        self.f_name = f_name
        self.l_name = l_name
        self.gender = gender


    def birthday(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    #def randomiser(self, last_digits):
    #    self.last_digits = last_digits

    @classmethod
    def input_user_name(cls):
        return cls(
            input("Please enter your first name: ").title(),
            input("Please enter your last name: ").title(),
            input("Please enter your gender: ").title())

    @staticmethod
    def create_last_4_digits():
        last_digits = "".join(["{}".format(randint(0, 9)) for i in range(0, 4)])
        return last_digits


 #   @classmethod
 #   def input_user_birthday(cls):
 #       return cls.birthday()
 #           input("Please enter your year of birth: ").title(),
 #           input("Please enter your month of birth: ").title(),
 #           input("Please enter your day of birth: ").title())


user_id_name = IdNumberGenerator.input_user_name()
#user_id_birthday = IdNumberGenerator.input_user_birthday()
print(user_id_name.f_name)
print(user_id_name.create_last_4_digits())