import random


class IdNumberGenerator:
    """"" Class to create ID number according to Lithuanian ID number reglament """
    def __init__(self): #  f"Hello, {name}. You are {age}."
        self.name = input("Please write your name: ")
        self.id = ''.join(["{}".format(random.randint(0, 9)) for number in range(0, 10)])

Participant = Totalizator()
print(Participant.id)