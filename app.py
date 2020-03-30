import random


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
            "".join(input("Please enter your month of birth: ").split()).title(),
            eval(input("Please enter your day of birth: "))
        )


def intro():
    """"" Intro message """
    print("Dear sir/madam,\n"
          "Next you will be asked to enter your credentials in order to generate your ID number.")


def rearranging_year():
    """"" Rearranging year (from 2 to 4 digits) """
    if len(str(user_id_birthday.year)) == 4:
        pass
    if len(str(user_id_birthday.year)) == 2:
        user_id_birthday.year = eval(input("Please enter 4 digit year expression: "))


def rearranging_gender():
    """"" Rearranging gender (to be Male/Men or Female/Women) """
    if user_id.gender.startswith("M") or user_id.gender.startswith("W") or user_id.gender.startswith("F"):
        pass
    else:
        user_id.gender = "".join(input("Please enter Male or Female as your gender: ").split()).title()


def rearranging_month():
    """"" Rearranging month if was entered as string type """
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
        int(user_id_birthday.month)
    except ValueError:
        try:
            user_id_birthday.month = months[user_id_birthday.month]
        except KeyError:
            user_id_birthday.month = int(input("Please enter month in numerical expression: "))


def digit_1():
    """"" Initializing 1st digit """
    if len(str(user_id_birthday.year)) == 4 and user_id_birthday.year in range(1900, 1999):
        if user_id.gender.startswith("M"):
            output_id[0] = 3
        else:
            output_id[0] = 4
    if len(str(user_id_birthday.year)) == 4 and user_id_birthday.year in range(2000, 2999):
        if user_id.gender.startswith("F") or user_id.gender.startswith("W") and 1900 <= user_id_birthday.year <= 1999:
            output_id[0] = 6
        else:
            output_id[0] = 5


def digit_2to3():
    """"" Initializing 2nd and 3rd digit """
    output_id[1] = user_id_birthday.year % 100 // 10
    output_id[2] = user_id_birthday.year % 10


def digit_4to5():
    """"" Initializing 4th and 5th digit """
    if len(str(user_id_birthday.month)) == 1:
        output_id[3] = 0
        output_id[4] = int(user_id_birthday.month)
    else:
        output_id[3] = int(user_id_birthday.month) // 10
        output_id[4] = int(user_id_birthday.month) % 10


def digit_6to7():
    """"" Initializing 6th and 7th digit """
    if len(str(user_id_birthday.day)) == 1:
        output_id[5] = 0
        output_id[6] = user_id_birthday.day
    else:
        output_id[5] = user_id_birthday.day // 10
        output_id[6] = user_id_birthday.day % 10


def digit_8to10():
    """"" Initializing 8th, 9th and 10th digit """
    sequence = str("".join(["{}".format(random.randint(0, 9)) for i in range(0, 3)]))
    output_id[7] = eval(sequence[0])
    output_id[8] = eval(sequence[1])
    output_id[9] = eval(sequence[2])


def digit_11():
    """"" Initializing 11th digit """
    counter = 1
    last_digit = 0
    for digit in range(len(output_id) - 1):
        if counter == 10:
            counter = 1
        last_digit += output_id[digit] * counter
        counter += 1
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

def saving_to_txt_file():
    save_txt = input("Do you want to save you id number to .txt file?").title()
    if save_txt.startswith("Y"):
        with open(f"{user_id.f_name}_{user_id.l_name}.txt", "w") as file:
            file.write(f"Dear {user_id.f_name} {user_id.l_name}, your ID number is {''.join(map(str, output_id))}")
    else:
        print(f"{user_id.f_name} {user_id.l_name}, your ID number is {''.join(map(str, output_id))}")


if __name__ == "__main__":
    numbers_in_id = 11
    output_id = [0] * numbers_in_id
    intro()
    user_id = Name.input_user_name()
    rearranging_gender()
    user_id_birthday = Birthday.input_user_birthday()
    rearranging_year()
    rearranging_month()
    digit_1()
    digit_2to3()
    digit_4to5()
    digit_6to7()
    digit_8to10()
    digit_11()
    saving_to_txt_file()
    
# Additional possible features:
# (1) List of dates when you can marry/buy alcohol/play in casino/start president campaign/etc...
# (2) Send email (finding @)
