import application.salary
import db.people
from application import *
from db import *

db.people.get_employees()
application.salary.calculate_salary()

# """Тут не совсем понял, правильно ли сделал, сначало импортировал всё из пакетов через
# * . Далее при использовании функций PyCharm сам импортировал application.salary
# и db.people"""








