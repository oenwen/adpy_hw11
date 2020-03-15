from _datetime import date
from adpy_hw11.application import salary
from adpy_hw11.application.db import people

if __name__ == '__main__':
    print(date.today())
    people.get_employees()
    salary.calculate_salary()




