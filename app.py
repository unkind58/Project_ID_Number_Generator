import random

numbers_in_id = 11
output_id = [0] * numbers_in_id

class IdNumberGenerator:
    """"" Class to create ID number according to Lithuanian ID number regulation """
    version = "[0.5]"

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
            eval(input("Please enter your year of birth: ")),
            eval(input("Please enter your month of birth: ")),
            eval(input("Please enter your day of birth: "))
        )


user_id = Name.input_user_name()
user_id_birthday = Birthday.input_user_birthday()
#print(user_id.f_name)
#print(user_id_birthday.year)

# ------------- rearranging year -------------

if len(str(user_id_birthday.year)) == 4:
    pass
if len(str(user_id_birthday.year)) == 2:
    year = eval(input("Please enter 4 digit year expression: "))

# ------------- 1st digit ------------- [+]

if len(str(user_id_birthday.year)) == 4 and user_id_birthday.year in range(1900, 1999):
    if user_id.gender.startswith("M"):
        output_id[0] = 3
    else:
        output_id[0] = 4
if len(str(user_id_birthday.year)) == 4 and user_id_birthday.year in range(2000, 2999):
    if user_id.gender.startswith("W") and 1900 <= user_id_birthday.year <= 1999:
        output_id[0] = 6
    else:
        output_id[0] = 5

# ------------- 2nd-3rd digit ------------- [+]

output_id[1] = user_id_birthday.year % 100 // 10
output_id[2] = user_id_birthday.year % 10

# ------------- 4th-5th digit ------------- [+]

months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}
try:
    if int(user_id_birthday.month):
        pass
except ValueError:
    try:
        if str(user_id_birthday.month):
            month = months.get(user_id_birthday.month)
    except ValueError:
        year = eval(input("Please enter valid month expression: "))

if len(str(user_id_birthday.month)) == 1:
    output_id[3] = 0
    output_id[4] = user_id_birthday.month
else:
    output_id[3] = user_id_birthday.month // 10
    output_id[4] = user_id_birthday.month % 10

# ------------- 6th-7th digit ------------- [+]

if len(str(user_id_birthday.day)) == 1:
    output_id[5] = 0
    output_id[6] = user_id_birthday.day
else:
    output_id[5] = user_id_birthday.day // 10
    output_id[6] = user_id_birthday.day % 10

# ------------- 8th-10th digit ------------- [+]

sequence = str("".join(["{}".format(random.randint(0, 9)) for i in range(0, 3)]))
output_id[7] = eval(sequence[0])
output_id[8] = eval(sequence[1])
output_id[9] = eval(sequence[2])

# ------------- 11th digit -------------
counter = 1
last_digit = 0
for digit in range(len(output_id) - 1):
    if counter == 10:
        counter = 1
    last_digit += output_id[digit] * counter
    counter += 1
# print(last_digit)
counter = 3
if last_digit % 11 != 10:
    output_id[10] = last_digit % 11
else:
    last_digit = 0
    for digit in range(len(output_id) - 1):
        if counter == 10:
            counter = 1
        last_digit += output_id[digit] * counter
        counter += 1
if last_digit % 11 != 10:
    output_id[10] = last_digit % 11
else:
    output_id[10] = 0
# print(last_digit)

print(output_id)


# Additional possible features:

# (1) Making .txt with id generated in it
# (2) List of dates when you can marry/buy alco/play in casino/start president campaign/etc...