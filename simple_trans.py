
import datetime
from dateutil.relativedelta import relativedelta
import random

products = 10
months = 14
currentDateTime = datetime.datetime.now()

for m in range(0, months):
    prev_month  = datetime.datetime.now() - relativedelta(months=m)
    #print prev_month.strftime('%m%Y')

    for p in range(1, products + 1):
        print prev_month.strftime('%m%Y'), p,  random.randint(1, 100)