import pandas as pd
import logging

print(pd)
print(pd.__file__)

file = '/Users/lionel/PyCharmMiscProject/check.csv'


df = pd.read_csv(file, encoding='unicode_escape', nrows = 1000)


logging.basicConfig(
    filename ='/jsn.txt',
    level = logging.DEBUG,
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

def is_positive_number(number):
    logging.debug(f"checking if {number} is positive number")
    if number > 0:
        logging.info(f"{number} is positive number")
    else:
        logging.warning(f"{number} is negative number")

