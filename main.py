from application import salary
from db import people
from datetime import date


if __name__ == '__main__':
    print(f'Hello! Today is {date.today()}!')
    salary.calculate_salary()
    people.get_employees()





