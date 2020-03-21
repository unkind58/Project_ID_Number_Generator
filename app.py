class IdNumberGenerator:
    """"" Class to create ID number according to Lithuanian ID number regulation """
    version = "[0.4]"

    def __init__(self,):
        pass


class Name:
    def __init__(self, f_name: str, l_name: str, gender: str):
        self.f_name = f_name
        self.l_name = l_name
        self.gender = gender

    @classmethod
    def input_user_name(cls):
        return cls(
            "".join(input("Please enter your first name: ").split()).title(),
            "".join(input("Please enter your last name: ").split()).title(),
            "".join(input("Please enter your gender: ").split()).title()
        )


class Birthday:
    def __init__(self, year: int, month: int, day: int):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def input_user_birthday(cls):
        return cls(
            int(input("Please enter your year of birth: ")),
            int(input("Please enter your month of birth: ")),
            int(input("Please enter your day of birth: "))
        )


user_id = Name.input_user_name()
user_id_birthday = Birthday.input_user_birthday()
print(user_id.f_name)

# --------------- The starting  output of ID itself ---------------
numbers_in_id  = 11
output_id = [0] * numbers_in_id

# --------------- 1st digit of ID (male/female) ---------------

if user_id.gender == "Male":
    if 1900 <= user_id_birthday.year <= 1999:
        output_id[0] = 3
    else:
        output_id[0]= 4
if user_id.gender == "Female":
    if 1900 <= user_id_birthday.year <= 1999:
        output_id[0] = 5
    else:
        output_id[0] = 6

# --------------- 2nd-3rd digit of ID (full year) ---------------
if len(user_id_birthday.year) == 4:
    output_id.append(user_id_birthday.year % 100)
else:
    output_id.append(19)
    output_id.append(user_id_birthday.year)

# --------------- 4th-5th digit of ID (month) ---------------
if len(user_id_birthday.month) == 2:
    output_id.append(user_id_birthday.month)
else:
    output_id.append(0)
    output_id.append(user_id_birthday.month)

# --------------- 6th-7th digit of ID (day)---------------
if len(user_id_birthday.day) == 2:
    output_id.append(user_id_birthday.day)
else:
    output_id.append(0)
    output_id.append(user_id_birthday.day)  # DRY ?????????

# --------------- 8th-10th digit of ID ( ascending  order)---------------
# TBA
# --------------- 11th digit of ID ( unique number)---------------
# TBA


# Additional possible features:

# (1) Making .txt with id generated in it
# (2) List of dates when you can marry/buy alco/play in casino/start president campaign/etc...