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


user_id = IdNumberGenerator.input_user_name()
#user_id_birthday = IdNumberGenerator.input_user_birthday()         (DOESN`T WORK, maybe need second class [???])
print(user_id.f_name)
print(user_id.create_last_4_digits())



# --------------- The starting  output of ID itself ---------------

output_id = []

# --------------- 1st digit of ID (male/female) ---------------

if user_id.gender == "Male":
    output_id.append(3)
else:
    output_id.append(4)

# --------------- 2nd-3rd digit of ID (full year) ---------------
if len(user_id.year) == 4:
    output_id.append(user_id.year % 100)
else:
    output_id.append(19)
    output_id.append(user_id.year)

# --------------- 4th-5th digit of ID (month) ---------------
if len(user_id.month) == 2:
    output_id.append(user_id.month)
else:
    output_id.append(0)
    output_id.append(user_id.month)

# --------------- 6th-7th digit of ID (day)---------------
if len(user_id.day) == 2:
    output_id.append(user_id.day)
else:
    output_id.append(0)
    output_id.append(user_id.day)                   # DRY ?????????

# --------------- 8th-11th digit of ID ( random / by growing order)---------------

output_id.append(user_id.last_digits)


# Additional possible features:

# (1) Making .txt with id generated in it
# (2) List of dates when you can marry/buy alco/play in casino/start president campaign/etc...