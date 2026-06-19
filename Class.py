from datetime import datetime as dt,date
from dateutil.relativedelta import relativedelta


class Myage:
    def __init__(self, dob, name):
        self.__dob = dt.strptime(dob, '%Y-%m-%d')
        self.__name = name
        self.__age = relativedelta(date.today(), self.__dob).years

    def show_me_age(self):
        return f"{self.__name} is {self.__age} years old"

age = Myage("1993-01-01", "Anu")
print(age.show_me_age())
